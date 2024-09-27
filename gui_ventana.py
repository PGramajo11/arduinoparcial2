import tkinter as tk

class VentanaGUI:
    def __init__(self, root, arduino_serial, estado_ventana):
        self.arduino_serial = arduino_serial
        self.estado_ventana = estado_ventana

        # Crear la ventana de la Ventana
        ventana_ventana = tk.Toplevel(root)
        ventana_ventana.title("Control de Ventana")
        ventana_ventana.geometry("300x200")
        #ventana_ventana.eval('tk::PlaceWindow . center')  # Centrar ventana

        # Etiqueta de estado
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

    def abrir_ventana(self):
        self.arduino_serial.enviar_comando('3')
        self.estado_ventana.set("Ventana Abierta")

    def cerrar_ventana(self):
        self.arduino_serial.enviar_comando('4')
        self.estado_ventana.set("Ventana Cerrada")
