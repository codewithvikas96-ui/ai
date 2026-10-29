# AIM: Implement Decision Tree Learning Algorithm

# REQUIREMENTS:
# 1. Files: balance-scale.data and balance-scale.names
# 2. Install required modules:
#    python -m pip install pandas
#    python -m pip install scipy
#    python -m pip install scikit-learn
#    python -m pip install numpy

import numpy as np
import pandas as pd
import sklearn as sk

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# Function to import the dataset
def importdata():
    balance_data = pd.read_csv("balance-scale.data")

    # Print dataset length
    print("Dataset Length:", len(balance_data))

    # Print first five observations
    print("Dataset:")
    print(balance_data.head())

    return balance_data


# Function to split the dataset
def splitdataset(balance_data):
    # Separate input features and target variable
    X = balance_data.values[:, 1:5]
    Y = balance_data.values[:, 0]

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y,
        test_size=0.3,
        random_state=100
    )

    return X, Y, X_train, X_test, y_train, y_test


# Function to train the model using entropy
def train_using_entropy(X_train, X_test, y_train, y_test):
    # Create decision tree classifier using entropy
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy",
        random_state=100,
        max_depth=3,
        min_samples_leaf=5
    )

    # Train the model
    clf_entropy.fit(X_train, y_train)

    return clf_entropy


# Function to predict test data
def prediction(X_test, clf_object):
    y_pred = clf_object.predict(X_test)

    print("Predicted Values:")
    print(y_pred)

    return y_pred


# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")


# Main function
def main():
    data = importdata()

    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)

    clf_entropy = train_using_entropy(
        X_train, X_test, y_train, y_test
    )

    print("Results using Entropy:")

    y_pred_entropy = prediction(X_test, clf_entropy)

    cal_accuracy(y_test, y_pred_entropy)


main()