# AIM: Implement Decision Tree Learning Algorithm

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("balance-scale.data", header=None)

print("Dataset Length:", len(data))
print(data.head())

# Split features and target
X = data.iloc[:, 1:5]
Y = data.iloc[:, 0]

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=100
)

# Train Decision Tree using Entropy
model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=3,
    min_samples_leaf=5,
    random_state=100
)
model.fit(X_train, y_train)

# Predict and calculate accuracy
y_pred = model.predict(X_test)

print("Predicted Values:")
print(y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")