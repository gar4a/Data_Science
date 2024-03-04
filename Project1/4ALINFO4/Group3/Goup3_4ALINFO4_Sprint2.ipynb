from bs4 import BeautifulSoup
import pandas as pd
from google.colab import drive
import requests

# Mount Google Drive
drive.mount('/content/gdrive')

# Path to the CSV file on Google Drive
csv_file_path = '/content/gdrive/My Drive/Data_Science_Project_2024/Group3_job_offers_dataset.csv'

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Display basic information about the dataset before cleaning
print("Dataset Information (Before Cleaning):")
print(df.info())

# Summary statistics before cleaning
print("\nSummary Statistics (Before Cleaning):")
print(df.describe())

# Check for missing values before cleaning
print("\nMissing Values (Before Cleaning):")
print(df.isnull().sum())

# Data cleaning
# Drop rows with missing values
df.dropna(inplace=True)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Display basic information about the cleaned dataset
print("\nDataset Information (After Cleaning):")
print(df.info())

# Summary statistics of the cleaned dataset
print("\nSummary Statistics (After Cleaning):")
print(df.describe())

# Check for missing values in the cleaned dataset
print("\nMissing Values in Cleaned Dataset:")
print(df.isnull().sum())

# Data visualization using cleaned data
# Example: Distribution of SalaryRange after cleaning
import seaborn as sns
import matplotlib.pyplot as plt

# Statistical analysis
# Summary statistics for numerical variables
print("Summary Statistics for Numerical Variables:")
print(df.describe())

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Visualizations
# Pairplot for numerical variables
sns.pairplot(df, diag_kind='kde')
plt.suptitle("Pairplot for Numerical Variables")
plt.show()

# Boxplot for SalaryRange by Department
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x="Department", y="SalaryRange")
plt.title("Boxplot of SalaryRange by Department")
plt.xticks(rotation=45)
plt.show()

# Bar plot for Telecommuting
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Telecommuting")
plt.title("Count plot of Telecommuting")
plt.xlabel("Telecommuting")
plt.ylabel("Frequency")
plt.show()
