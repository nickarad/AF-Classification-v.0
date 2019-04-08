import tensorflow as tf 

# Creates a dataset that reads all of the records from two CSV files, each with
# eight float columns

filenames = ["samples.csv", "samples1.csv"]
print(filenames)

record_defaults = [[0.1]] * 2 
dataset = tf.data.experimental.CsvDataset(filenames, record_defaults)

print(dataset)