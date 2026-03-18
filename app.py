import os
import time
import joblib
import pandas as pd
import streamlit as st

# ======================================
# CONFIGURATION DE LA PAGE

st.set_page_config(
    page_title="Estimation immobilière",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# CHARGEMENT DU MODÈLE


project_root = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(project_root, "models", "house_price_model.pkl")
trained_model = joblib.load(model_path)

# CHEMIN DE L'IMAGE


banner_image_path = os.path.join(project_root, "images", "real_estate_banner.jpeg")


# STYLE CSS 


st.markdown(
    """
    <style>
        .stApp {
            background: #f8fafc;
        }

        .main-title {
            font-size: 3.1rem;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.05;
            letter-spacing: -0.04em;
            margin-bottom: 0.6rem;
        }

        .main-subtitle {
            font-size: 1.05rem;
            color: #475569;
            line-height: 1.7;
            margin-bottom: 1.2rem;
        }

        .hero-badge {
            display: inline-block;
            font-size: 0.9rem;
            font-weight: 700;
            color: #2563eb;
            background: #dbeafe;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            margin-bottom: 1rem;
        }

        .soft-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 1.2rem 1.3rem;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04);
            margin-bottom: 1rem;
        }

        .mini-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 1rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.03);
            text-align: center;
            height: 100%;
        }

        .section-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.55rem;
        }

        .section-text {
            color: #475569;
            font-size: 1rem;
            line-height: 1.7;
        }

        .result-card {
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            border-radius: 22px;
            padding: 1.4rem 1.5rem;
            color: white;
            box-shadow: 0 18px 34px rgba(37, 99, 235, 0.22);
            margin-top: 1rem;
            margin-bottom: 1rem;
            animation: fadeUp 0.45s ease;
        }

        .result-label {
            font-size: 0.95rem;
            font-weight: 700;
            color: #dbeafe;
            margin-bottom: 0.35rem;
        }

        .result-value {
            font-size: 2.5rem;
            font-weight: 900;
            letter-spacing: -0.03em;
        }

        .footer-note {
            color: #64748b;
            font-size: 0.92rem;
            text-align: center;
            margin-top: 2rem;
            line-height: 1.8;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white;
            border: none;
            border-radius: 14px;
            font-weight: 700;
            font-size: 1.05rem;
            letter-spacing: 0.3px;
            padding: 0.78rem 1rem;
            box-shadow: 0 12px 24px rgba(37, 99, 235, 0.18);
            transition: all 0.25s ease;
        }

        div.stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 16px 28px rgba(37, 99, 235, 0.25);
        }

        [data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid #e2e8f0;
        }

        @keyframes fadeUp {
            from {
                opacity: 0;
                transform: translateY(8px);
            }
            to {
                opacity: 1;
                transform: translateY(0px);
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================================
# SIDEBAR : SAISIE

with st.sidebar:
    st.header("Entrée")

    area = st.number_input("Surface", min_value=500, step=100, value=5000)
    bedrooms = st.selectbox("Nombre de chambres", options=list(range(1, 11)), index=2)
    bathrooms = st.selectbox("Nombre de salles de bain", options=list(range(1, 11)), index=1)
    stories = st.selectbox("Nombre d’étages", options=list(range(1, 6)), index=1)
    parking = st.selectbox("Places de parking", options=list(range(0, 11)), index=1)

    mainroad = st.selectbox("Route principale", ["yes", "no"], format_func=lambda v: "Oui" if v == "yes" else "Non")
    guestroom = st.selectbox("Chambre d’amis", ["yes", "no"], format_func=lambda v: "Oui" if v == "yes" else "Non")
    basement = st.selectbox("Sous-sol", ["yes", "no"], format_func=lambda v: "Oui" if v == "yes" else "Non")
    hotwaterheating = st.selectbox("Chauffage eau chaude", ["yes", "no"], format_func=lambda v: "Oui" if v == "yes" else "Non")
    airconditioning = st.selectbox("Climatisation", ["yes", "no"], format_func=lambda v: "Oui" if v == "yes" else "Non")
    prefarea = st.selectbox("Zone préférée", ["yes", "no"], format_func=lambda v: "Oui" if v == "yes" else "Non")

    furnishingstatus = st.selectbox(
        "Mobilier",
        ["furnished", "semi-furnished", "unfurnished"],
        format_func=lambda v: {
            "furnished": "Meublé",
            "semi-furnished": "Semi-meublé",
            "unfurnished": "Non meublé"
        }[v]
    )

    predict_button = st.button("✨ Estimer le prix", use_container_width=True)

    st.divider()
    st.subheader("Téléversement du CSV")
    uploaded_csv = st.file_uploader("Importer un fichier CSV", type=["csv"])

# ======================================
# HERO PRINCIPAL

hero_left, hero_right = st.columns([1.2, 1], gap="large")

with hero_left:
    st.markdown('<div class="hero-badge">🤖 Powered by AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Prédiction des prix de l’immobilier</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="main-subtitle">
            Estimez rapidement le prix d’un bien immobilier à partir de ses caractéristiques principales.
            Renseignez les informations dans la barre latérale, puis obtenez un résultat clair et professionnel.
        </div>
        """,
        unsafe_allow_html=True
    )

with hero_right:
    if os.path.exists(banner_image_path):
        st.image(banner_image_path, use_container_width=True)
    else:
        st.markdown(
            """
            <div class="soft-card" style="min-height:240px; display:flex; align-items:center; justify-content:center;">
                <div style="text-align:center;">
                    <div style="font-size:3rem;">🏠</div>
                    <div class="section-title">Image du projet</div>
                    <div class="section-text">Ajoute une image dans <code>images/real_estate_banner.jpeg</code></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ======================================
# À PROPOS

st.markdown(
    """
    <div class="soft-card">
        <div class="section-title">À propos de cette application</div>
        <div class="section-text">
            Cette application estime le prix d’un bien immobilier à partir de ses caractéristiques principales.
            Les informations sont saisies dans la barre latérale, et les résultats sont affichés de façon claire,
            avec une lecture rapide et un traitement possible de fichiers CSV.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ======================================
# DONNÉES D'ENTRÉE

input_data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "mainroad": [mainroad],
    "guestroom": [guestroom],
    "basement": [basement],
    "hotwaterheating": [hotwaterheating],
    "airconditioning": [airconditioning],
    "parking": [parking],
    "prefarea": [prefarea],
    "furnishingstatus": [furnishingstatus]
})

