#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import glob
import csv
import numpy as np
import os
from collections import Counter
import math

def valeur_plus_frequente(liste):
    # Filtrer les valeurs qui sont des chaînes de caractères et différentes de None
    valeurs_str = [valeur for valeur in liste if (isinstance(valeur, str) 
                    or (isinstance(valeur, float) 
                    and not math.isnan(valeur))) and valeur is not None 
                    and valeur != "nan" and valeur != 0.0]
    # Vérifier si la liste filtrée est vide
    if not valeurs_str:
        return None
    # Utiliser Counter pour compter le nombre d'occurrences de chaque élément
    compteur = Counter(valeurs_str)
    # Utiliser max() avec une fonction lambda pour obtenir l'élément avec le plus grand nombre d'occurrences
    valeur_plus_frequente = max(compteur, key=compteur.get)
    return valeur_plus_frequente

# Définir une fonction pour nettoyer chaque valeur de la colonne
def clean_string(encoded_string):
    if isinstance(encoded_string, str):  # Vérifiez si la valeur est une chaîne de caractères
        # Décoder la chaîne depuis l'UTF-8 avec 'replace' pour gérer les caractères non décodables
        decoded_string = encoded_string.encode('latin1').decode('utf-8', errors='replace')
        # Réencoder la chaîne en latin1
        cleaned_string = decoded_string.encode('latin1')
    else:
        return encoded_string  # Retourner la valeur telle quelle si elle n'est pas une chaîne de caractères

def detect_csv_separator(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))  # Reads the first 1024 bytes to detect the delimiter
        return dialect.delimiter
    
    
# Define a function to clean and convert the data
def clean_and_convert(data):
    # Check if data is null or empty
    if data is None or data == '':
        return '-1'
    # Convert data to string if it's not already
    data_str = str(data)
    # Remove non-numeric characters
    cleaned_data = ''.join(filter(str.isdigit, data_str))
    return cleaned_data

def categorize_vehicle(code_vehicule):
    if code_vehicule in [1, 2, 3, 10, 11, 12, 41, 42, 43, 50, 60, 80]:
        return 1  # 'Passagers Véhicules'
    elif code_vehicule in [4, 5, 6, 30, 31, 32, 33, 34, 35, 36]:
        return 2  # 'Motocyclettes'
    elif code_vehicule in [7, 8, 9]:
        return 3  # 'Camions légers'
    elif code_vehicule in [13, 14, 15, 16, 17]:
        return 4  # 'Gros Camions'
    elif code_vehicule in [18, 19, 20, 21, 37, 38, 39, 40]:
        return 5  # 'Transport Public'
    else:
        return 0  # 'Autres/Inconnus'

def actp(input):
    return str(input)[:1]
 
print('END')


# In[38]:


#caracteristique
# Get a list of all CSV files in the directory
files = glob.glob('../Downloads/car*.csv'
# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()
# Loop through each file and append its data to the combined DataFrame
for file in files:
    print(file)
    # Read the first row of the file to infer data types
    separator = detect_csv_separator(file)
    #dtypes = pd.read_csv(file, nrows=1,encoding='ansi').dtypes.to_dict()
    print(separator)
    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, encoding='ansi', sep=separator, quotechar='"')
    combined_data = pd.concat([combined_data, df], ignore_index=True)
    
# Now 'combined_data' contains data from all CSV files
combined_data['Num_Acc'] = combined_data['Num_Acc'].fillna(combined_data['Accident_Id'])
combined_data = combined_data.drop(columns=['Accident_Id'])

# Supprimer les colonnes "gps" et "dep" et "com"
combined_data.drop(columns=['gps', 'dep', 'com'], inplace=True)

float_columns = combined_data.select_dtypes(include=['float']).columns
combined_data[float_columns] = combined_data[float_columns].fillna(0)
combined_data[float_columns] = combined_data[float_columns].astype(np.int64)

string_columns = combined_data.select_dtypes(include=['object']).columns
adr_freq = str(valeur_plus_frequente(combined_data['adr']))
print('valeur_plus_frequente adr '+ adr_freq)
combined_data['adr'].fillna(value=adr_freq, inplace=True)
lat_freq = str(valeur_plus_frequente(combined_data['lat']))
print('valeur_plus_frequente lat '+ lat_freq)
combined_data['lat'].fillna(value=lat_freq, inplace=True)
long_freq = str(valeur_plus_frequente(combined_data['long']))
print('valeur_plus_frequente long '+ long_freq)
combined_data['long'].fillna(value=long_freq, inplace=True)

# Chemin du fichier de sortie
output_file = '../csv/caracteristiques.csv'

# Vérifier si le fichier existe
if os.path.exists(output_file):
    # Si le fichier existe, le supprimer
    os.remove(output_file)

# Enregistrer le nouveau fichier CSV
combined_data.to_csv(output_file, sep='|', index=False)
print('End Caracteristiques')


# In[71]:



#usagers
# Get a list of all CSV files in the directory
files = glob.glob('../Downloads/usagers*.csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each file and append its data to the combined DataFrame
for file in files:
    print(file)
    # Read the first row of the file to infer data types
    separator = detect_csv_separator(file)
    #dtypes = pd.read_csv(file, nrows=1).dtypes.to_dict()
    print(separator)
    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, encoding='ansi', sep=separator, quotechar='"')

    combined_data = pd.concat([combined_data, df], ignore_index=True)
    
