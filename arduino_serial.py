import serial
import time

class ArduinoSerial:
    def __init__(self, serial_port):
        try:
            self.serial_conn = serial.Serial(serial_port, 9600, timeout=1)
            time.sleep(2)  # Espera para que se establezca la conexión
        except serial.SerialException as e:
            print(f"Error al conectarse con Arduino: {e}")
            self.serial_conn = None

    def enviar_comando(self, comando):
        if self.serial_conn:
            try:
                self.serial_conn.write(comando.encode())
                print(f"Comando '{comando}' enviado.")
            except Exception as e:
                print(f"Error al enviar comando '{comando}': {e}")

    def leer_datos(self):
        if self.serial_conn and self.serial_conn.in_waiting > 0:
            datos = self.serial_conn.readline().decode().strip()
            return datos
        return None

    def cerrar(self):
        if self.serial_conn:
            self.serial_conn.close()
