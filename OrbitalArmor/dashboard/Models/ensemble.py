from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,  OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import metrics, preprocessing

import pandas as pd
import numpy as np
file = './dataset_sdn.csv'
data = pd.read_csv(file)
data = data.dropna()

y = data.label

categorical_features = ['src', 'dst', 'Protocol']
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot", one_hot, categorical_features)],remainder = "passthrough")
data = data.drop(['label'], axis=1)
transformed_data = transformer.fit_transform(data)

print(data.shape)

X = preprocessing.StandardScaler().fit(transformed_data).transform(transformed_data)
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.2)

clf1 =LogisticRegression(C=0.03, solver='saga')
clf2 =  GaussianNB()
clf3 = KNeighborsClassifier(n_neighbors=3, metric='manhattan',weights='distance')
clf4 = DecisionTreeClassifier(criterion='gini',max_depth=8,max_leaf_nodes=11)
M = VotingClassifier(
        estimators = [('lr', clf1), ('gnb', clf2 ), ('knn', clf3), ('dt', clf4)],
        voting='hard',weights=[2,3,1,5])

clf1.fit(X_train, y_train)
clf2.fit(X_train, y_train)
clf3.fit(X_train, y_train)
clf4.fit(X_train, y_train)
M.fit(X_train, y_train)

clf1.predict(X_test)
clf2.predict(X_test)
clf3.predict(X_test)
clf4.predict(X_test)
M.predict(X_test)

lrScore = clf1.score(X_test, y_test)
gnbScore = clf2.score(X_test, y_test)
knnScore = clf3.score(X_test, y_test)
dtScore = clf4.score(X_test, y_test)
MScore = M.score(X_test, y_test)

print(lrScore, gnbScore, knnScore, dtScore)

print ('overrall score is ')
print(MScore)

