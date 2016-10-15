from myhmm_log import MyHmmLog

#--------pre-processing to convert sequences in files into list of sequences---------#

def pre_process(filename):
	f=open(filename)
	s=f.read().strip()
	s=s.split('\n')
	out=[]
	for i in s:
		temp=i.split()
		out.append(temp[6:])
	f.close()
	return out[:2000]

#---------------------create the 3 models---------------------------------------------#

model1 = MyHmmLog('debate_initial.txt')
model2 = MyHmmLog('debate_initial.txt')

# train the 3 models

model1.forward_backward_multi(pre_process('consonant.data'))
model2.forward_backward_multi(pre_process('vowel.data'))

print 'finished training'
#-----------------------test the data--------------------------------------------------#
i=1
count={"single":0,"multi":0,"silent":0,"quality":0}
count={"vowel":0,"consonant":0}
filename = 'letter.data'
f=open(filename)
s=f.read().strip()
test_temp=s.split('\n')[0:800]
out=[]
#print test_temp
d={}
for j in test_temp:
	d['consonant'] = model1.backward(j.split()[6:])
	d['vowel'] = model2.backward(j.split()[6:])
	v = max(d['consonant'],d['vowel'])
	for k in d.items():
		if k[1] == v:
			out.append(1 if k[0]=='vowel' else 0)
open('hmmouttrain.txt','w').write(str(out))
'''
l=pre_process('consonant.data')
for i in l:
	for j in i:
		d = {}
		d['consonant'] = model1.backward(j)
		d['vowel'] = model2.backward(j)
		v = max(d['consonant'],d['vowel'])
		for k in d.items():
			if k[1] == v:
				print(k[0],'\n\n\n\n\n\n')
				count['consonant']+=1
			#count['quality'] = (count['single']*10 + count['multi']* (-10) + count['silent'] * 10)/(count['single']+count['multi']+count['silent'])
			#open("_output.txt","w").write(str(count))
print 'consonant',count['consonant']
count={"vowel":0,"consonant":0}
'''
'''
l=pre_process('vowel.data')
for i in l:
	for j in i:
		d = {}
		d['consonant'] = model1.backward(j)
		d['vowel'] = model2.backward(j)
		v = max(d['consonant'],d['vowel'])
		for k in d.items():
			if k[1] == v:
				print(k[0],'\n\n\n\n\n\n')
				count['vowel']+=1
			
print 'vowel',count['vowel']
'''
'''
---------------------backward for verification -------------------------------------
count={"single":0,"multi":0,"silent":0,"quality":0}
for j in pre_process('c1_test_vq.txt'):
	f = open('c1_out_back_vq.txt','a')
	d = {}
	d['single'] = model1.backward(j)
	d['multi'] = model2.backward(j)
	d['silent'] = model3.backward(j)
	v = max(d['single'],d['multi'],d['silent'])
	for k in d.items():
		if k[1] == v:
			f.write(k[0]+',')
			count[k[0]]+=1
	count['quality'] = (count['single']*10 + count['multi']* (-10) + count['silent'] * 10)/(count['single']+count['multi']+count['silent'])
	open("test_1_b_output.txt","w").write(str(count))'''