import tkinter as tk
from arduino_serial import ArduinoSerial
from gui_principal import InterfazPrincipal

if __name__ == "__main__":
    # Definir el puerto serial donde está conectado el Arduino
    SERIAL_PORT = 'COM3'  # Cambia esto por el puerto adecuado en tu sistema

    # Crear la conexión con Arduino
    arduino = ArduinoSerial(SERIAL_PORT)

    # Crear la ventana principal de la aplicación
    root = tk.Tk()
    app = InterfazPrincipal(root, arduino)

    # Ejecutar la aplicación de Tkinter
    root.protocol("WM_DELETE_WINDOW", app.cerrar)  # Asegurar el cierre correcto del puerto serial
    root.mainloop()
