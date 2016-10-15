import numpy as np
import copy
theta=[]
X=[]
hTheta=0
JBuffer=0
Y=[]
alpha=0.003
def h(exNo):
	return np.matrix(theta) * np.transpose(np.matrix(X[exNo]))

def cost_function():
	errorSum = 0
	for i in range(len(X)):
		errorSum += (h(i)-Y[i])**2
	return (1/(2*len(X))) * errorSum

def compare(t1,t2):
	if([abs(t1[i]-t2[i]) for i in range(len(t1))]<=[0.001 for i in range(len(t1))])
		return False
	return True
	
def descend_and_learn():
	thetaNew = copy.deepcopy(theta)
	while compare(thetaNew,theta):
		theta=copy.deepcopy(thetaNew)
		for j in range(len(X[0])):
			temp = 0
			for i in range(1,len(X)):
				temp += (h(i)-Y[i])
			thetaNew[j] = theta[j] - (alpha/len(x)) * temp
		
def findResult(x):
	return np.matrix(theta) * np.transpose(np.matrix(X[exNo]))