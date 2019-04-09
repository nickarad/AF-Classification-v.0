import tensorflow as tf 
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import labels as lb

# def load_data():
dir = 'training2017CSV/'
records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.csv') != -1)]
records.sort() 
# print(records)
y, f = lb.get_labels()
# print(y)
# print(f)
print(type(y))
records = ['A00001.csv','A00002.csv']
print(records)

x_train = np.array([])


for r in records:
    test = pd.read_csv(dir + r)
    test = test.values.tolist()
    # test = test[:,1]
    x = np.array([])
    for t in test:
        # print(t[1])
        x = np.append(x,t[1])
    # print(x)
    x = x[0:2714]
    x_train = np.append(x_train,x)

x_train = x_train.reshape(-1, 2714)
print(x_train)    

