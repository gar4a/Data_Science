#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.decomposition import PCA

# Charger le jeu de données
data = pd.read_excel('C:/Users/ssghaier/Documents/.machine learning/Motor_Vehicle_Collisions_-_Crashes_20240131_cleaned.xlsx')

# Définir les critères de gravité et créer une étiquette de gravité
data['SEVERITY'] = pd.cut(data['NUMBER OF PERSONS INJURED'] + data['NUMBER OF PERSONS KILLED'],
                          bins=[-1, 0, 3, float('inf')],
                          labels=['minor', 'moderate', 'severe'])

# Définir les caractéristiques et la variable cible
X = data[['NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'BOROUGH', 'ZIP CODE', 'CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1']]
y = data['SEVERITY'] 

# Gérer les variables catégoriques
X = pd.get_dummies(X, columns=['BOROUGH', 'ZIP CODE', 'CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1'])

# Identifier les valeurs manquantes
missing_values = data.isnull().sum()

# Afficher les colonnes avec des valeurs manquantes
print(missing_values[missing_values > 0])

# Supprimer les lignes avec des valeurs manquantes
data.dropna(inplace=True)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Réduction de la dimensionnalité avec PCA
pca = PCA(n_components=100)  # Choisissez le nombre de composantes principales souhaitées
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Initialiser et entraîner le modèle RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_pca, y_train)

# Faire des prédictions et évaluer le modèle
y_pred = rf_classifier.predict(X_test_pca)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# In[ ]:




