import pytest
import app  
import pandas as pd

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_coletar_dados():
    dados = app.coletar_dados()
    assert isinstance(dados, list)
    
def test_coletar_dados_erro():
    with pytest.raises(Exception):
        with requests_mock.Mocker() as m:
            m.get('https://api.openweathermap.org/data/2.5/weather', exc=Exception)
            coletar_dados()

def test_limpar_tabela(client):
    resultado = client.get('/clear_data')
    assert b'Tabela do banco de dados foi esvaziada' in resultado.data
    
def test_limpar_tabela_erro():
    with pytest.raises(Exception):
        with sqlite3.connect(':memory:') as conn:
            with conn.cursor() as cursor:
                limpar_tabela()

def test_criar_tabela():
    df = app.criar_tabela()
    assert isinstance(df, pd.DataFrame)
    
def test_criar_tabela_erro():
    with pytest.raises(Exception):
        with requests_mock.Mocker() as m:
            m.get('https://api.openweathermap.org/data/2.5/weather', exc=Exception)
            criar_tabela()