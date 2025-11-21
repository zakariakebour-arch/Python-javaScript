# Python-javaScript
# Proyecto Flask - Interacción con JSON

Este es un proyecto sencillo utilizando **Flask** en Python que permite interactuar con un archivo **JSON**. La aplicación tiene un formulario web donde el usuario puede ingresar su nombre, apellidos, edad y teléfono. Los datos ingresados se guardan en un archivo `archivo.json` y luego se muestran en una página dinámica utilizando **JavaScript**.

## Descripción del Proyecto

El código consta de dos partes principales:

1. **Backend (Flask)**:
   - La aplicación está construida con Flask, un micro-framework de Python.
   - En la ruta principal (`/`), se sirve un formulario HTML donde los usuarios pueden ingresar datos.
   - Al enviar el formulario, los datos se reciben a través de la ruta `/recibir`, se almacenan en un archivo JSON (`archivo.json`), y luego se muestra una página de respuesta.

2. **Frontend (HTML + JavaScript)**:
   - El archivo `index.html` contiene el formulario para ingresar los datos del usuario.
   - El archivo `respuesta.html` muestra los datos guardados en el archivo JSON en formato de tarjetas.
   - **JavaScript** se utiliza para leer el archivo `archivo.json` y mostrar los datos de manera dinámica en la página.

Este proyecto es ideal para aprender a trabajar con formularios en Flask, cómo manejar datos en formato JSON y cómo interactuar con ellos en una interfaz web utilizando JavaScript.

## ¿Cómo funciona?

1. El usuario ingresa sus datos en el formulario de `index.html` (nombre, apellidos, edad, teléfono).
2. Cuando el formulario se envía, Flask recibe los datos y los guarda en el archivo `archivo.json`.
3. En la página de `respuesta.html`, JavaScript lee el archivo JSON y muestra los datos de manera estructurada en tarjetas.

## Requisitos

- **Python 3.x**
- **Flask**

Este proyecto está diseñado para ser un ejemplo sencillo de cómo interactuar con archivos JSON en una aplicación web.

