import sys
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder
import cv2
def softmax(w,X):
    
    w_dot_phi = np.matmul(X,w.T)
    exps = np.exp(w_dot_phi)

    sum_res = np.sum(exps,axis=1).reshape((exps.shape[0],1))

    exps = exps/sum_res

    return exps
if __name__ == '__main__':

    weights = np.load('celegans.npy')
    y_test = pd.read_csv('labels.csv').values
    # print(y_test)
    path = sys.argv[1]
    # print(weights.shape)
    # print(y_test.shape)
    # print(path)
    images = os.listdir(path)
    curr_dir = os.getcwd()
    X_test = []
    for i in images:
        X = np.asarray(cv2.imread(curr_dir+'\\'+path+'\\'+i,flags = cv2.IMREAD_GRAYSCALE))
        X = X.reshape((-1,101*101))        
        X = np.hstack([X,np.ones((1,1))])
        # print(X.shape)
        X_test.append(X)
    X_test = np.asarray(X_test)
    X_test = X_test.reshape((len(X_test),101*101 + 1))
    y_pred = softmax(weights,X_test)
    encoder = OneHotEncoder()
    t_test = encoder.fit_transform(y_test.reshape((-1,1)))
    t_test = t_test.toarray() 
    argmax_pred = np.argmax(y_pred,axis=1)
    argmax_test = np.argmax(t_test,axis=1)
    
    # print(argmax_pred)
    # print(argmax_test)
    correct = (argmax_pred == argmax_test).sum()
    print(f"The accuracy is {correct*100/argmax_pred.shape[0]}")