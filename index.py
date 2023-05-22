import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

# Capturar video desde la cámara USB
def capture_camera():
    camera = cv2.VideoCapture(1)  # 0 indica el primer dispositivo de video (cámara)
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



@app.route('/video_feed')
def video_feed():
    return Response(capture_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def camara():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
