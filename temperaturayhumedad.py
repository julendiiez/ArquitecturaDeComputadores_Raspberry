import Adafruit_DHT

# Configura el tipo de sensor y el pin GPIO al que está conectado
sensor = Adafruit_DHT.DHT11
pin = 4  # El pin GPIO al que está conectado el sensor (cambia según tu configuración)

while True:
    # Intenta obtener la lectura del sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Si la lectura fue exitosa, muestra los valores
    if humidity is not None and temperature is not None:
        print('Temperatura={0:0.1f}°C Humedad={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Error al obtener la lectura del sensor. Inténtalo de nuevo.')

