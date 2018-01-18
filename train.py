
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model.perceptron import Perceptron
from sklearn.preprocessing import scale
import os
import matplotlib.pyplot as plt

from random import shuffle

def movingaverage(values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma


training_data = []
file_name = 'training_data.npy'
if os.path.isfile(file_name):
	print('File exists, loading previous data!')
	training_data = list(np.load(file_name))


training_data = shuffle(training_data)
print(training_data)
X = np.array([i[0] for i in training_data])
#X = scale( X, axis=0, with_mean=True, with_std=True, copy=True )

X_fin = list()
for i in range(0,300):
	std = np.std(X[i])
	mean = np.mean(X[i])
	X_fin.append([std,mean])

print(X_fin[0:10])
Y = np.array([int(i[1]) for i in training_data])
'''
X_full = np.concatenate(X,axis=0)
#print(X_full.shape)
y = np.arange(1000)
ym = np.arange(998)
print(X_full[0:1000].shape,y.shape)


plt.subplot(3,2,1)
plt.plot(y,X_full[0:1000],color='#D62728', linewidth=1, label='Wood')
plt.plot(ym,scale( movingaverage(X_full[0:1000],3), axis=0, with_mean=True, with_std=True, copy=True ),color='#2C9F2C', linewidth=1, label='Wood')

plt.subplot(3,2,2)
#plt.plot(y,X_full[1000:2000],color='#2C9F2C', linewidth=1, label='Laptop')
plt.plot(ym,scale( movingaverage(X_full[1000:2000],3), axis=0, with_mean=True, with_std=True, copy=True ),color='#D62728', linewidth=1, label='Wood')

plt.subplot(3,2,3)
#plt.plot(y,X_full[2000:3000],color='#FD7F23', linewidth=1, label='Book')
plt.plot(ym,scale(movingaverage(X_full[2000:3000],3), axis=0, with_mean=True, with_std=True, copy=True ),color='#D62728', linewidth=1, label='Wood')

plt.show()
#print(X)
#print(X[0],Y[0])
#print(X[100],Y[100])
#print(X[200],Y[200])
#print(X.shape)
#print(Y.shape)
'''


#clf = SGDClassifier(loss="hinge", penalty="l2")
clf = Perceptron()
print(np.array(X_fin).shape,X.shape,Y.shape)
clf.fit(X_fin, Y)


wrong = 0
for i in range(0,100):
	std = np.std(X[i])
	mean = np.mean(X[i])
	lar = np.max(X[i])
	if(clf.predict([[std,mean]]) != Y[i]):
		wrong +=1

print(wrong, ((300-wrong)/300) *100)