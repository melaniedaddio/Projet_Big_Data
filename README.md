# Projet Analyse et Traitement de Données
# Résumé des Exercices

## Exercice 1 : Calcul du nombre d'amis en commun avec MapReduce

Dans cet exercice, l'objectif était de calculer le nombre d'amis en commun entre chaque paire d'utilisateurs dans un réseau social. Le fichier `amis.txt` contient des données sur les utilisateurs et leurs amis. Nous avons utilisé une approche MapReduce pour:
1. Mapper les paires d'utilisateurs en associant leurs amis respectifs.
2. Réduire ces paires pour calculer l'intersection des amis et déterminer le nombre d'amis en commun.

Le programme génère le nombre d'amis communs pour chaque paire d'utilisateurs dans le fichier, permettant une analyse de la structure sociale du réseau.

---

## Exercice 2 : Calcul des k mots les plus fréquents d'un site Web

Dans ce deuxième exercice, le but était d'extraire le texte brut d'un site Web, de nettoyer les données, puis de calculer les mots les plus fréquents à l'aide d'un modèle MapReduce. Voici les principales étapes :
1. Extraction du texte brut à l'aide de `BeautifulSoup`.
2. Nettoyage du texte pour ne conserver que les mots significatifs (d'une longueur minimum de 4 caractères).
3. Application de MapReduce pour compter la fréquence des mots et trier les `k` mots les plus fréquents.
4. Sauvegarde des résultats dans un fichier `.txt`.

Ce programme permet de déterminer les mots les plus répétés sur un site Web, fournissant une analyse textuelle utile.

---

## Exercice 3 : Prédiction de la probabilité de défaut de paiement d'un prêt hypothécaire

Cet exercice visait à prédire la probabilité qu'un individu fasse défaut sur un prêt hypothécaire, à partir d'un ensemble de données bancaires. Les étapes suivantes ont été suivies :
1. **Prétraitement des données** : gestion des valeurs manquantes, séparation des données en ensembles d'entraînement, validation et test, et encodage des variables catégorielles.
2. **Modélisation** : trois modèles ont été testés pour la prédiction, incluant la régression logistique, l'arbre de décision et le KNN.
3. **Résultats** : L'arbre de décision a montré les meilleurs résultats pour prédire le défaut de paiement, surclassant les autres modèles en termes de performance et d'interprétabilité.

L'objectif final était de choisir le modèle le plus efficace pour prédire les défauts de paiement dans un cadre bancaire.

## Technologies utilisées

- **Python** : pour le traitement des données et l'implémentation des algorithmes.
- **PySpark** : pour l'implémentation du MapReduce dans le cadre du traitement parallèle.
- **SageMaker** : pour l'entraînement et le déploiement des modèles de machine learning.
- **BeautifulSoup** et **Regex** : pour le scraping et le nettoyage des données textuelles sur les sites Web.

---

## Auteurs
- Hurtado
- Daddio
- Sopguombue
