from hmmlearn.hmm import GMMHMM
import numpy as np
gmm=[GMMHMM(n_components=3,n_mix=20,covariance_type='diag') for i in range(4)]
#--------pre-processing to convert sequences in files into list of sequences---------#

def pre_process(fil):
	data = []
	data1=[]
	x=""
	for f in fil:
		x=x+"\n"+open(f).read().strip()
	x.strip()
	data1=(x).split('\n')[1:]
	
	for fi in data1:		
		data.append(list(map(float,fi.split(','))))
	return np.array(data)

def test(fil):
	dat=pre_process([fil])[0]
	print dat,type(dat), type(dat[0])
	temp=[gmm[i].score(dat) for i in range(4)]
	return temp.index(max(temp))

path="./SEE-exam_problem3/Dataset_Generation/MFCC Generator/outputs/mfcc_files/"
import os
fp=[]
for p,subdirs,files in os.walk(path+"Mister"):	
	fp = files
data_path = list(map(lambda x: p+"/"+x,fp))
print data_path

dat=[pre_process(data_path)]
gmm[0].fit(dat)
#x=gmm.score(dat[0][:90])

for p,subdirs,files in os.walk(path+"one_second"):	
	fp = files
data_path = list(map(lambda x: p+"/"+x,fp))
#print data_path

dat=[pre_process(data_path)]
gmm[1].fit(dat)

for p,subdirs,files in os.walk(path+"Others"):	
	fp = files
data_path = list(map(lambda x: p+"/"+x,fp))
print data_path
dat=[pre_process(data_path)]
gmm[2].fit(dat)

for p,subdirs,files in os.walk(path+"thank_you"):	
	fp = files
data_path = list(map(lambda x: p+"/"+x,fp))
print data_path
dat=[pre_process(data_path)]
gmm[3].fit(dat)

k=[]

for p,subdirs,files in os.walk(path+"Mister_test"):	
	fp = files
test_path = list(map(lambda x: p+"/"+x,fp))
k.append([test(t) for t in test_path])

for p,subdirs,files in os.walk(path+"one_second"):	
	fp = files
test_path = list(map(lambda x: p+"/"+x,fp))
k.append([test(t) for t in test_path])

for p,subdirs,files in os.walk(path+"Others_test"):	
	fp = files
test_path = list(map(lambda x: p+"/"+x,fp))
k.append([test(t) for t in test_path])

for p,subdirs,files in os.walk(path+"thank_you_test"):	
	fp = files
test_path = list(map(lambda x: p+"/"+x,fp))
print fp
k.append([test(t) for t in test_path])



print k
count = 0
for i in range(len(k)):
	for j in k[i]:
		if i==j:
			count += 1
			
print 'Accuracy : ',float(count)/(len(k[0])+len(k[1])+len(k[2])+len(k[3]))






