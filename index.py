import tkinter as tk
from tkinter import messagebox
import serial
import time
import threading

class PuertaVentanaApp:
    def __init__(self, root, serial_port):
        self.root = root
        self.serial_port = serial_port
        self.serial_conn = None

        # Variables para almacenar el estado de la puerta y ventana
        self.estado_puerta = tk.StringVar(value="Puerta Cerrada")
        self.estado_ventana = tk.StringVar(value="Ventana Cerrada")

        # Configuración de la ventana principal
        self.root.title("Control de Puerta y Ventana")
        self.root.geometry("400x500")
        self.root.eval('tk::PlaceWindow . center')  # Para centrar la ventana principal

        # Etiquetas de temperatura y humedad
        self.temp_label = tk.Label(self.root, text="Temperatura: --- °C", font=("Arial", 12))
        self.hum_label = tk.Label(self.root, text="Humedad: --- %", font=("Arial", 12))
        self.temp_label.pack(pady=10)
        self.hum_label.pack(pady=5)

        # Botón Puerta
        self.puerta_button = tk.Button(self.root, text="Puerta", command=self.abrir_ventana_puerta, 
                                       bg="blue", fg="white", font=("Arial", 16), height=2, width=10)
        self.puerta_button.pack(pady=20)

        # Botón Ventana
        self.ventana_button = tk.Button(self.root, text="Ventana", command=self.abrir_ventana_ventana, 
                                        bg="orange", fg="white", font=("Arial", 16), height=2, width=10)
        self.ventana_button.pack(pady=20)

        # Botón Cerrar Aplicación
        self.cerrar_button = tk.Button(self.root, text="Cerrar Aplicación", command=self.cerrar, 
                                       bg="red", fg="white", font=("Arial", 16), height=2, width=15)
        self.cerrar_button.pack(pady=20)

        # Configuración de la conexión serial con Arduino
        try:
            self.serial_conn = serial.Serial(self.serial_port, 9600, timeout=1)
            time.sleep(2)  # Espera para que se establezca la conexión
        except serial.SerialException as e:
            print(f"Error al conectarse con Arduino: {e}")

        # Iniciar el hilo para actualizar la lectura de temperatura y humedad
        self.actualizar_sensores()

    def actualizar_sensores(self):
        # Hilo para actualizar las lecturas de temperatura y humedad desde Arduino
        def leer_datos():
            while True:
                if self.serial_conn and self.serial_conn.in_waiting > 0:
                    datos = self.serial_conn.readline().decode().strip()
                    if "Humedad" in datos and "Temperature" in datos:
                        try:
                            partes = datos.split("\t")
                            humedad = partes[0].split(": ")[1]
                            temperatura = partes[1].split(": ")[1].replace("*C", "")
                            self.temp_label.config(text=f"Temperatura: {temperatura} °C")
                            self.hum_label.config(text=f"Humedad: {humedad} %")
                        except IndexError:
                            pass
                time.sleep(2)  # Actualización cada 2 segundos

        threading.Thread(target=leer_datos, daemon=True).start()

    def abrir_ventana_puerta(self):
        # Crear una nueva ventana para controlar la puerta
        ventana_puerta = tk.Toplevel(self.root)
        ventana_puerta.title("Control de Puerta")
        ventana_puerta.geometry("300x300")
        #ventana_puerta.eval('tk::PlaceWindow . center')  # Centrar la ventana

        # Etiqueta de estado de la puerta
        estado_label = tk.Label(ventana_puerta, textvariable=self.estado_puerta, font=("Arial", 12))
        estado_label.pack(pady=10)

        # Botón Abrir Puerta
        abrir_button = tk.Button(ventana_puerta, text="Abrir", command=self.abrir_puerta, 
                                 bg="green", fg="white", font=("Arial", 16), height=2, width=10)
        abrir_button.pack(pady=20)

        # Botón Cerrar Puerta
        cerrar_button = tk.Button(ventana_puerta, text="Cerrar", command=self.cerrar_puerta, 
                                  bg="red", fg="white", font=("Arial", 16), height=2, width=10)
        cerrar_button.pack(pady=20)

    def abrir_ventana_ventana(self):
        # Crear una nueva ventana para controlar la ventana
        ventana_ventana = tk.Toplevel(self.root)
        ventana_ventana.title("Control de Ventana")
        ventana_ventana.geometry("300x300")
        #ventana_ventana.eval('tk::PlaceWindow . center')  # Centrar la ventana

        # Etiqueta de estado de la ventana
        estado_label = tk.Label(ventana_ventana, textvariable=self.estado_ventana, font=("Arial", 12))
        estado_label.pack(pady=10)

        # Botón Abrir Ventana
        abrir_button = tk.Button(ventana_ventana, text="Abrir", command=self.abrir_ventana, 
                                 bg="green", fg="white", font=("Arial", 16), height=2, width=10)
        abrir_button.pack(pady=20)

        # Botón Cerrar Ventana
        cerrar_button = tk.Button(ventana_ventana, text="Cerrar", command=self.cerrar_ventana, 
                                  bg="red", fg="white", font=("Arial", 16), height=2, width=10)
        cerrar_button.pack(pady=20)

    def abrir_puerta(self):
        if self.serial_conn:
            try:
                self.serial_conn.write(b'1')  # Enviar el comando '1' para abrir la puerta
                print("Comando 'Abrir Puerta' enviado.")
                self.estado_puerta.set("Puerta Abierta")
            except Exception as e:
                print(f"Error al enviar comando 'Abrir Puerta': {e}")

    def cerrar_puerta(self):
        if self.serial_conn:
            try:
                self.serial_conn.write(b'2')  # Enviar el comando '2' para cerrar la puerta
                print("Comando 'Cerrar Puerta' enviado.")
                self.estado_puerta.set("Puerta Cerrada")
            except Exception as e:
                print(f"Error al enviar comando 'Cerrar Puerta': {e}")

    def abrir_ventana(self):
        if self.serial_conn:
            try:
                self.serial_conn.write(b'3')  # Enviar el comando '3' para abrir la ventana
                print("Comando 'Abrir Ventana' enviado.")
                self.estado_ventana.set("Ventana Abierta")
            except Exception as e:
                print(f"Error al enviar comando 'Abrir Ventana': {e}")

    def cerrar_ventana(self):
        if self.serial_conn:
            try:
                self.serial_conn.write(b'4')  # Enviar el comando '4' para cerrar la ventana
                print("Comando 'Cerrar Ventana' enviado.")
                self.estado_ventana.set("Ventana Cerrada")
            except Exception as e:
                print(f"Error al enviar comando 'Cerrar Ventana': {e}")

    def cerrar(self):
        if self.serial_conn:
            self.serial_conn.close()
        self.root.quit()

if __name__ == "__main__":
    # Definir el puerto serial donde está conectado el Arduino
    SERIAL_PORT = 'COM3'  # Cambia esto por el puerto adecuado en tu sistema

    root = tk.Tk()
    app = PuertaVentanaApp(root, SERIAL_PORT)
    root.protocol("WM_DELETE_WINDOW", app.cerrar)  # Asegurarse de cerrar el puerto serial al salir
    root.mainloop()
