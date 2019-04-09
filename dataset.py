import tensorflow as tf 
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import labels as lb

# def load_data():
dir = 'training2017CSV/'
records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.csv') != -1)]
# print(records)
y, f = lb.get_labels()
print(y)
# print(f)
print(y[0])