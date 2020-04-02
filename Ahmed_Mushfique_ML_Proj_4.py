import numpy as np
import matplotlib.pyplot as pl
import random
import keras
from keras.datasets import mnist
import cv2
from math import exp
import time
from sklearn.preprocessing import OneHotEncoder, StandardScaler


(x_train, y_train), (x_test, y_test) = mnist.load_data()
images = x_test

x_train = x_train.reshape(x_train.shape[0], 28*28)



new_col = np.ones(x_train.shape[0]).reshape(x_train.shape[0],1)
x_train =  np.append(x_train,new_col,axis=1)

x_test = x_test.reshape(x_test.shape[0], 28*28)
new_col = np.ones(x_test.shape[0]).reshape(x_test.shape[0],1)
x_test =  np.append(x_test,new_col,axis=1)

encoder = OneHotEncoder()
t = encoder.fit_transform(y_train.reshape((-1,1)))
t = t.toarray()

t_test = encoder.transform(y_test.reshape((-1,1)))
t_test = t_test.toarray() 

sc = StandardScaler()
x_tr = sc.fit_transform(x_train)
x_te = sc.transform(x_test)

w_r = np.random.uniform(size=(encoder.n_values_[0],x_train.shape[1]))

def softmax(w,X):
    
    w_dot_phi = np.matmul(X,w.T)
    exps = np.exp(w_dot_phi)

    sum_res = np.sum(exps,axis=1).reshape((exps.shape[0],1))

    exps = exps/sum_res

    return exps
lr = 0.0001
w = w_r *1*(10**(-5)) 
for i in range(100):
    y = softmax(w,x_tr)
    derivative = np.matmul((y - t).T,x_tr)
#     derivative.shape
    w = w - lr*derivative

y_pred = softmax(w,x_te)
argmax_pred = np.argmax(y_pred,axis=1)
argmax_test = np.argmax(t_test,axis=1)

correct = (argmax_pred == argmax_test).sum()
print(f"The accuracy is {correct*100/argmax_pred.shape[0]}")