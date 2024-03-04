import pandas as pd
import json
import unidecode
import glob
import os

def clean_string(s):
    """ Nettoie la chaîne de caractères en remplaçant les caractères spéciaux """
    return unidecode.unidecode(s)

def detect_separator(csv_file):
    """ Détecte le séparateur dans un fichier CSV """
    with open(csv_file, 'r', encoding='ISO-8859-1') as file:
        first_line = file.readline()
        if ';' in first_line:
            return ';'
        else:
            return ','

def replace_values_in_csv(json_mappings_file, csv_files):
    with open(json_mappings_file, 'r', encoding='utf-8') as file:
        mappings = json.load(file)

    for key in mappings:
        if isinstance(mappings[key], list):
            mappings[key] = [clean_string(val) for val in mappings[key]]

    modified_files = []

    for csv_file in csv_files:
        try:
            sep = detect_separator(csv_file)
            df = pd.read_csv(csv_file, encoding='ISO-8859-1', sep=sep, quotechar='"')

            modified = False
            for col in df.columns:
                if col in mappings and isinstance(mappings[col], list):
                    df[col] = df[col].apply(lambda x: safe_apply(x, mappings[col]))
                    modified = True

            if modified:
                modified_csv_file = csv_file.replace('.csv', '_modified.csv')
                df.to_csv(modified_csv_file, index=False)
                modified_files.append(modified_csv_file)

        except pd.errors.ParserError as e:
            print(f"Error processing file {csv_file}: {e}")

    return modified_files

def safe_apply(x, mapping):
    try:
        index = int(x) - 1
        if 0 <= index < len(mapping):
            return mapping[index]
        return x
    except (ValueError, TypeError):
        return x

csv_folder_path = 'C:\\Users\\sneji\\Desktop\\webscrapping\\usagers\\'
csv_files = glob.glob(os.path.join(csv_folder_path, '*.csv')) 
json_mappings_file = 'C:\\Users\\sneji\\Desktop\\remplacement_des_données.json'
modified_files = replace_values_in_csv(json_mappings_file, csv_files)

for file in modified_files:
    print(f"File modified: {file}")
