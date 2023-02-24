#!/usr/bin/env python
# coding: utf-8

# # Using KNN Algorithm to predict if a person will have diabetes or not

# ### importing libraries

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### loading the dataset

# In[2]:


data = pd.read_csv('diabetes.csv')


# In[3]:


data.head()


# In[4]:


data[0:6]


# #### Replace columns like [Gluscose,BloodPressure,SkinThickness,BMI,Insulin] with Zero as values with mean of respective column

# In[5]:


zero_not_accepted = ['Glucose','BloodPressure','SkinThickness','BMI','Insulin']

for col in zero_not_accepted:
    data[col]= data[col].replace(0,np.NaN)
    mean = int(data[col].mean(skipna=True))
    data[col] = data[col].replace(np.NaN,mean)


# ### extracting independent variables

# In[6]:


X = data.iloc[:,0:8]


# ### extracting dependent variable

# In[7]:


y = data.iloc[:,8]


# ### Explorning data to know relation before processing

# In[8]:


sns.heatmap(data.corr())


# ### splitting dataset into training and testing set

# In[9]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


# In[10]:


X_train


# In[11]:


X_test


# In[12]:


import math
def Euclidian_Distance(test,train):
    distance=0
    for x in range(len(test)):
        distance += pow((test[x] - train[x]), 2)
    return math.sqrt(distance)


# In[13]:


def KNNClassifier(K):
    labels=[]
    num_test = X_test.shape[0]
    num_train = X_train.shape[0]
    for i in range(num_test):
        distance=[] 
        index=[]
        for j in range(num_train):
            distance.append(Euclidian_Distance(X_test.iloc[i],X_train.iloc[j]))
            index.append(j)
        #dis_list = zip(distances, y_train)
        #sorted_list = sorted(dis_list)
        df1=pd.DataFrame({'Dis':distance,'ind':index})
        df1=df1.sort_values('Dis')
        zero_count = 0
        one_count = 0
        for i in df1['ind'].head(K):
            if y_train.iloc[i] == 1:
                one_count += 1
            else:
                zero_count += 1
        if one_count >= zero_count:
            labels.append(1)
        else:
            labels.append(0)
    return labels


# In[14]:


labels=KNNClassifier(3)


# In[ ]:





# In[16]:


y_test = np.array(y_test)
labels=np.array(labels)
labels.shape[0]


# In[18]:


y_test = list(y_test)
tcount = 0
for i in range(len(labels)):
    if labels[i] == y_test[i]:
        tcount += 1
print((tcount / len(y_test))*100,"%")


# In[ ]:




