import time
import  numpy as np
from numpy import array,uint8
def convertInput(w,inp):
	l=[]
	#print inp
	for i in range(len(inp)):
		inp[i]=np.uint8(inp[i])
	#print inp,len(inp)
	for i in range(0,len(inp),w):
		l.append(inp[i:i+w])
		#print inp[i:i+w]
	y=np.array(l)
	'''print l
	print type(y)
	print type(y[0])
	print type(y[0][0])
	#time.sleep(3)'''
	return np.array(l)

def visualizePreprocess(filename='letter.data'):
	f=open(filename)
	s=f.read().strip()
	s=s.split('\n')
	out={}
	for i in s:
		temp=i.split()
		#print i,'\n',temp
		#time.sleep(3)
		out[temp[1]]={}
	for i in s:
		temp=i.split()
		out[temp[1]][temp[3]]=convertInput(8,temp[6:])
	f.close()
	f=open('out.txt','w')
	f.write(str(out))
	f.close()
	return out
def loadData(filename='out.txt'):
	return eval(open(filename).read())
	
def visualize(img):
	import matplotlib
	import matplotlib.pyplot as plt
	plt.imshow(img,cmap='gray')
	plt.show()
	
def neuralPreprocess(outputFileName='neuralOut.txt',filename='letter.data'):
	f=open(filename)
	s=f.read().strip()
	s=s.split('\n')
	out={}
	for i in s:
		temp=i.split()
		out[temp[1]]={}
	for i in s:
		temp=i.split()
		out[temp[1]][int(temp[0])]=list(map(float,temp[6:]))
	f.close()
	'''f=open(outputFileName,'w')
	f.write(str(out))
	f.close()'''
	return out

