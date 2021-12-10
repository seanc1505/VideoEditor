import keras
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras import layers
scaler = Rescaling(scale=1.0 / 255)

dataset = keras.preprocessing.image_dataset_from_directory('train/', batch_size=64,color_mode='rgb',labels = 'inferred',image_size=(256,
    256))


inputs = keras.Input(shape=(None, None, 3), batch_size = 64 )
x = inputs
# x = Rescaling(scale=1.0 / 255)(inputs)
x = layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu")(x)
x = layers.MaxPooling2D(pool_size=(3, 3))(x)
x = layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu")(x)
x = layers.MaxPooling2D(pool_size=(3, 3))(x)
x = layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu")(x)
# Apply global average pooling to get flat feature vectors
x = layers.GlobalAveragePooling2D()(x)

# Add a dense classifier on top
num_classes = 10
outputs = layers.Dense(num_classes, activation="softmax")(x)

model = keras.Model(inputs=inputs, outputs=outputs)
model.summary()
model.compile(optimizer=keras.optimizers.RMSprop(learning_rate=1e-3),
              loss=keras.losses.CategoricalCrossentropy())

# for data, labels in dataset:
empty_or_full = model.fit_generator(dataset,epochs =3)


    # processed_data = model(data)
    # print(processed_data.shape)
    