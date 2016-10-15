from hmmlearn.hmm import GMMHMM
import numpy as np


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

	d = [np.array(map(np.array,data[i:i+200])) for i in range(0,len(data),200)]
	#print type(d),type(d[0]),type(d[0][0]),type(d[0][0][0]),len(d),len(d[0]),len(d[0][0])
	d =  np.array(d)
	#print type(d),type(d[0]),type(d[0][0]),type(d[0][0][0]),len(d),len(d[0]),len(d[0][0])
	return d

def test(fil):
	for f in fil:
		dat=pre_process([f])
		li=[]
		w = open(f+'.out2','w')
		for i in range(len(dat)):
			temp=[gmm[j].score(dat[i]) for j in range(2)]
			li.append(temp.index(max(temp)))
		w.write(str(li))

if __name__ == '__main__':

	gmm=[GMMHMM(n_components=3,n_mix=1,covariance_type='diag') for i in range(2)]

	path="./mfcc_files/"
	data_path = [path+'single/single_1_mfcc.txt',path+'single/single_3_mfcc.txt',path+'single/single_5_mfcc.txt',path+'single/single_6_mfcc.txt']

	dat=pre_process(data_path)
	gmm[0].fit(dat)

	data_path = [path+'multi/MULTI_1_mfcc.txt',path+'multi/MULTI_2_mfcc.txt',path+'multi/MULTI_3_mfcc.txt',path+'multi/MULTI_4_mfcc.txt']
	dat=pre_process(data_path)
	gmm[1].fit(dat)

	k=[]


	single = [30,34,36]
	multi = [31,30,30,44,39,45,45]

	# test_path = [path+'Testing Dataset/single_7_mfcc.txt',path+'Testing Dataset/single_9_mfcc.txt',path+'Testing Dataset/single_10_mfcc.txt']
	
	# test(test_path)

	# test_path = [path+'Testing Dataset/MULTI_6_mfcc.txt',path+'Testing Dataset/MULTI_7_mfcc.txt',path+'Testing Dataset/MULTI_8_mfcc.txt',path+'Testing Dataset/MULTI_9_mfcc.txt']
	# #k.append([test(t) for t in test_path])

	# test(test_path)

	test_path = [path+'Testing Dataset/host5_mfcc.txt']
	test(test_path)

	# test_path = [path+'Testing Dataset/3_6_mfcc.txt',path+'Testing Dataset/3_7_mfcc.txt',path+'Testing Dataset/3_8_mfcc.txt']
	# k.append([test(t) for t in test_path])

	# print k
	# count = 0
	# for i in range(len(k)):
	# 	for j in k[i]:
	# 		if i==j:
	# 			count += 1
				
	# print 'Accuracy : ',count/7.0*100






