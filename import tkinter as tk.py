import tkinter as tk
from tkinter import messagebox
import requests

# Diccionario con ciudades representativas por país
ciudades_por_pais = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Reino Unido": "Londres",
    "Estados Unidos": "Washington",
    "México": "Ciudad de México",
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Alemania": "Berlín",
    "Canadá": "Ottawa",
    "Australia": "Sídney",
    "Japón": "Tokio",
    "Rusia": "Moscú",
    "India": "Nueva Delhi"
}

def obtener_temperatura(ciudad, api_key):
    """Obtiene la temperatura de una ciudad utilizando la API de OpenWeatherMap."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Levanta un error si el código de estado no es 200
        datos = respuesta.json()

        # Si la respuesta de la API es exitosa (código 200)
        if datos['cod'] == 200:
            temperatura = datos['main']['temp']
            descripcion = datos['weather'][0]['description']
            return f"La temperatura en {ciudad} es {temperatura}°C con {descripcion}."
        else:
            return "No se pudo obtener los datos del clima. Verifica la ciudad o la clave de la API."
    
    except requests.exceptions.RequestException as e:
        return f"Error al obtener los datos: {str(e)}"
    except KeyError:
        return "Error al procesar los datos. Puede que la API haya devuelto un formato inesperado."

def mostrar_clima():
    """Función que maneja la interacción con la interfaz y muestra el clima."""
    pais = entry_pais.get().strip()
    api_key = 'tu_clave_de_api'  # Reemplaza con tu clave de API

    if pais == "":
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa el nombre de un país.")
        return

    if pais in ciudades_por_pais:
        ciudad = ciudades_por_pais[pais]
        resultado = obtener_temperatura(ciudad, api_key)
    else:
        resultado = "El país ingresado no está disponible en nuestro sistema."

    # Mostrar el resultado en la ventana
    label_resultado.config(text=resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Termómetro de Clima Global")
ventana.geometry("400x300")

# Título
label_titulo = tk.Label(ventana, text="Clima de los países", font=("Arial", 16))
label_titulo.pack(pady=10)

# Ingreso del país
label_pais = tk.Label(ventana, text="Introduce el nombre de un país:", font=("Arial", 12))
label_pais.pack(pady=5)

entry_pais = tk.Entry(ventana, font=("Arial", 12))
entry_pais.pack(pady=5)

# Botón para obtener la temperatura
boton_clima = tk.Button(ventana, text="Obtener Clima", font=("Arial", 12), command=mostrar_clima)
boton_clima.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=20)

# Ejecutar la interfaz
ventana.mainloop()
