from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
from numpy import genfromtxt
import time
data = genfromtxt('Amateur.csv', delimiter=',', dtype=int)
dt = tree.DecisionTreeClassifier(max_depth=10, criterion='gini')
dt.fit(data[:,:65], data[:,65])

start=time.time()
pred=dt.predict([[0,0,0,0,0,1,0,0,2,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,2,2,2,2,2,2,2,0,0,2,0,1,2,1,0,0,0,0,2,1,1,1,1,2,0,0,0,1,1,1,1,1,0,0,1,0,2,2,1,2,1]])
end=time.time()
print(end-start)
print(pred)
