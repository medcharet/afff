import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CHARET's Portfolio",
    page_icon="✨",
    layout="wide",
)

# Header
st.title("🚀 CHARET Mohamed  🚀")
# st.subheader("Welcome to my world of finance, mathematics, and data!")
st.subheader("Elève ingénieur en troisième année Actuariat et Finance")
# Sidebar with personal information
st.sidebar.markdown(
    "<style>img {border-radius: 50%;}</style>", unsafe_allow_html=True
)
st.sidebar.image("CHARET_.png", width=150)
st.sidebar.header("Contact")
st.sidebar.markdown("- Email: m.charet@insea.ac.ma")
st.sidebar.markdown("- Phone: +212637143327")
st.sidebar.markdown("- Location: Rabat, Maroc")
# st.markdown(pdf_link(resume_url, "**Resume **"), unsafe_allow_html=True)
resume_url = "CV_CHARET_MOHAMED.pdf"
with open(resume_url, "rb") as file:
    btn = st.sidebar.download_button(
        label="Download Resume",
        data=file,
        file_name="CV_CHARET_MOHAMED.pdf",
        mime="application/pdf"
    )
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/mohamed-charet-952077223/)")

# Education section
st.header("📚 Education")
st.subheader("Ingénieur en Actuariat et Finance quantitative | INSEA")
st.markdown("10/2021 - 08/2024\nRabat, Maroc")

st.subheader("Licence Mathématique Appliquée | Faculté des sciences Ibn Zohr")
st.markdown("09/2018 - 06/2021\nAgadir, Maroc")

st.subheader("Baccalauréat Science Math A - Option Français | Lycée Hassan II")
st.markdown("09/2017 - 06/2018\nOulad Teima, Maroc")
# Experience section
st.header("🌟 Experience")
st.subheader("Consultant  | FRS Consulting")
st.markdown("07/2023 - 09/2023\nCasablanca, Maroc")
st.markdown(
    "- Etude des méthodes deterministes et stochastiques pour l’évaluation des provisions techniques.\n"
    "- Création d'une application web Python (avec Streamlit) pour l'évaluation des provisions techniques par la méthode de la CHAIN LADDER."
)
st.subheader("Gestionnaire de risque | Actuelia Afrique (Cabinet de Conseil en Actuariat)")
st.markdown("08/2028 - 09/2023\nCasablanca, Maroc")
st.markdown(
    "- Etude des indicateurs de Pilotage."
    "\n- Calcul du Capital de Solvabilité Requis (SCR) en utilisant à la fois la méthode standard et le modèle interne."
    "\n- Utilisation de la méthode de Simulation dans le Simulation (SdS) pour anticiper la distribution des fonds propres au future."
    # "\n- Exploration d'approches alternatives à SdS, notamment l'application de techniques de machine learning telles que XGBoost, Random Forest, et le modèle SVM (Support Vector Machine)."
)

st.subheader("Stage de découverte | HCP")
st.markdown("07/2022 - 08/2022\nAgadir, Maroc")
st.markdown(
    "- Analyse des données démographiques des ménages au sein de la région Souss Massa.\n"
    "- Réalisation d'une Analyse Exploratoire des Données (EDA)."
)

# Projects section
st.header("🚀 Projects")
st.subheader("Finance")
st.markdown("- Pricing des produits structurés")
st.markdown("- Modélisation et Analyse des Options Financières : Intégration du Modèle de Black-Scholes et Simulations de Monte Carlo.")
st.markdown("- Optimisation du ratio d'un portefeuille et création d'une application R Shiny.")

st.subheader("Assurance non-vie")
st.markdown("- Modélisation des montants et nombre de sinistre sous logiciel R.")
st.markdown("- Tarification des contrats en SAS.")
st.markdown("- Estimation des coûts des sinistres et provisionnement en R.")

st.subheader("Régression linéaire")
st.markdown("- Prédiction du prix des crypto monnaies sous R.")

st.subheader("Série chronologique")
st.markdown("- Prévision du prix du Bitcoin")

# Skills section
st.header("🔧 Compétences")
st.subheader("Finance")
st.markdown("- Mathématique financière, Finance de marché, Gestion de portefeuille.")
st.markdown("- Pricing, Calcul stochastique, Théorie des options.")
st.markdown("- Analyse quantitative, Econometrie de la finance, Courbes des taux, Monte Carlo.")

st.subheader("Actuariat")
st.markdown("- Tarification, Provisionnement, Assurance vie, Assurance Non-vie, Prévoyance, Réassurance.")

st.subheader("Statistique")
st.markdown("- Modélisation des séries temporelles, Régression linéaire, ANOVA.")
st.markdown("- Théorie des copules, Analyse Composantes Principales, Inférence statistique, Statistique multivariée, GLM.")

st.subheader("Informatique")
st.markdown("- LaTeX, C++, R, SAS, EXCEL/VBA, PYTHON.")

# Languages section
st.header("🌐 Langues")
st.markdown("- Arabe: Native")
st.markdown("- Français: Avancé")
st.markdown("- Anglais: Intermédiaire")

# Extracurricular activities section
st.header("🎉 Parascolaires")
st.markdown("- Membre du club INSEA CHARITY")
st.markdown("- Membre du club ENACTUS INSEA")

# Interests section
st.header("🗺️ Centres d'intérêt")
st.markdown("- Rédaction de rapports en LaTeX")
st.markdown("- Actualités et événements mondiaux")
st.markdown("- Sport")

# About me section
st.header("🚀 À propos")
st.markdown(
    "Jeune étudiant extrêmement motivé et passionné par les mathématiques, la finance et l'actuariat. "
    "Je suis autonome, responsable, rigoureux, créatif, adaptable et je m'intègre facilement au travail d'équipe. "
    "Actuellement, je suis à la recherche d'une opportunité de stage de fin d'études (PFE)."
)
