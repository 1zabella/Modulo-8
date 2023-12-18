from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import boto3
import pandas as pd
from dotenv import load_dotenv
import os
import logging
from io import BytesIO

load_dotenv()

class Config:
    def __init__(self):
        load_dotenv()
        self.aws_region_name = os.getenv('AWS_REGION_NAME')
        self.aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.aws_session_token = os.getenv('AWS_SESSION_TOKEN')

class S3Handler:
    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_region_name, aws_session_token):
        self.client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region_name,
            aws_session_token=aws_session_token
        )

    def list_buckets(self):
        response = self.client.list_buckets()
        return [bucket['Name'] for bucket in response.get('Buckets', [])]

config = Config()
s3_handler = S3Handler(config.aws_access_key_id, config.aws_secret_access_key, config.aws_region_name, config.aws_session_token)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'conexao_com_aws',
    default_args=default_args,
    description='Esta DAG será utilizada para conectar com o Amazon S3',
    schedule_interval=timedelta(days=1),
)

def connect_to_s3():
    try:
        buckets = s3_handler.list_buckets()
        logging.info("Buckets S3:")
        for bucket in buckets:
            logging.info(f' - {bucket}')
    except Exception as e:
        logging.error(f"Error connecting to S3: {e}")

s3_bucket_connection_task = PythonOperator(
    task_id='s3_bucket_connection_task',
    python_callable=connect_to_s3,
    dag=dag,
)

def choose_bucket():
    chosen_bucket = 'atividade-ponderada-airflow'
    logging.info("Bucket Escolhido: %s", chosen_bucket)
    return chosen_bucket

choose_bucket_task = PythonOperator(
    task_id='choose_bucket',
    python_callable=choose_bucket,
    dag=dag,
)

class FileProcessor:
    def __init__(self, s3_handler, chosen_bucket, chosen_file):
        self.s3_handler = s3_handler
        self.chosen_bucket = chosen_bucket
        self.chosen_file = chosen_file

    def download_file_from_s3(self):
        with BytesIO() as file_buffer:
            self.s3_handler.download_fileobj(Bucket=self.chosen_bucket, Key=self.chosen_file, Fileobj=file_buffer)
            file_buffer.seek(0)
            df = pd.read_csv(file_buffer, encoding='latin1')
        return df

    def remove_special_characters(self, df):
        df = df.applymap(lambda x: ''.join(e for e in x if e.isalnum() or e.isspace()) if isinstance(x, str) else x)
        return df

    def preprocess_data(self, df):
        df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
        df = self.remove_special_characters(df)

        if df.isnull().values.any():
            logging.info("Dados nulos encontrados. Preenchendo com 'N/A'...")
            df.fillna('N/A', inplace=True)

        return df

    def upload_processed_file_to_s3(self, df):
        with BytesIO() as processed_buffer:
            df.to_csv(processed_buffer, index=False)
            processed_buffer.seek(0)
            self.s3_handler.upload_fileobj(processed_buffer, Bucket=self.chosen_bucket, Key=self.chosen_file)

def preprocess_file(**kwargs):
    ti = kwargs['ti']
    chosen_bucket = ti.xcom_pull(task_ids='choose_bucket')
    chosen_file = 'Listagem_dos_Filmes_Brasileiros_e_Estrangeiros_Exibidos_2009_a_2019.csv'  

    file_processor = FileProcessor(s3_handler, chosen_bucket, chosen_file)

    try:
        df = file_processor.download_file_from_s3()
        processed_df = file_processor.preprocess_data(df)
        file_processor.upload_processed_file_to_s3(processed_df)
        logging.info("Arquivo pré-processado salvo no S3.")
        return 'branch_has_nulls' if processed_df.isnull().values.any() else 'branch_no_nulls'
    except Exception as e:
        logging.error(f"Error preprocessing file: {e}")
        return 'branch_no_nulls'

preprocess_file_task = PythonOperator(
    task_id='preprocess_file',
    python_callable=preprocess_file,
    provide_context=True,
    dag=dag,
)

s3_bucket_connection_task >> choose_bucket_task >> preprocess_file_task 

if __name__ == "__main__":
    dag.cli()