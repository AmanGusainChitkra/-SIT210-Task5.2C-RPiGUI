from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
import sys

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

button1 = 10
button2 = 12
button3 = 13


#Defining functions to toggle leds
def button1Press():
    print("Button1")
    GPIO.output(button1, not GPIO.input(button1))
def button2Press():
    print("Bitton2")
    GPIO.output(button2, not GPIO.input(button2))
def button3Press():
    print("Button3")
    GPIO.output(button3, not GPIO.input(button3))
def exit():
    print("Exit")
    GPIO.cleanup()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("LedControl")

layout = QHBoxLayout()

#declaring buttons for Leds
Wbutton1 = QPushButton("Red")
Wbutton2 = QPushButton("Yellow")
Wbutton3 = QPushButton("Green")
Wbutton1.setStyleSheet("background-color : red")
Wbutton2.setStyleSheet("background-color : blue")
Wbutton3.setStyleSheet("background-color : green")
Wbutton1.clicked.connect(button1Press)
Wbutton2.clicked.connect(button2Press)
Wbutton3.clicked.connect(button3Press)

# adding buttons to the layout
layout.addWidget(Wbutton1)
layout.addWidget(Wbutton2)
layout.addWidget(Wbutton3)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
