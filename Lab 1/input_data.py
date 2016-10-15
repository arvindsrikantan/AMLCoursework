import csv
import pickle
import re
import HTMLParser
from nltk.corpus import stopwords


def cleanTweets(inp):
	'''
		inp is a tweet
	'''
	# 1. Tokenize
	# 2. Remove stop words
	# 3. Maybe use the CMU cleaner
	
	html_parser = HTMLParser.HTMLParser()
	tw = html_parser.unescape(inp.strip())
	tw = tw.decode("utf8").encode('ascii','ignore') 									# Decoding string
	tw,subs = re.subn(r'RT @[a-zA-Z]*:\b|[a-zA-Z]*:\b|rt','',tw) 						# Removing retweets
	tw,subs = re.subn(r"'",'',tw) 														# Removing apostrophe due to string warping
	tw,subs = re.subn(r'@[a-zA-Z0-9_]*\b','',tw) 									# Removing screen names
	tw,subs = re.subn(r'#[a-zA-Z0-9_]*\b','',tw) 								# Removing hashtags
	tw,subs = re.subn(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|\
		(?:%[0-9a-fA-F][0-9a-fA-F]))+|http$','',tw) 										# Removing URLs
	tw,subs = re.subn(r'(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]\
		|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)','',tw)			# Removing emoticons
	tw,subs = re.subn(r"""[-_/#"'|\`:%]|[.?!]{2,}""",'',tw) 							# Removing unnecessary punctuation
	tw,subs = re.subn(r'[-+]?[\d]+(.[\d]+(e[\d]+))?','',tw)
	tweet = ' '.join(tw.strip().split()).lower() 
	
	stop = stopwords.words('english')
	# print len(stop)
	return [i for i in tweet.split(' ') if i not in stop]

rows = csv.reader(open("testing.csv", 'rb'))
tweets = {}
for row in rows:
	tweets[row[0]] = {}
	tweets[row[0]]['target'] = row[1]
	
temp = []
# for i in tweets.keys():
	# temp.extend(cleanTweets(i))
# vocab = list(set(temp))
vocab = pickle.load(open("vocab.pickle"))
print len(vocab), len(temp)#, vocab, temp[0]

for tweet in tweets.keys():
	tweets[tweet]["features"] = {}
	for j in vocab:
		tweets[tweet]["features"][j] = tweet.count(j) if j in tweet else 0
# vocab.sort()		
pickle.dump(tweets, open("testing.pickle", "w"))
# pickle.dump(vocab, open("vocab.pickle", "w"))
# pickle.load(open("inp.pickle")) - to read
