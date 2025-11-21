from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/recibir", methods=['POST', 'GET'])
def recibir():
    # Intentamos leer el archivo JSON y cargar los datos actuales
    try:
        with open("static/archivo.json", "r") as archivo:
            lista = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, inicializamos la lista vacía
        lista = []

    # Creamos un nuevo diccionario con los datos recibidos
    persona = {
        'nombre': request.form['nombre'],
        'apellidos': request.form['apellidos'],
        'edad': request.form['edad'],
        'telefono': request.form['telefono']
    }
    
    # Añadimos la nueva persona a la lista
    lista.append(persona)
    
    # Guardamos la lista actualizada de vuelta en el archivo JSON
    with open("static/archivo.json", "w") as archivo:
        json.dump(lista, archivo, indent=4)
        
    return render_template("respuesta.html")

if __name__ == '__main__':
    app.run(debug=True)
