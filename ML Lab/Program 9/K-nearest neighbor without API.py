#!/usr/bin/env python
# coding: utf-8

# The kNN task can be broken down into writing 3 primary functions:
# 1.	Calculate the distance between any two points
# 2.	Find the nearest neighbours based	on these pair wise distances
# 3.	Majority vote on a class labels based on the nearest neighbour list

# In[7]:


#Loading iris dataset and defining the our target and data
from sklearn import datasets
import pandas as pd

iris=datasets.load_iris()
X = pd.DataFrame(iris.data) 
X.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']


# # Train the Model

# In[9]:


# splitting the data into training and test sets (80:20)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)


# In[10]:


#shape of train and test objects
print(X_train.shape)
print(X_test.shape)


# In[11]:


# shape of new y objects
print(y_train.shape)
print(y_test.shape)


# In[12]:


#import the KNeighborsClassifier class from sklearn
from sklearn.neighbors import KNeighborsClassifier

#import metrics model to check the accuracy 
from sklearn import metrics
#Try running from k=1 through 25 and record testing accuracy
k_range = range(1,26)
scores = {}
scores_list = []
for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train,y_train)
        y_pred=knn.predict(X_test)
        scores[k] = metrics.accuracy_score(y_test,y_pred)
        scores_list.append(metrics.accuracy_score(y_test,y_pred))


# In[13]:


#Testing accuracy for each value of K
scores


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

#plot the relationship between K and the testing accuracy
plt.plot(k_range,scores_list)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')


# K values with 3 to 19 has the same accuracy which is 96.66, so we can use any one value from that, i choose K as 5 and train the model with full training data

# In[15]:


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)


# In[17]:


#0 = setosa, 1=versicolor, 2=virginica
classes = {0:'setosa',1:'versicolor',2:'virginica'}

#Making prediction on some unseen data 
#predict for the below two random observations
x_new = [[3,4,5,2],
         [5,4,2,2]]
y_predict = knn.predict(x_new)

print(classes[y_predict[0]])
print(classes[y_predict[1]])


# In[ ]:




