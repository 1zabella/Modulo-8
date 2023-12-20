"""
COMPUTE AND PRINT CROSS VALIDATED RMSLE OF A PIPELINED MODEL
FOR THE KAGGLE HOUSES ADVANCED REGRESSION CHALLENGE
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, make_scorer

from houses_trainer.pipeline import create_pipeline

class Trainer:
    url_train = "data/houses_train_raw.csv"

    def __init__(self):
        self.data = None
        self.X = None
        self.y = None
        self.y_log = None
        self.cachedir = None
        self.pipe = None

    def load_data(self):
        print("---- loading data... ----")
        self.data = pd.read_csv(self.url_train)
        self.X = self.data.drop(columns='SalePrice')
        self.y = self.data.SalePrice
        self.y_log = np.log(self.y)
        print(f"---- X shape: {self.X.shape} ----")

    def build_pipeline(self, feature_cutoff_percentage=75):
        print("---- preprocessing... ----")
        self.pipe = create_pipeline(self.X, self.y, feature_cutoff_percentage)
        # print shape post feature preprocessing
        self.X_preproc = \
            self.pipe.named_steps["pipeline"].fit_transform(self.X, self.y_log)
        print(f"---- X shape: {self.X_preproc.shape} ----")

    def cross_validate(self, cv=5):
        print(f"---- cross validate {cv} folds----")
        rmse = make_scorer(
            lambda y, y_true: mean_squared_error(y, y_true)**0.5)
        cvs = cross_val_score(
            self.pipe, self.X, self.y_log,
            cv=5, scoring=rmse, n_jobs=-1)
        print(f'Mean RMSLE: {cvs.mean()} /n Standard Dev : {cvs.std()}')


# Instanciate trainer
trainer = Trainer()
# Load data
trainer.load_data()
# Build Pipeline
trainer.build_pipeline(
    feature_cutoff_percentage=75
)
# Cross validate
trainer.cross_validate(cv=5)
