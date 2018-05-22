#!/usr/bin/python3

import sklearn 
from sklearn import tree
import sys
inn=sys.argv

#apple and orange ---texture,weight
#smooth==0 and bumpy==1


w=int(inn[1])
out=int(inn[2])
features=[[110,0],[120,0],[130,1],[140,1]]
output=["Apple","Apple","Orange","Orange"]
#row loading decision tree classifier()

algo=tree.DecisionTreeClassifier()

trained=algo.fit(features,output)
#passing the variable
#testing trained model of Q&A


resoutput=trained.predict([[w,out]])

print(resoutput)


