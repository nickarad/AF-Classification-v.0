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
# y, f = lb.get_labels()
# print(y)
# print(f)
# print(type(y))

counter = 0
minim = 9000
for r in records:
    test = pd.read_csv(dir + r)
    test = test.values.tolist()
    if len(test)<3000:
        counter = counter + 1
        if len(test) < minim:
            minim =len(test)
            print(minim)
        print(dir + r)
        

print(counter)
print(minim)