# Now 'combined_data' contains data from all CSV files
# Supprimer les colonnes "secu", "secu1", "secu2" et "secu3"
combined_data.drop(columns=['secu', 'secu1', 'secu2', 'secu3'], inplace=True)

# Replace the problematic data in the column
combined_data['id_vehicule'] = combined_data['id_vehicule'].apply(clean_and_convert)
combined_data['id_usager'] = combined_data['id_usager'].apply(clean_and_convert)

column_types = df.dtypes
print(column_types)
print(combined_data['actp'])
float_columns = combined_data.select_dtypes(include=['float']).columns
print(float_columns)
combined_data[float_columns] = combined_data[float_columns].fillna(0)
combined_data[float_columns] = combined_data[float_columns].astype(np.int64)
combined_data['actp'] = combined_data['actp'].apply(actp)
print(combined_data['actp'])
string_columns = combined_data.select_dtypes(include=['object']).columns

combined_data[string_columns] = combined_data[string_columns].fillna(value='na')

combined_data.to_csv('../csv/usagers.csv', sep='|', index=False)

print('end Usager')


# In[64]:


#vehicules
# Get a list of all CSV files in the directory
files = glob.glob('../Downloads/vehicules*.csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each file and append its data to the combined DataFrame
for file in files:
    print(file)
    # Read the first row of the file to infer data types
    separator = detect_csv_separator(file)
    #dtypes = pd.read_csv(file, nrows=1).dtypes.to_dict()
    print(separator)
    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, encoding='ansi', sep=separator, quotechar='"')
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Now 'combined_data' contains data from all CSV files
# Replace the problematic data in the column
combined_data['id_vehicule'] = combined_data['id_vehicule'].apply(clean_and_convert)

# Aggregation 
# 1 - 'Passagers Véhicules'[1, 2, 3, 10, 11, 12, 41, 42, 43, 50, 60, 80]
# 2 - 'Motocyclettes' [4, 5, 6, 30, 31, 32, 33, 34, 35, 36]
# 3 - 'Camions légers' [7, 8, 9]
# 4 - 'Gros Camions' [13, 14, 15, 16, 17]
# 5 - 'Transport Public' [18, 19, 20, 21, 37, 38, 39, 40]
# 0 - 'Autres/Inconnus' [90]
combined_data['catv'] = combined_data['catv'].apply(categorize_vehicle)

float_columns = combined_data.select_dtypes(include=['float']).columns
combined_data[float_columns] = combined_data[float_columns].fillna(0)
combined_data[float_columns] = combined_data[float_columns].astype(np.int64)
string_columns = combined_data.select_dtypes(include=['object']).columns
combined_data[string_columns] = combined_data[string_columns].fillna(value='NA')
print(df.dtypes)
# Chemin du fichier de sortie
output_file = '../csv/vehicules.csv'

# Vérifier si le fichier existe
if os.path.exists(output_file):
    # Si le fichier existe, le supprimer
    os.remove(output_file)

# Enregistrer le nouveau fichier CSV
combined_data.to_csv(output_file, sep='|', index=False)
print('End Vehicules')


# In[ ]:



#lieux
# Get a list of all CSV files in the directory
files = glob.glob('../Downloads/lieux*.csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each file and append its data to the combined DataFrame
for file in files:
    print(file)
    # Read the first row of the file to infer data types
    separator = detect_csv_separator(file)
    #dtypes = pd.read_csv(file, nrows=1).dtypes.to_dict()
    print(separator)
    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, encoding='ansi', sep=separator, quotechar='"',low_memory=False)
    df['voie'] = df['voie'].astype(str)
    # Fill missing values with a specific value, e.g., 'Unknown'
    df['voie'].fillna('Unknown', inplace=True)
    
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Now 'combined_data' contains data from all CSV files
# Supprimer les colonnes "v1" et "v2" et "env1"
combined_data.drop(columns=['v1', 'v2', 'env1', 'pr' , 'pr1', 'nbv'], inplace=True)

float_columns = combined_data.select_dtypes(include=['float']).columns
print(float_columns)
combined_data[float_columns] = combined_data[float_columns].fillna(0)
combined_data[float_columns] = combined_data[float_columns].astype(np.int64)
string_columns = combined_data.select_dtypes(include=['object']).columns
print(string_columns)

voie_freq = str(valeur_plus_frequente(combined_data['voie']))
print('valeur_plus_frequente voie '+ voie_freq)
combined_data['voie'].fillna(value=voie_freq, inplace=True)

lartpc_freq = str(valeur_plus_frequente(combined_data['lartpc']))
print('valeur_plus_frequente lartpc '+ lartpc_freq)
combined_data['lartpc'].fillna(value=lartpc_freq, inplace=True)

larrout_freq = str(valeur_plus_frequente(combined_data['larrout']))
print('valeur_plus_frequente larrout '+ larrout_freq)
combined_data['larrout'].fillna(value=larrout_freq, inplace=True)

combined_data.to_csv('../csv/lieux.csv', sep='|',  index=False)
print('end lieux')


# In[ ]:




