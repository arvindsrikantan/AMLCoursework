import numpy as np
import math
f=open('Mobile_Data.csv','r')
s=f.read().split('\n')
dataset=[]

y=[]
for i in range(1,len(s)-1):
        #print(s[i].split(",")[2:8])
        dataset.append(list(map(float,s[i].split(",")[2:8])))
	dataset[i-1].insert(0,1.0)
        y.append(float(s[i].split(",")[8]))
 
f.close()
num=65
#print dataset
X=dataset[:num]

#print X
Xtest=dataset[num:]
X_dagger=np.linalg.pinv(np.matrix(X))
y_train=y[:num]
y_test=y[num:]

w=X_dagger*np.transpose(np.matrix(y_train))
print w

ytest=np.matrix(Xtest)*w
print ytest
print y_test
error=np.divide(np.multiply(ytest-np.matrix(y_test),(ytest-np.matrix(y_test))),y_test).mean()
print math.sqrt(error)

