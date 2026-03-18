import os
import joblib
import pandas as pd


def predict_new_house():
    """
    Charge le modèle sauvegardé et effectue une prédiction
    sur une nouvelle maison.
    """

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(project_root, "models", "house_price_model.pkl")

    trained_model = joblib.load(model_path)

    new_house_data = pd.DataFrame({
        "area": [6000],
        "bedrooms": [4],
        "bathrooms": [3],
        "stories": [2],
        "mainroad": ["yes"],
        "guestroom": ["no"],
        "basement": ["yes"],
        "hotwaterheating": ["no"],
        "airconditioning": ["yes"],
        "parking": [2],
        "prefarea": ["yes"],
        "furnishingstatus": ["semi-furnished"]
    })

    predicted_price = trained_model.predict(new_house_data)

    print("Prix prédit pour la nouvelle maison :", predicted_price[0])


if __name__ == "__main__":
    predict_new_house()