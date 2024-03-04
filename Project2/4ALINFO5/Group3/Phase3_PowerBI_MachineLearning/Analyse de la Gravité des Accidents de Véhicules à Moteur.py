#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[5]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
data = pd.read_excel('C:/Users/ssghaier/Documents/.machine learning/Motor_Vehicle_Collisions_-_Crashes_20240131_cleaned.xlsx')

# Define features and create binary target variable
X = data[['BOROUGH', 'ZIP CODE', 'CRASH TIME', 'CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1']]
data['INJURY_OR_FATALITY'] = (data['NUMBER OF PERSONS INJURED'] > 0) | (data['NUMBER OF PERSONS KILLED'] > 0)
y = data['INJURY_OR_FATALITY']

# Preprocess 'CRASH TIME' column
X['CRASH HOUR'] = X['CRASH TIME'].apply(lambda x: int(str(x)[:2]) if pd.notnull(x) else x)
X.drop(columns=['CRASH TIME'], inplace=True)

# Handle categorical variables
X = pd.get_dummies(X, columns=['BOROUGH', 'ZIP CODE', 'CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression classifier
log_reg = LogisticRegression(max_iter=1000, random_state=42)

# Train the classifier
log_reg.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = log_reg.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# In[ ]:




