#!/usr/bin/python3
import time
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#loading iris data
iris=load_iris()
# print flowers name
fl_name=iris.target_names

#print features of iris
fl_features=iris.feature_names

#loading flowers features data
fl_features_data=iris.data

#print(fl_features_data)

#loading flower name data
fl_real_data=iris.target

plt.xlabel("Setosa")
plt.ylabel("versicolor")
plt.title("IRIS flowers")
x1=fl_features_data[0:50]
y1=fl_features_data[50:100]
z1=fl_features_data[100:]
plt.scatter(x1,y1,label="setso",marker='*',c='r')
plt.scatter(x1,z1,label="setso",marker='x',c='b')
plt.scatter(y1,z1,label="setso",marker='o',c='g')
plt.legend()
plt.show()


