from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
from numpy import genfromtxt
data = genfromtxt('Advanced.csv', delimiter=',', dtype=int)
#max_depth_range = np.arange(5, 20)
criterion_options = ['gini', 'entropy'] 
parameters = dict(max_depth=[11], criterion=criterion_options)
cv = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42) 
dt = tree.DecisionTreeClassifier()
clf = GridSearchCV(dt, parameters, cv=cv)
clf.fit(data[:,:65], data[:,65])
print(clf.best_score_)
print()
print(clf.best_params_)
tree.export_graphviz(clf, out_file='Advanced.dot') 
