# 🏠 House Price Prediction App

Application web de prédiction des prix de l’immobilier basée sur le Machine Learning, développée avec **Python**, **Scikit-learn** et **Streamlit**.

---

## 📌 Description du projet

Cette application permet d’estimer le prix d’un bien immobilier à partir de ses caractéristiques principales grâce à un modèle de Machine Learning.

L’utilisateur renseigne les informations du logement (surface, nombre de chambres, salles de bain, parking, etc.) et l’application fournit une estimation du prix en temps réel.

Ce projet illustre une approche **end-to-end de Data Science**, allant de la préparation des données jusqu’au déploiement d’une application interactive.

---

## 🎯 Objectifs

- Automatiser l’estimation des prix immobiliers  
- Mettre en pratique un projet complet de Data Science  
- Développer un modèle prédictif fiable  
- Concevoir une application web interactive avec Streamlit  
- Proposer une interface moderne et intuitive  

---

## 🤖 Modèle de Machine Learning

### Type de modèle

- **Régression supervisée**

### Algorithme utilisé

- **Random Forest Regressor**

### Librairies principales

- **Scikit-learn**
- **Pandas**
- **NumPy**

### Pourquoi ce modèle ?

Le modèle **Random Forest Regressor** a été choisi pour sa robustesse, sa capacité à gérer les données tabulaires et sa bonne performance sur des relations non linéaires.

---

## 📊 Variables utilisées

Le modèle prend en compte plusieurs caractéristiques du bien immobilier, notamment :

- Surface  
- Nombre de chambres  
- Nombre de salles de bain  
- Nombre d’étages  
- Nombre de places de parking  
- Climatisation  
- Présence d’une route principale  
- Présence d’une chambre d’amis  
- Sous-sol  
- Chauffage à eau chaude  
- Zone préférée  
- Type de mobilier  

---

## 🖥️ Fonctionnalités de l’application

L’application propose :

- Une interface moderne type SaaS  
- Une saisie intuitive des caractéristiques du bien  
- Une estimation du prix en temps réel  
- Un résumé des caractéristiques après prédiction  
- Une lecture simplifiée des facteurs influents  
- L’importation d’un fichier CSV pour effectuer plusieurs prédictions à la fois  

---

## ⚙️ Technologies utilisées

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**

---

## 📁 Structure du projet

```bash
    house-price-prediction/
    │
    ├── data/               # Données utilisées
    ├── models/             # Modèle entraîné
    ├── src/                # Scripts (train, preprocess, predict)
    ├── images/             # Captures d’écran
    ├── app.py              # Application Streamlit
    ├── requirements.txt    # Dépendances
    └── README.md

--- 

## 📸 Aperçu de l’application

Voici quelques captures d’écran de l’application :

![Interface principale](images/home_page.png)
![Résultat de prédiction](images/predict_page.png)

---

## 💡 Perspectives d’amélioration

- Optimisation des performances du modèle  
- Ajout de nouvelles variables explicatives  
- Déploiement en ligne  
- Amélioration continue de l’interface utiapp_result.lisateur  
- Comparaison avec d’autres modèles de régression  

---

## 👨‍💻 Auteur

**Ange Désiré Boua**  
Étudiant en **Master 2 Big Data & Intelligence Artificielle**  
📍 Institut Universitaire d’Abidjan (Côte d’Ivoire)  
📧 angedesireboua@gmail.com  

---

##  Conclusion

Ce projet démontre ma capacité à concevoir une solution complète de Data Science, depuis l’analyse des données jusqu’au déploiement d’une application interactive et exploitable.