#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import glob

#usagers
# Get a list of all CSV files in the directory
files = glob.glob('DataScienceProject/Data/usagers*.csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()
print(files)
# Loop through each file and append its data to the combined DataFrame
for file in files:
    # Read the first row of the file to infer data types
    dtypes = pd.read_csv(file, nrows=1).dtypes.to_dict()

    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, dtype=dtypes, encoding='UTF-8', sep=';', quotechar='"')
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Now 'combined_data' contains data from all CSV files
combined_data.to_excel('DataScienceProject/combinedData/usagers.xlsx', index=False)
combined_data.head


# In[2]:


#caracteristique
# Get a list of all CSV files in the directory
files = glob.glob('DataScienceProject/Data/carcteristiques*.csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()
print('test')
print(files)
# Loop through each file and append its data to the combined DataFrame
for file in files:
    # Read the first row of the file to infer data types
    dtypes = pd.read_csv(file, nrows=1).dtypes.to_dict()

    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, dtype=dtypes, encoding='UTF-8', sep=';', quotechar='"')
    combined_data = pd.concat([combined_data, df], ignore_index=True)
# Now 'combined_data' contains data from all CSV files
combined_data.to_excel('DataScienceProject/combinedData/carcteristiques.xlsx', index=False)


# In[3]:


#vehicules
# Get a list of all CSV files in the directory
files = glob.glob('DataScienceProject/Data/vehicules*.csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()
print('test')
print(files)
# Loop through each file and append its data to the combined DataFrame
for file in files:
    # Read the first row of the file to infer data types
    dtypes = pd.read_csv(file, nrows=1).dtypes.to_dict()

    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, dtype=dtypes, encoding='UTF-8', sep=';', quotechar='"')
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Now 'combined_data' contains data from all CSV files
combined_data.to_excel('DataScienceProject/combinedData/vehicules.xlsx', index=False)


# In[4]:



#lieux
# Get a list of all CSV files in the directory
files = glob.glob('DataScienceProject/Data/lieux*.csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()
print('test')
print(files)
# Loop through each file and append its data to the combined DataFrame
for file in files:
    # Read the first row of the file to infer data types
    dtypes = pd.read_csv(file, nrows=1).dtypes.to_dict()

    # Read the entire CSV file using inferred data types
    df = pd.read_csv(file, dtype=dtypes, encoding='UTF-8', sep=';', quotechar='"')
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Now 'combined_data' contains data from all CSV files
combined_data.to_excel('DataScienceProject/combinedData/lieux.xlsx', index=False)

