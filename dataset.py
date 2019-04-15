import tensorflow as tf 
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import labels as lb
from tensorflow import keras
import matplotlib.pyplot as plt 
  
def load_data():
    dir = 'training2017CSV/'
    records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.csv') != -1)]
    records.sort() 
    # print(records)
    y, f = lb.get_labels()
    # print(y)
    # print(f)
    # print(type(y))
    # records = ['A00001.csv','A00002.csv']
    # records = records[0:100]
    # print(records)
    x_train = np.array([])
    for r in records:
        test = pd.read_csv(dir + r, index_col=0,nrows=2714)
        # print(test)
        test = test.values.tolist()
        # print(test)
        # test = test[0:2714]
        # test = test[:,1]
        x = np.array([])
        for t in test:
            # print(t[1])
            x = np.append(x,t)
        # print(x)
        # x = x[0:2714]
        x_train = np.append(x_train,x)
        print(dir + r)

    x_train = x_train.reshape(-1, 2714)
    x_train = tf.keras.utils.normalize(x_train, axis = 1)
    # print(x_train)  
    return y,x_train

y,x = load_data()
np.save('X_data.npy', x)
np.save('y_data.npy', y)
# print(y)
# print(x)

# plt.plot(x[0])
# plt.grid(color='r', linestyle='--', linewidth=0.3)
# plt.show()
