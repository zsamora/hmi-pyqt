import sys
import socket

from tutorialHMI import *


def send_command(text):
    try:
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.connect(('98:d3:51:f5:c9:f4', 1))
        s.send(bytes(text, 'UTF-8'))
        s.close()
    except Exception as e:
        print(e)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # Led and button
        self.led_state = False
        self.pushButton.clicked.connect(self.change_led_state)
        # Dial and LCD
        self.dial.valueChanged.connect(self.slider_moved)

    def change_led_state(self):
        # Led estaba encendido
        if self.led_state:
            send_command("2")
            self.label_2.setText("Secuencia LED apagada")
            self.pushButton.setText("ON")
        # Led estaba apagado
        else:
            send_command("1")
            self.label_2.setText("Secuencia LED encendida")
            self.pushButton.setText("OFF")
        self.led_state = not self.led_state

    def slider_moved(self):
        self.lcdNumber.display(self.dial.value())


if __name__ == "__main__":
    # Crea la aplicación
    app = QtWidgets.QApplication(sys.argv)
    # Crear la ventana principal
    window = MainWindow()
    # Set the form title
    window.setWindowTitle("Tutorial HMI PyQT+RPi")
    # Show form
    window.show()
    # Run the program
    sys.exit(app.exec())