# ======================================
# PRÉDICTION 


if predict_button:
    validation_errors = []

    if area <= 0:
        validation_errors.append("La surface doit être supérieure à 0.")
    if bedrooms <= 0:
        validation_errors.append("Le nombre de chambres doit être supérieur à 0.")
    if bathrooms <= 0:
        validation_errors.append("Le nombre de salles de bain doit être supérieur à 0.")
    if stories <= 0:
        validation_errors.append("Le nombre d’étages doit être supérieur à 0.")
    if parking < 0:
        validation_errors.append("Le nombre de places de parking ne peut pas être négatif.")

    if validation_errors:
        for error in validation_errors:
            st.error(error)
    else:
        with st.spinner("Calcul de l'estimation en cours..."):
            prediction_result = trained_model.predict(input_data)[0]

        formatted_price = f"{prediction_result:,.0f}".replace(",", " ")

        st.success("✔️ Estimation générée avec succès")

        # Résumé affiché 
        summary_col_1, summary_col_2, summary_col_3 = st.columns(3, gap="medium")

        with summary_col_1:
            st.markdown(
                f"""
                <div class="mini-card">
                    <div class="section-title">Surface</div>
                    <div style="font-size:2rem; font-weight:800; color:#0f172a;">
                        {f"{area:,}".replace(",", " ")} m²
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with summary_col_2:
            st.markdown(
                f"""
                <div class="mini-card">
                    <div class="section-title">Chambres</div>
                    <div style="font-size:2rem; font-weight:800; color:#0f172a;">
                        {bedrooms}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with summary_col_3:
            st.markdown(
                f"""
                <div class="mini-card">
                    <div class="section-title">Salles de bain</div>
                    <div style="font-size:2rem; font-weight:800; color:#0f172a;">
                        {bathrooms}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        placeholder = st.empty()
        step_value = max(1, int(prediction_result / 30))

        for i in range(0, int(prediction_result), step_value):
            placeholder.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Estimation du prix</div>
                    <div class="result-value">{f"{i:,.0f}".replace(",", " ")} FCFA</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            time.sleep(0.01)

        placeholder.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">Estimation du prix</div>
                <div class="result-value">{formatted_price} FCFA</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption("💡 Cette estimation est basée sur un modèle de Machine Learning entraîné sur des données immobilières.")

        st.markdown(
            """
            <div class="soft-card">
                <div class="section-title">Lecture rapide</div>
                <div class="section-text">
                    Les facteurs les plus influents dans l’estimation incluent généralement la surface,
                    le nombre de salles de bain, la climatisation, le parking et le nombre d’étages.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.info("Renseignez les informations dans la barre latérale puis cliquez sur « Estimer le prix ».")

# ======================================
# PRÉDICTIONS MULTIPLES VIA CSV


if uploaded_csv is not None:
    try:
        uploaded_data = pd.read_csv(uploaded_csv)

        st.markdown(
            """
            <div class="soft-card">
                <div class="section-title">Aperçu du fichier importé</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.dataframe(uploaded_data.head())

        required_columns = [
            "area", "bedrooms", "bathrooms", "stories", "mainroad",
            "guestroom", "basement", "hotwaterheating", "airconditioning",
            "parking", "prefarea", "furnishingstatus"
        ]

        missing_columns = [column for column in required_columns if column not in uploaded_data.columns]

        if missing_columns:
            st.error(f"Colonnes manquantes dans le CSV : {missing_columns}")
        else:
            uploaded_data["predicted_price_fcfa"] = trained_model.predict(uploaded_data)

            st.markdown(
                """
                <div class="soft-card">
                    <div class="section-title">Résultats des prédictions multiples</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.dataframe(uploaded_data)

    except Exception as error:
        st.error(f"Erreur lors du traitement du fichier CSV : {error}")

# ======================================
# FOOTER


st.markdown(
    """
    <div class="footer-note">
        Application développée avec Streamlit dans le cadre d’un projet de machine learning sur la prédiction des prix.
        <br>
        Auteur : Ange Désiré Boua - Étudiant en Data Science <br>
        <br>
        gmail : angedesireboua@gmail.com
    </div>
    """,
    unsafe_allow_html=True
)