import tensorflow as tf


def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(2048, activation=tf.nn.relu, input_shape=(2714,)),
        tf.keras.layers.Dense(2048, activation=tf.nn.relu),
        tf.keras.layers.Dense(4, activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])
    return model
