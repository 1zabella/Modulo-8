from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer, KNNImputer


def create_preproc_ordinal():
    feat_ordinal_dict = {
        # considers "missing" as the worse category
        "BsmtCond": ['missing', 'Po', 'Fa', 'TA', 'Gd'],
        "BsmtExposure": ['missing', 'No', 'Mn', 'Av', 'Gd'],
        "BsmtFinType1": ['missing', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'],
        "BsmtFinType2": ['missing', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'],
        "BsmtQual": ['missing', 'Fa', 'TA', 'Gd', 'Ex'],
        "Electrical": ['missing', 'Mix', 'FuseP', 'FuseF', 'FuseA', 'SBrkr'],
        "ExterCond": ['missing', 'Po', 'Fa', 'TA', 'Gd', 'Ex'],
        "ExterQual": ['missing', 'Fa', 'TA', 'Gd', 'Ex'],
        "Fence": ['missing', 'MnWw', 'GdWo', 'MnPrv', 'GdPrv'],
        "FireplaceQu": ['missing', 'Po', 'Fa', 'TA', 'Gd', 'Ex'],
        "Functional": ['missing', 'Sev', 'Maj2', 'Maj1', 'Mod', 'Min2', 'Min1', 'Typ'],
        "GarageCond": ['missing', 'Po', 'Fa', 'TA', 'Gd', 'Ex'],
        "GarageFinish": ['missing', 'Unf', 'RFn', 'Fin'],
        "GarageQual": ['missing', 'Po', 'Fa', 'TA', 'Gd', 'Ex'],
        "HeatingQC": ['missing', 'Po', 'Fa', 'TA', 'Gd', 'Ex'],
        "KitchenQual": ['missing', 'Fa', 'TA', 'Gd', 'Ex'],
        "LandContour": ['missing', 'Low', 'Bnk', 'HLS', 'Lvl'],
        "LandSlope": ['missing', 'Sev', 'Mod', 'Gtl'],
        "LotShape": ['missing', 'IR3', 'IR2', 'IR1', 'Reg'],
        "PavedDrive": ['missing', 'N', 'P', 'Y'],
        "PoolQC": ['missing', 'Fa', 'Gd', 'Ex'],
    }

    feat_ordinal = sorted(feat_ordinal_dict.keys())
    feat_ordinal_values_sorted = [feat_ordinal_dict[i] for i in feat_ordinal]

    encoder_ordinal = OrdinalEncoder(
        categories=feat_ordinal_values_sorted,
        handle_unknown="use_encoded_value",
        unknown_value=-1  # Considers unknown values as worse than "missing"
    )

    preproc_ordinal = make_pipeline(
        SimpleImputer(strategy="constant", fill_value="missing"),
        encoder_ordinal,
        MinMaxScaler()
    )

    return preproc_ordinal, feat_ordinal


def create_preproc_numerical():
    return make_pipeline(
        KNNImputer(),
        MinMaxScaler()
    )

def create_preproc_nominal():
    return make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        OneHotEncoder(handle_unknown="ignore")
    )

