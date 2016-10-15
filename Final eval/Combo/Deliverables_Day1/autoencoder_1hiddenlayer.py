import neurolab as nl
import numpy as np
import random

# def train(data):
	
# 	# inp,target = zip(*data)
# 	# inp = list(inp)
# 	# target = list(target)
# 	# print type(inp),type(inp[0]),type(inp[0][1]),inp[0],len(inp)
# 	# print type(target),type(target[0]),type(target[0][1]),len(target),target[0]
# 	# print inp[0]
# 	inp =[]
# 	target=[]
# 	for i in data:
# 		inp.append(data[0])
# 		target.append(data[1])

# 	net = nl.net.newff([[0, 1]] * 384, [8,4])	
	
# 	err = net.train(inp, target, show=1,epochs=65)	#Gradient Descent Backpropagation	
	
# 	net.save('netTrained16_.txt')

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))
    #return 2.0/(1.0+np.exp(-2*z))-1

sigmoid_vec = np.vectorize(sigmoid)

def get_activations(data,index):
	net = nl.load('autoencoder1_16_first_weights.txt')
	a = np.array(data[index])
	#print len(data)
	# for i in range(len(net.layers)):
	weights = []
	biases = []
	biases.append(net.layers[0].np['b'])
	weights.append(net.layers[0].np['w'])
	biases = np.array(biases)
	weights = np.array(weights)
	#print "hello:",weights[0].shape,(np.transpose(np.dot(weights[0], np.transpose(a)))+biases).shape
	#print len(weights),len(weights[0]),len(weights[0][0]),weights[0].shape,np.transpose(a).shape,biases.shape
	a = sigmoid_vec(np.add(np.transpose(np.dot(weights[0], np.transpose(data))),biases))
	#print a.shape,a
	return a.tolist()

def train(inp,target,flag=0):
	#net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5]], [5, 1])
	# print type(inp),type(inp[0]),type(inp[0][0])
	# for i in range(len(inp)):
	# 	if not len(inp[i]) == 384:
	# 		print "no",len(inp.p[i]),i

	# global net
	net = nl.net.newff([[0, 1]] *384, [16, 384])
	print "in train"
	#128 input nodes,16 hidden nodes,26 output nodes
	if flag ==1:net.layers[-1].transf = nl.trans.LogSig()	#if flag is 1,output layer transfer function is Logistic Regression
	else:net.layers[-1].transf = nl.trans.SoftMax()
			#if 0,SoftMax CLassifier is used

	err = net.train(inp, inp, show=1,epochs=2)	#Gradient Descent Backpropagation	

	
	
	net.save('autoencoder1_16_first_weights.txt')

def test(data):

	global net
	net=nl.load('part2_16.txt')
	count = 0
	for i in data:
		#print len(i[0]),type(i[0])
		out = net.sim([i[0]])[0]
		val = i[1]
		#print out, val
		if np.argmax(out) == val.index(max(val)):
			count += 1

	print "accuracy : ",(float(count)/len(data)) * 100


if __name__ == '__main__':

	
	#Creating the required datasets
	'''
	f = {
		"horse":list(map(eval,(open('horse.txt').read().strip().split("\n")))),
		"elephant":list(map(eval,(open('elephant-101.txt').read().strip().split("\n")))),
		"leopards":list(map(eval,(open('leopards-101.txt').read().strip().split("\n")))),
		"motorbikes":list(map(eval,(open('motorbikes-101.txt').read().strip().split("\n"))))
	}

	d = {
		"horse" : [1.,0.,0.,0.],
		"elephant" : [0.,1.,0.,0.],
		"leopards" : [0.,0.,1.,0.],
		"motorbikes" : [0.,0.,0.,1.]
	}

	inp = {}
	for i in f.keys():
		inp[i] = []
		for j in f[i]:
			l = list(map(float,j))
			if len(l)==384:
				t = (l,d[i])
				inp[i].append(t)
			else:
				print "wrong"

	train_data = []
	test_data = []
	for i in inp.keys():
		train_data.extend(inp[i][:int(len(inp[i])*0.7)])
		test_data.extend(inp[i][int(len(inp[i])*0.7):])

	random.shuffle(train_data)

	open('train.txt','w').write(str(train_data))
	open('test.txt','w').write(str(test_data))
	'''

	train_data = eval(open('train.txt').read().strip())
	test_data = eval(open('test.txt').read().strip())
	
	inp,target = zip(*train_data)
	train(inp,target)
	f = open('layer1_activations.txt','w')
	s = str(get_activations(inp,0))
	#print s
	f.write(s)

	inp,target = zip(*test_data)
	#train(inp,target)
	f = open('layer1_test_activations.txt','w')
	s = str(get_activations(inp,0))
	#print s
	f.write(s)
	#test(test_data)
