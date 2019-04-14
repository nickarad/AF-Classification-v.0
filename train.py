import tensorflow as tf 
import matplotlib.pyplot as plt 
import numpy as np
import createmodel as crm
import dataset as ds
from tensorflow import keras

# ************************************* Prepare Dataset ************************************************
y,x = ds.load_data()
x_train = x[0:800]
y_train = y[0:800]
x_test = x[801:1000]
y_test = y[801:1000]
# ======================================================================================================

# ************************************* Create Model ***************************************************
model = crm.create_model()
model.fit(x_train, y_train, epochs=3)
# -- model accurancy
val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy
# ======================================================================================================

# ************************************* Make predictions ***************************************************
predictions = model.predict(x_test)
print("prediction:", np.argmax(predictions[8]))
print("real value:", y_test[8])
# ======================================================================================================

# ************************************* Save Model ***************************************************
model.summary()
# Save entire model
model.save('my_model.h5')
# ======================================================================================================

