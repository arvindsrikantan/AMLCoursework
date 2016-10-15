# Speaker detection

from hmmlearn.hmm import GMMHMM
import numpy as np
import os
import pickle

#--------pre-processing to convert sequences in files into list of sequences---------#

def pre_process(fil):
	data = []
	data1=[]
	x=""
	for f in fil:
		if(not f==None):
			x=x+"\n"+open(f).read().strip()
	x.strip()
	data1=(x).split('\n')[1:]
	
	for fi in data1:		
		data.append(list(map(float,fi.split(','))))

	d = [np.array(map(np.array,data[i:i+200])) for i in range(0,len(data),200)]
	d =  np.array(d)
	
	return d

def test(fil):
	for f in fil:
		if(not f==None):
			dat=pre_process([f])
			li=[]
			w = open(f+'.out3_2','w')
			for i in range(len(dat)):
				temp=[gmm[j].score(dat[i]) for j in range(3)]
				li.append(temp.index(max(temp)))
			w.write(str(li))

if __name__ == '__main__':

	gmm=[GMMHMM(n_components=3,n_mix=1,covariance_type='diag') for i in range(3)]

	path="./mfcc_files/"

	for p,subdirs,files in os.walk(path+"arnab"):    
		fp = files
	data_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))

	dat=pre_process(data_path)
	gmm[0].fit(dat)

	for p,subdirs,files in os.walk(path+"kejriwal"):    
		fp = files
	data_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))
	dat=pre_process(data_path)
	gmm[1].fit(dat)

	for p,subdirs,files in os.walk(path+"ravish"):    
		fp = files
	data_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))
	dat=pre_process(data_path)
	gmm[2].fit(dat)

	k=[]

	pickle.dump(gmm[0],open('arnab.pickle','w'))
	pickle.dump(gmm[1],open('arvind.pickle','w'))
	pickle.dump(gmm[2],open('ravish.pickle','w'))

	path="./mfcc_files/Testing/"

	for p,subdirs,files in os.walk(path+"shouting"):    
		fp = files
	test_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))

	test(test_path)	

	# for p,subdirs,files in os.walk(path+"multiple"):    
	# 	fp = files
	# test_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))
	# test(test_path)

	# test_path = [path+'arnab_7_mfcc.txt',path+'arvind_9_mfcc.txt',path+'host5_mfcc.txt']

	# test(test_path)







