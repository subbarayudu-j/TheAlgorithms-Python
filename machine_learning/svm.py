from sklearn.datasets.samples_generator import make_blobs 
  
# creating datasets X containing n_samples 
# Y containing two classes 
X, Y = make_blobs(n_samples=500, centers=2, 
                  random_state=0, cluster_std=0.40) 
  
# plotting scatters  
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring'); 
plt.show()  
# creating line space between -1 to 3.5 
xfit = np.linspace(-1, 3.5) 

# plotting scatter 
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring') 

# plot a line between the different sets of data 
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]: 
	yfit = m * xfit + b 
	plt.plot(xfit, yfit, '-k') 
	plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none', 
	color='#AAAAAA', alpha=0.4) 

plt.xlim(-1, 3.5); 
plt.show() 
# importing required libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# reading csv file and extracting class column to y. 
x = pd.read_csv("C:\...\cancer.csv") 
a = np.array(x) 
y = a[:,30] # classes having 0 and 1 

# extracting two features 
x = np.column_stack((x.malignant,x.benign)) 
x.shape # 569 samples and 2 features 

print (x),(y) 
# import support vector classifier 
from sklearn.svm import SVC # "Support Vector Classifier" 
clf = SVC(kernel='linear') 

# fitting x samples and y classes 
clf.fit(x, y) 
