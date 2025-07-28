# 🧾 Mapping des données Account Payables – Projet Datahub Infor M3

Ce projet a pour objectif de réaliser le **mapping des données Finance / Achats** du système ERP Infor M3 vers un Datahub d'entreprise. Cette étape se concentre sur le domaine **Account Payables**, avec un chargement en base \`staging\` et des validations automatisées de la qualité des données.

---

## 🎯 Objectifs pédagogiques

- Comprendre les étapes d’un pipeline de données orienté Finance
- Identifier et charger les bonnes données depuis M3
- Contrôler leur qualité à travers des tests automatisés (pytest)
- Préparer les données pour la modélisation dans le Datahub

---

## 📁 Structure du projet

\`\`\`
Mapping-Infor-M3/
├── raw_data/                      # Données brutes simulant un export M3
│   └── AccountPayables.csv
├── src/                           # Scripts ETL (extract/load)
│   ├── extract_ap.py              # Extraction CSV simulée
│   └── load_ap.py                 # Chargement en base staging
├── tests/
│   └── test_mapping_ap.py         # Tests qualité automatisés (pytest)
├── notebooks/
│   └── eda_ap.ipynb               # Analyse exploratoire des données
├── database/
│   └── modele_dimensionnel_ap.md  # Notes sur le futur modèle cible
├── .env                           # Chaîne de connexion DB
└── README.md
\`\`\`

---

## 🔄 Pipeline mis en œuvre

### 1. 📥 Extraction
Le fichier \`AccountPayables.csv\` contient les colonnes suivantes :
- \`invoice_id\`, \`supplier_id\`, \`amount\`, \`invoice_date\`, \`due_date\`

### 2. 📤 Chargement
Le script \`load_ap.py\` charge les données dans la table SQL :
\`\`\`sql
staging.stg_account_payables
\`\`\`
via SQLAlchemy, avec création automatique de la table si elle n'existe pas.

### 3. 🔎 Validation (tests unitaires)
Des tests \`pytest\` vérifient :
- Présence de données
- Montants positifs
- Absence de valeurs nulles dans les colonnes clés
- Ordre logique des dates (due_date ≥ invoice_date)

### 4. 📊 EDA (Analyse exploratoire)
Un notebook \`eda_ap.ipynb\` explore :
- Les statistiques descriptives
- Les valeurs manquantes
- Les distributions des montants
- Les doublons
- La répartition des délais de paiement

---

## 🔐 Exemple de configuration \`.env\`

\`\`\`
CONN_STR=mssql+pyodbc://sa:TestPass123!@localhost:1433/datahub_finance_achats?driver=ODBC+Driver+17+for+SQL+Server
\`\`\`

---

## 🚀 Prochaines étapes

- Appliquer la même logique à d'autres jeux de données : \`Account Receivables\`, \`Payment Terms\`, \`P&L\`, \`General Ledger\`
- Enrichir les règles de qualité avec des contraintes métiers plus fines
- Construire le modèle dimensionnel cible pour le Datahub

---

## 👨‍💻 Compétences mobilisées

- Lecture et analyse de données brutes ERP (simulées)
- Modélisation des règles de qualité
- Utilisation de \`pandas\`, \`sqlalchemy\`, \`pytest\`, \`matplotlib\`
- Reproductibilité avec environnement virtuel et \`dotenv\`

---

## 📚 Références

- Documentation [Infor M3 Finance Data Model](https://www.infor.com/)
- SQLAlchemy Docs : https://docs.sqlalchemy.org/
- Pandas Profiling : https://pandas-profiling.github.io/
EOF
