import tensorflow as tf


def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(4096,kernel_initializer='normal', activation=tf.nn.relu, input_shape=(2714,)),
        # tf.keras.layers.Dense(4096,kernel_initializer='normal', activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(2048,kernel_initializer='normal', activation=tf.nn.relu),
        # tf.keras.layers.Dense(2048,kernel_initializer='normal', activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1024,kernel_initializer='normal', activation=tf.nn.relu),
        # tf.keras.layers.Dense(1024,kernel_initializer='normal', activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(512,kernel_initializer='normal', activation=tf.nn.relu),
        # tf.keras.layers.Dense(512,kernel_initializer='normal', activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(256,kernel_initializer='normal', activation=tf.nn.relu),
        # tf.keras.layers.Dense(256,kernel_initializer='normal', activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(128,kernel_initializer='normal', activation=tf.nn.relu),
        # tf.keras.layers.Dense(128,kernel_initializer='normal', activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(64,kernel_initializer='normal', activation=tf.nn.relu),
        # tf.keras.layers.Dense(64,kernel_initializer='normal', activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(4,kernel_initializer='normal', activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])
    return model
