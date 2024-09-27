import tkinter as tk
from gui_puerta import PuertaGUI
from gui_ventana import VentanaGUI
from gui_luces import LucesGUI
from gui_alarma import AlarmaGUI

class InterfazPrincipal:
    def __init__(self, root, arduino_serial):
        self.root = root
        self.arduino_serial = arduino_serial

        # Variables para almacenar el estado de la puerta, ventana y alarma
        self.estado_puerta = tk.StringVar(value="Puerta Cerrada")
        self.estado_ventana = tk.StringVar(value="Ventana Cerrada")
        self.estado_alarma = tk.StringVar(value="Alarma Desactivada")

        # Crear la ventana principal
        self.root.title("Control de Puerta, Ventana, Luces y Alarma")
        self.root.geometry("400x400")
        self.root.eval('tk::PlaceWindow . center')  # Centrar ventana

        # Etiquetas de temperatura y humedad
        self.temp_label = tk.Label(self.root, text="Temperatura: --- °C", font=("Arial", 12))
        self.hum_label = tk.Label(self.root, text="Humedad: --- %", font=("Arial", 12))
        self.temp_label.pack(pady=10)
        self.hum_label.pack(pady=5)

        # Botones para abrir ventanas de Puerta, Ventana, Luces y Alarma
        self.puerta_button = tk.Button(self.root, text="Puerta", command=self.abrir_ventana_puerta, 
                                       bg="blue", fg="white", font=("Arial", 16), height=2, width=10)
        self.puerta_button.pack(pady=10)

        self.ventana_button = tk.Button(self.root, text="Ventana", command=self.abrir_ventana_ventana, 
                                        bg="orange", fg="white", font=("Arial", 16), height=2, width=10)
        self.ventana_button.pack(pady=10)

        self.luces_button = tk.Button(self.root, text="Luces", command=self.abrir_ventana_luces, 
                                      bg="yellow", fg="black", font=("Arial", 16), height=2, width=10)
        self.luces_button.pack(pady=10)

        self.alarma_button = tk.Button(self.root, text="Alarma", command=self.abrir_ventana_alarma, 
                                       bg="red", fg="white", font=("Arial", 16), height=2, width=10)
        self.alarma_button.pack(pady=10)

        # Botón para cerrar la aplicación
        self.cerrar_button = tk.Button(self.root, text="Cerrar Aplicación", command=self.cerrar, 
                                       bg="gray", fg="white", font=("Arial", 16), height=2, width=15)
        self.cerrar_button.pack(pady=20)

        # Iniciar la actualización de la lectura de sensores
        self.actualizar_sensores()

    def actualizar_sensores(self):
        datos = self.arduino_serial.leer_datos()
        if datos and "Humedad" in datos and "Temperature" in datos:
            try:
                partes = datos.split("\t")
                humedad = partes[0].split(": ")[1]
                temperatura = partes[1].split(": ")[1].replace("*C", "")
                self.temp_label.config(text=f"Temperatura: {temperatura} °C")
                self.hum_label.config(text=f"Humedad: {humedad} %")
            except IndexError:
                pass

        # Vuelve a ejecutar la función después de 2 segundos (2000 milisegundos)
        self.root.after(2000, self.actualizar_sensores)

    def abrir_ventana_puerta(self):
        PuertaGUI(self.root, self.arduino_serial, self.estado_puerta)

    def abrir_ventana_ventana(self):
        VentanaGUI(self.root, self.arduino_serial, self.estado_ventana)

    def abrir_ventana_luces(self):
        LucesGUI(self.root, self.arduino_serial)

    def abrir_ventana_alarma(self):
        AlarmaGUI(self.root, self.arduino_serial, self.estado_alarma)

    def cerrar(self):
        self.arduino_serial.cerrar()
        self.root.quit()

