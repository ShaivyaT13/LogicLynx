import pandas as pd
import numpy as np
import warnings
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
warnings.filterwarnings('ignore')

df= pd.read_csv('MergeFileCrop.csv')
print(df)
               
X = df[['temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

RF = RandomForestClassifier(n_estimators=100, random_state=0)
RF= RF.fit(X_train,y_train)

predicted_values = RF.predict(X_test)
accuracy= accuracy_score(y_test, predicted_values)
print("RF's Accuracy is: ", accuracy)

from sklearn.model_selection import cross_val_score
cross_val_score(RF, X, y, cv=10)
print(cross_val_score(RF, X, y, cv=10))

import pickle
pickle.dump(RF, open('RandomForest.pkl', 'wb'))
model=pickle.load(open('RandomForest.pkl', 'rb'))
