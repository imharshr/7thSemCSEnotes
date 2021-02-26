import pandas as pd
from collections import Counter
import math

tennis=pd.readcsv('playtennis.csv')
print('the traing data set is \n\n:',tennis)

def entropy(alist):
	c=Counter(x for x in alist)
	instance=len(alist)
	prob=[x/instance for x in c.values()]
	return sum([-p*math.log(p,2) for p in prob])

def information_gain(d,split,target):
	splitting=d.groupby(split)
	n=len(d.index)
	agent=splitting.agg({target:[entropy, lambda x: len(x)/n]})[target]
	agent.colums=['Entropy','observation']
	newentropy=sum(agent['Entropy']*agent['observation'])
	oldentropy=entropy(d[target])
	return oldentropy-newentropy

def id3(sub,target,a):
	count=Counter(x for x in sub(target))
	if len(count) == 1:
 		return next(iter(count))
    else:
	 	gain=[information_gain(sub,target,attr) for attr in a] 
	 	print("gain:",gain)
	 	maximum=gain.index(max(gain))
	 	best=a[maximum]
	 	print("best",best)
	 	tree={best:{}}
	 	remaining=[i for i in a if i!=best]

	 	for val,subset in sub.groupby(best):
	 		subset=id3(subset,target,remaining)
	 		tree[val][best]=subset
	 	return tree
names = list(tennis.columns)
print("List of Attributes:", names)
names.remove('play')
print("Predicting Attributes:", names)
tree = id3(tennis,'play',names)
print("\n\nThe Resultant Decision Tree is :\n")
print(tree) 