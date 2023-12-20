from houses_trainer.preprocessors import create_preproc_nominal, create_preproc_numerical, create_preproc_ordinal

from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.feature_selection import SelectPercentile, mutual_info_regression
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import StackingRegressor


def create_preproc(X, y=None, feature_cutoff_percentile=75):
    preproc_ordinal, feat_ordinal = create_preproc_ordinal()
    
    preproc_numerical = create_preproc_numerical()
    feat_numerical = sorted(X.select_dtypes(
        include=["int64", "float64"]).columns)
    
    preproc_nominal = create_preproc_nominal()
    feat_nominal = sorted(
        list(set(X.columns) - set(feat_numerical) - set(feat_ordinal)))
    
    feature_transformer = make_column_transformer(
        (preproc_numerical, feat_numerical),
        (preproc_ordinal, feat_ordinal),
        (preproc_nominal, feat_nominal),
        remainder="drop")

    feature_selector = SelectPercentile(
        mutual_info_regression,
        percentile=feature_cutoff_percentile,  # keep only xx% of all features
    )

    preproc = make_pipeline(
        feature_transformer,
        feature_selector
    )

    return preproc


def create_model(X, y=None):
    gboost = GradientBoostingRegressor(n_estimators=100)
    ridge = Ridge()
    svm = SVR(C=1, epsilon=0.05)
    adaboost = AdaBoostRegressor(
        base_estimator=DecisionTreeRegressor(max_depth=None))

    model = StackingRegressor(
        estimators=[("gboost", gboost),
                    ("adaboost", adaboost),
                    ("ridge", ridge),
                    ("svm_rbf", svm)],
        final_estimator=LinearRegression(),
        cv=5,
        n_jobs=-1
    )
    return model


def create_pipeline(X, y=None, feature_cutoff_percentile=75):

    pipe = make_pipeline(
        create_preproc(X, y, feature_cutoff_percentile),
        create_model(X, y),
    )
    return pipe
