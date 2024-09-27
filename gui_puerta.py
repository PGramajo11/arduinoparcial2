import tkinter as tk

class PuertaGUI:
    def __init__(self, root, arduino_serial, estado_puerta):
        self.arduino_serial = arduino_serial
        self.estado_puerta = estado_puerta

        # Crear la ventana de la Puerta
        ventana_puerta = tk.Toplevel(root)
        ventana_puerta.title("Control de Puerta")
        ventana_puerta.geometry("300x200")
        #ventana_puerta.eval('tk::PlaceWindow . center')  # Centrar ventana

        # Etiqueta de estado
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

    def abrir_puerta(self):
        self.arduino_serial.enviar_comando('1')
        self.estado_puerta.set("Puerta Abierta")

    def cerrar_puerta(self):
        self.arduino_serial.enviar_comando('2')
        self.estado_puerta.set("Puerta Cerrada")
