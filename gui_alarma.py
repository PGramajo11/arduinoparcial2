import tkinter as tk

class AlarmaGUI:
    def __init__(self, root, arduino_serial, estado_alarma):
        self.arduino_serial = arduino_serial
        self.estado_alarma = estado_alarma

        # Crear la ventana de la Alarma
        ventana_alarma = tk.Toplevel(root)
        ventana_alarma.title("Control de Alarma")
        ventana_alarma.geometry("300x200")
        #ventana_alarma.eval('tk::PlaceWindow . center')  # Centrar la ventana

        # Etiqueta de estado de la alarma
        estado_label = tk.Label(ventana_alarma, textvariable=self.estado_alarma, font=("Arial", 12))
        estado_label.pack(pady=10)

        # Botón Activar Alarma
        activar_button = tk.Button(ventana_alarma, text="Activar", command=self.activar_alarma, 
                                   bg="green", fg="white", font=("Arial", 16), height=2, width=10)
        activar_button.pack(pady=20)

        # Botón Desactivar Alarma
        desactivar_button = tk.Button(ventana_alarma, text="Desactivar", command=self.desactivar_alarma, 
                                      bg="red", fg="white", font=("Arial", 16), height=2, width=10)
        desactivar_button.pack(pady=20)

    def activar_alarma(self):
        self.arduino_serial.enviar_comando('7')  # Enviar el comando '7' para activar la alarma
        self.estado_alarma.set("Alarma Activa")
        print("Comando 'Activar Alarma' enviado.")

    def desactivar_alarma(self):
        self.arduino_serial.enviar_comando('8')  # Enviar el comando '8' para desactivar la alarma
        self.estado_alarma.set("Alarma Desactivada")
        print("Comando 'Desactivar Alarma' enviado.")
