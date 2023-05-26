#import cv2
from flask import Flask, render_template, Response
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import requests
from bs4 import BeautifulSoup

GPIO.setmode(GPIO.BCM)
analog_pin = 18
sensor= Adafruit_DHT.DHT11
pin = 16
led_pin = 5




app = Flask(__name__)

@app.route('/temperaturayhumedad')
def sensores():
    # Lectura de temperatura y humedad desde el sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    GPIO.setup(analog_pin, GPIO.IN)
    time.sleep(0.1)
    sensor_value = GPIO.input(analog_pin)
    # Conversión del valor analógico a porcentaje de humedad (0-100%)
    humidity2 = (sensor_value / 1023.0) * 100
    if humidity is not None and temperature is not None:
        # Renderizar la plantilla HTML con los valores de temperatura y humedad
        return render_template('temp.html', temperature=temperature, humidity=humidity,humidity2=humidity2)
    else:
         # En caso de fallo al leer el sensor, mostrar un mensaje de error
         return 'Error al leer el sensor DHT11'

"""
# Capturar video desde la cámara USB
def capture_camera():
    camera = cv2.VideoCapture(0)  # 0 indica el primer dispositivo de video (cámara)
    GPIO.output(led_pin, GPIO.HIGH)

    while True:
        # Leer el cuadro de video
        success, frame = camera.read()
        if not success:
            break
        else:
            # Codificar el cuadro de video en formato de imagen JPEG
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()

            # Generar un generador de secuencia de bytes para el cuadro de video
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    camera.release()
"""

"""
@app.route('/video_feed')
def video_feed():
    return Response(capture_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')
"""


@app.route('/')
def inicio():
    GPIO.setup(led_pin, GPIO.OUT) #Establecer el puerto con el LED
    GPIO.output(led_pin, GPIO.HIGH)
    # Obtener el contenido HTML de la página
    url = "https://www.euskalmet.euskadi.eus/el-tiempo/donostia/"
    response = requests.get(url)
    html_content = response.content

    # Crear objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(html_content, 'html.parser')


    # Encontrar el elemento tab-panel panel-today
    tab_panel_today = soup.find('div', class_='tab-panel panel-today active')

    # Encontrar el elemento div con la clase temp-content dentro de tab-panel panel-tomorrow
    temp_content_div = tab_panel_today.find('div', class_='temp-content')
    info_content_div=tab_panel_today.find('div', class_='info-icon-content')
    # Obtener todo el contenido dentro de temp-content
    contenido_hoy = temp_content_div.text.strip()
    contenido1_hoy = info_content_div.text.strip()


    # Encontrar el elemento tab-panel panel-tomorrow
    tab_panel_tomorrow = soup.find('div', class_='tab-panel panel-tomorrow')

    # Encontrar el elemento div con la clase temp-content dentro de tab-panel panel-tomorrow
    temp_content_div1 = tab_panel_tomorrow.find('div', class_='temp-content')
    info_content_div1=tab_panel_tomorrow.find('div', class_='info-icon-content')
    # Obtener todo el contenido dentro de temp-content
    contenido_mañana = temp_content_div1.text.strip()
    contenido1_mañana = info_content_div1.text.strip()



    # Encontrar el elemento tab-panel panel-after-tomorrow
    tab_panel_aftertomorrow = soup.find('div', class_='tab-panel panel-after-tomorrow')

    # Encontrar el elemento div con la clase temp-content dentro de tab-panel panel-tomorrow
    temp_content_div2 = tab_panel_aftertomorrow.find('div', class_='temp-content')
    info_content_div2=tab_panel_aftertomorrow.find('div', class_='info-icon-content')
    # Obtener todo el contenido dentro de temp-content
    contenido_pasadomañana = temp_content_div2.text.strip()
    contenido1_pasadomañana = info_content_div2.text.strip()
    return render_template('inicio.html',contenido_hoy=contenido_hoy, contenido1_hoy=contenido1_hoy, contenido_mañana=contenido_mañana, contenido1_mañana=contenido1_mañana, contenido_pasadomañana=contenido_pasadomañana, contenido1_pasadomañana=contenido1_pasadomañana)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
