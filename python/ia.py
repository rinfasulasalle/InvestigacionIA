import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Cargar conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar y ajustar la forma de los datos
x_train = x_train / 255.0
x_test = x_test / 255.0

# Construir el modelo de red neuronal
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilar y entrenar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

# Evaluar el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Precisión de la clasificación:', test_acc)
