import DecisionTree
import pickle
import Node

def main():
    #Insert input file
    """
    IMPORTANT: Change this file path to change training data 
    """
    """
    IMPORTANT: Change this variable too change target attribute 
    """
    tweets = pickle.load(open("inp.pickle"))
    vocab = pickle.load(open("vocab.pickle"))
	
    target = "target"
    data = []
    for i in tweets.keys():
    	l = list(zip(*sorted(tweets[i]["features"].items(), key=lambda x: x[0]))[1])
    	l.extend(tweets[i]["target"])
    	data.append(l)
    attributes = vocab[:]
    attributes.append(target)
    # print data[0], len(data[0])
    # print attributes
    # data.remove(attributes)
	
	
    # Run ID3
    tree = DecisionTree.makeTree(data, attributes, target, 0)
    pickle.dump(tree, open("tree_partial.pickle","wb"))
    tree = pickle.load(open("tree_partial.pickle","rb"))
    print "generated decision tree", str(tree)
    

def test():
	tweets = pickle.load(open("testing.pickle"))
	vocab = pickle.load(open("vocab.pickle"))
	tree = pickle.load(open("tree_partial.pickle"))
	
	target = "target"
	data = []
	for i in tweets.keys():
		l = list(zip(*sorted(tweets[i]["features"].items(), key=lambda x: x[0]))[1])
		l.extend(tweets[i]["target"])
		data.append(l)
	attributes = vocab[:]
	attributes.append(target)
	
	count = 0
	accuracy = 0
	for entry in data:
		count += 1
		tempDict = tree.copy()
		result = ""
		while(isinstance(tempDict, dict)):
			root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
			tempDict = tempDict[tempDict.keys()[0]]
			index = attributes.index(root.value)
			value = entry[index]
			if(value in tempDict.keys()):
				child = Node.Node(value, tempDict[value])
				result = tempDict[value]
				tempDict = tempDict[value]
			else:
				print "can't process input %s" % count
				result = "?"
				break
		if result == entry[-1]:
			accuracy += 1
		print ("entry %s = %s, correct count = %s, target = %s" % (count, result, accuracy, entry[-1]))
	print "ACCURACY= %s%%, %s, total = %s"%(accuracy*100/float(count), accuracy*100/float(len(data)), len(data))
		
    
if __name__ == '__main__':
	main()
	test()