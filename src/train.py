# IMPORTATION DES LIBRAIRIES


import os  # pour gérer les chemins des fichiers
import joblib  # pour sauvegarder le modèle
import pandas as pd  # pour manipuler les données

# outils machine learning
from sklearn.model_selection import train_test_split  # séparer les données
from sklearn.pipeline import Pipeline  # enchaîner preprocessing + modèle
from sklearn.ensemble import RandomForestRegressor  # modèle utilisé
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # métriques

# notre fonction de preprocessing
from src.preprocess import build_preprocessor


# FONCTION PRINCIPALE


def train_model():

   
    # CHEMINS DES FICHIERS
  
    # on récupère le dossier principal du projet
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # chemin vers le dataset
    dataset_path = os.path.join(project_root, "data", "Housing.csv")

    # chemin où on va sauvegarder le modèle
    model_output_path = os.path.join(project_root, "models", "house_price_model.pkl")


   
    # CHARGEMENT DES DONNÉES
    

    # on lit le fichier CSV
    housing_data = pd.read_csv(dataset_path)


   
    # SÉPARATION X / y
    

    # X = variables (features)
    feature_data = housing_data.drop("price", axis=1)

    # y = ce qu’on veut prédire
    target_price = housing_data["price"]


   
    # PRÉPROCESSING
    

    # on prépare les données (encodage, etc.)
    data_preprocessor = build_preprocessor()


   
    # TRAIN / TEST SPLIT
    

    # on sépare les données :
    # 80% entraînement, 20% test
    X_train, X_test, y_train, y_test = train_test_split(
        feature_data,
        target_price,
        test_size=0.2,
        random_state=42
    )


    
    # PIPELINE
   

    # pipeline = preprocessing + modèle
    machine_learning_pipeline = Pipeline(
        steps=[
            ("preprocessing", data_preprocessor),
            ("model", RandomForestRegressor(
                n_estimators=300,
                max_depth=20,
                min_samples_split=5,
                random_state=42
            ))
        ]
    )


    # ENTRAÎNEMENT
    
    # le modèle apprend à partir des données
    machine_learning_pipeline.fit(X_train, y_train)


    
    # PRÉDICTION
    

    # le modèle prédit sur les données test
    predicted_prices = machine_learning_pipeline.predict(X_test)


    # ------------------------------
    # ÉVALUATION
    # ------------------------------

    # erreur moyenne
    mae_score = mean_absolute_error(y_test, predicted_prices)

    # erreur plus sévère
    rmse_score = mean_squared_error(y_test, predicted_prices) ** 0.5

    # qualité globale du modèle
    r2_score_value = r2_score(y_test, predicted_prices)

    print("Résultats du modèle Random Forest")
    print(f"MAE  : {mae_score:.2f}")
    print(f"RMSE : {rmse_score:.2f}")
    print(f"R²   : {r2_score_value:.4f}")


    # ------------------------------
    # FEATURE IMPORTANCE
    # ------------------------------

    # on récupère le modèle
    trained_model = machine_learning_pipeline.named_steps["model"]

    # on récupère le preprocessing
    fitted_preprocessor = machine_learning_pipeline.named_steps["preprocessing"]

    # noms des colonnes après transformation
    feature_names = fitted_preprocessor.get_feature_names_out()

    # importance des variables
    importances = trained_model.feature_importances_

    # tableau clair
    feature_importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importances
    }).sort_values(by="importance", ascending=False)

    print("\nTop 10 features les plus importantes :")
    print(feature_importance_df.head(10))


   # SAUVEGARDE
   

    # on sauvegarde le modèle
    joblib.dump(machine_learning_pipeline, model_output_path)

    print(f"\nModèle sauvegardé dans : {model_output_path}")



# LANCEMENT DU SCRIPT


if __name__ == "__main__":
    train_model()