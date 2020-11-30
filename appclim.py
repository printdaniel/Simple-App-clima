from tkinter import *
import requests

#728cfb098554b6f599339bc53c37b3e4
#http://api.openweathermap.org/data/2.5/weather
#exclude={part}&appid={YOUR API KEY}

def mostrar_respuesta(res):
    try:
        nombre_ciudad = res["name"]
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]
    
        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp))
        descripcion["text"] = desc
    except:
        ciudad["text"] = "No se reconoce la ciudad"

def clima_JSON(ciudad):
    try:
        API_key = '728cfb098554b6f599339bc53c37b3e4'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        parametros = {"APPID" : API_key, "q":ciudad,"units":"metric","lang":"es"}
        response = requests.get(url,params = parametros)
        res = response.json()
        mostrar_respuesta(res)
    
    except:
        print("Error")
    
    
    
ventana = Tk()
ventana.geometry("350x550")
ventana.title("Clima APP")
ventana.config(bg="snow")

label1 = Label(text="Ingrese ciudad")
label1.pack()

texto_ciudad = Entry(ventana, font=("Courier", 20, "normal"), justify="center")
texto_ciudad.pack()

obtener_clima = Button(ventana, text='Obtener Clima',font = ("Courier", 20, "normal"),
                command = lambda:clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label( font=("Courier", 20, "normal"))
ciudad.pack(padx = 30, pady = 30)

temperatura = Label( font=("Courier", 50, "normal"))
temperatura.pack(padx = 10, pady = 10)

descripcion = Label(font=("Courier", 20, "normal"))
descripcion.pack(padx = 30, pady = 30)

ventana.mainloop()