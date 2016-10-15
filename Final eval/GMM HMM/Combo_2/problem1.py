from hmmlearn.hmm import GMMHMM
import numpy as np
gmm=[GMMHMM(n_components=8,n_mix=10,covariance_type='diag') for i in range(3)]
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
	dat=pre_process(fil)[0]
	temp=[gmm[i].fit(dat) for i in range(3)]
	return temp.index(max(temp))

path="./SEE-exam/Dataset_Generation/MFCC Generator/outputs/mfcc_files/"
data_path = [path+'single/single_1_mfcc.txt',path+'single/single_3_mfcc.txt',path+'single/single_5_mfcc.txt',path+'single/single_6_mfcc.txt']

dat=[pre_process(data_path)]
gmm[0].fit(dat)
#x=gmm.score(dat[0][:90])
data_path = [path+'two/TWO_1_mfcc.txt',path+'two/TWO_2_mfcc.txt',path+'two/TWO_3_mfcc.txt',path+'two/TWO_4_mfcc.txt']
dat=[pre_process(data_path)]
gmm[1].fit(dat)

data_path = [path+'three/3_1_mfcc.txt',path+'three/3_2_mfcc.txt',path+'three/3_3_mfcc.txt',path+'three/3_4_mfcc.txt']
dat=[pre_process(data_path)]
gmm[2].fit(dat)

k=[]

test_path = [path+'Testing Dataset/single_7_mfcc.txt',path+'Testing Dataset/single_9_mfcc.txt',path+'Testing Dataset/single_10_mfcc.txt']
k.append([test(t) for t in test_path])

test_path = [path+'Testing Dataset/TWO_6_mfcc.txt',path+'Testing Dataset/TWO_12_mfcc.txt',path+'Testing Dataset/TWO_14_mfcc.txt',path+'Testing Dataset/TWO_13_mfcc.txt']
k.append([test(t) for t in test_path])

test_path = [path+'Testing Dataset/3_6_mfcc.txt',path+'Testing Dataset/3_7_mfcc.txt',path+'Testing Dataset/3_8_mfcc.txt']
k.append([test(t) for t in test_path])

count = 0
for i in range(len(k)):
	for j in k[i]:
		if i==j:
			count += 1
			
print 'Accuracy : ',count*10.






