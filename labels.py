import pandas as pd
import numpy as np

def get_labels():
    dir = 'training2017/'
    label = pd.read_csv(dir + 'REFERENCE.csv')
    label = label.values.tolist() # --> convert test dataframe to list
    # print(label)
    classes = ['A','N','O','~']
    y = np.array([])
    file = []
    for t in label:
            # print(t[1])
            position = classes.index(t[1])
            y = np.append(y,position)
            # y = np.append(y,t[1])
            file.append(t[0])
        # print(x)
    y = y.astype(int)
    return y,file
