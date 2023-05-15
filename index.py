#aqui se definen las rutas de nuestra pagina

from flask import *
import datetime

app=Flask(__name__)

@app.route('/')#Se llama a la funcion sobre la url principal

def home():
    return render_template('home.html')

def datos():
    data={
        "hora":datetime.datetime.now(),
        "asignatura":"ACO"

    }
    return render_template('datos.html',**data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

