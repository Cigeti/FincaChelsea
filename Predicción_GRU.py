import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import Sequential
from keras.layers import GRU, Dense, Dropout
from keras.optimizers import Adam
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('/Users/reymondrojas/Documents/AnalisisDatos/Chelsea/NodoAmbiente/humedad.csv', delimiter=';')
data['DateTime'] = pd.to_datetime(data['DateTime'])
data['Humedad %'] = data['Humedad %'].str.replace(',', '.').astype(float)

# Normalizar los datos
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data['Humedad %'].values.reshape(-1, 1))

# Función para crear secuencias
def create_sequences(data, sequence_length):
    sequences = []
    for i in range(len(data) - sequence_length):
        sequences.append(data[i:i + sequence_length])
    return np.array(sequences)

# Longitud de la secuencia
sequence_length = 30
# Crear secuencias
sequences = create_sequences(data_scaled, sequence_length)

# Preparar entradas y salidas
X = sequences[:, :-1]
y = sequences[:, -1]

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construir el modelo GRU
model = Sequential()
model.add(GRU(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(GRU(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Compilar el modelo
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=1)

# Hacer predicciones
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)
y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))

# Visualizar los resultados
plt.figure(figsize=(12, 6))
plt.plot(y_test_scaled, label='Valor Real')
plt.plot(predictions, label='Predicción', color='red')
plt.title('Predicción de Humedad')
plt.xlabel('Tiempo')
plt.ylabel('Humedad')
plt.legend()
plt.show()


####Predecir horas futuras####

def predict_next_hours(model, last_sequence, n_hours):
    future_predictions = []
    current_sequence = last_sequence.reshape(1, -1, 1)

    for _ in range(n_hours):
        # Obtener la próxima predicción
        next_prediction = model.predict(current_sequence)

        # Redimensionar next_prediction para que coincida con la forma de current_sequence
        next_prediction_reshaped = next_prediction.reshape(1, 1, -1)

        # Actualizar la secuencia con la predicción
        current_sequence = np.append(current_sequence[:, 1:, :], next_prediction_reshaped, axis=1)

        # Añadir la predicción a la lista
        future_predictions.append(next_prediction.ravel()[0])

    return np.array(future_predictions)

# Preparar la última secuencia de los datos
last_sequence = data_scaled[-sequence_length:]

# Predicción para las próximas 'n' horas
n_future_hours = 72  # Número de horas a predecir
future_predictions = predict_next_hours(model, last_sequence, n_future_hours)

# Deshacer la normalización para obtener valores reales
future_predictions_real = scaler.inverse_transform(future_predictions.reshape(-1, 1))

# Visualizar las predicciones futuras
future_hours = pd.date_range(start=data['DateTime'].iloc[-1] + pd.Timedelta(hours=1), periods=n_future_hours, freq='H')
plt.figure(figsize=(12, 6))
plt.plot(future_hours, future_predictions_real, label='Predicciones Futuras', color='green')
plt.title(f'Predicciones de Humedad para las Próximas {n_future_hours} Horas')
plt.xlabel('Fecha y Hora')
plt.ylabel('Humedad')
plt.xticks(rotation=45)
plt.legend()
plt.show()

