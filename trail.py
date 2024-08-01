import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import DenseNet121

# Create a simple model
model = Sequential([
    DenseNet121(weights='imagenet', include_top=False, input_shape=(256, 256, 3)),
    Flatten(),
    Dense(4, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Save the model
model.save('simple_model.h5')

# Load the model
loaded_model = tf.keras.models.load_model('simple_model.h5')
print("Model loaded successfully.")
