import tkinter as tk

class LucesGUI:
    def __init__(self, root, arduino_serial):
        self.arduino_serial = arduino_serial

        # Crear la ventana de las Luces
        ventana_luces = tk.Toplevel(root)
        ventana_luces.title("Control de Luces")
        ventana_luces.geometry("300x200")
        #ventana_luces.eval('tk::PlaceWindow . center')  # Centrar la ventana

        # Botón Prender
        prender_button = tk.Button(ventana_luces, text="Prender", command=self.prender_luces, 
                                   bg="green", fg="white", font=("Arial", 16), height=2, width=10)
        prender_button.pack(pady=20)

        # Botón Apagar
        apagar_button = tk.Button(ventana_luces, text="Apagar", command=self.apagar_luces, 
                                  bg="red", fg="white", font=("Arial", 16), height=2, width=10)
        apagar_button.pack(pady=20)

    def prender_luces(self):
        self.arduino_serial.enviar_comando('5')  # Enviar el comando '5' para prender las luces
        print("Comando 'Prender Luces' enviado.")

    def apagar_luces(self):
        self.arduino_serial.enviar_comando('6')  # Enviar el comando '6' para apagar las luces
        print("Comando 'Apagar Luces' enviado.")