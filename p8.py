import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

data = pd.read_csv(url, header=None)

X = data.iloc[:, 0:8]
Y = data.iloc[:, 8]

model = AdaBoostClassifier(n_estimators=30, random_state=7)

result = cross_val_score(model, X, Y)

print(result.mean())