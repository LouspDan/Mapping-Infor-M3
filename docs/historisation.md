# Stratégie d’historisation des données

## SCD Type 1  
**Quoi ?** Écrase les anciennes valeurs sans garder de trace.  
**Quand ?** Pour corriger une erreur ou mettre à jour un libellé.  
**Avantage ?** Simplicité et rapidité.  
**Inconvénient ?** Perte de l’historique.

## SCD Type 2  
**Quoi ?** Conserve chaque version : on ajoute une nouvelle ligne à chaque changement.  
**Quand ?** Pour suivre précisément l’évolution d’un attribut (ex. statut d’une facture).  
**Avantage ?** Historique complet et traçable.  
**Inconvénient ?** Complexité et volume de données plus élevé.

## Change Data Capture (CDC)  
**Quoi ?** Mécanisme automatique qui détecte insertions, mises à jour et suppressions dans la source.  
**Quand ?** Pour automatiser l’ingestion incrémentale et alimenter les tables historiques.  
**Avantage ?** Processus performant et peu invasif sur la base source.  
**Inconvénient ?** Mise en place plus technique (configuration des logs).
