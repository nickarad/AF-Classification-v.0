import tensorflow as tf 
import matplotlib.pyplot as plt 
import numpy as np
import createmodel as crm
# import dataset as ds
from tensorflow import keras

# ************************************* Prepare Dataset ************************************************
x = np.load('x_data.npy')
y = np.load('y_data.npy')
print(x)
print(y)
print(x.shape)
# y,x = ds.load_data()
train_num = 6000
test_num = 1000
x_train = x[0:train_num -1]
y_train = y[0:train_num -1]
x_test = x[train_num:train_num + test_num -1]
y_test = y[train_num:train_num + test_num -1]
# ======================================================================================================

# ************************************* Create Model ***************************************************
model = crm.create_model()
model.fit(x_train, y_train, epochs=20)
# -- model accurancy
val_loss, val_acc = model.evaluate(x_test, y_test,batch_size=256,verbose=2, shuffle=True, callbacks=[checkpointer])  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy
# ======================================================================================================

# ************************************* Make predictions ***************************************************
predictions = model.predict(x_test)
test = 2
print("prediction:", np.argmax(predictions[test]))
print("real value:", y_test[test])
# ======================================================================================================

# ************************************* Save Model ***************************************************
# model.summary()
# Save entire model
model.save('my_model.h5')
# ======================================================================================================

