# ======================================
# PRÉTRAITEMENT DES DONNÉES
# ======================================

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def build_preprocessor():
    """
    Construit le préprocesseur des données.
    """

    numerical_features = [
        "area",
        "bedrooms",
        "bathrooms",
        "stories",
        "parking"
    ]

    categorical_features = [
        "mainroad",
        "guestroom",
        "basement",
        "hotwaterheating",
        "airconditioning",
        "prefarea",
        "furnishingstatus"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numerical_features),
            ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_features)
        ]
    )

    return preprocessor