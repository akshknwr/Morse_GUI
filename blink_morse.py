import Rpi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QRadioButton, QDialog,  QGridLayout, QVBoxLayout, QWidget,QLineEdit, QFormLayout
import sys
import numpy as np   # import the numpy package
import json           # this package needed for processing csv file
from collections import Counter  # this is for dictionary construction with counting functionality
import functools
import time


led=8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)




class UI_blinkMorse(QDialog):
    def __init__(self):
        super(UI_blinkMorse, self).__init__()

        self.le = QLineEdit()
        self.le.setObjectName("host")
        self.le.setPlaceholderText("enter few characters ..max 12 characters allowed")
        self.le.setMinimumWidth(500)

       
        


        self.pb = QPushButton()
        self.pb.setObjectName("blink")
        self.pb.setText("Blink") 
        self.pb.clicked.connect(functools.partial(self.blink_morse))

        self.label= QLabel()
        self.label.setText("text will appear here")
        self.morseLabel=QLabel()
        


        layout = QFormLayout()
        layout.addWidget(self.le)
        layout.addWidget(self.pb)
        layout.addWidget(self.label)
        layout.addWidget(self.morseLabel)
        # QTextEdit.textChanged.connect(your_method_to_put_text_somewhere_else)

        self.setLayout(layout)
 



        # self.connect(self.pb, Signal("clicked()"),self.button_click)
        self.setWindowTitle("Learning")

    def button_click(self):
        # shost is a QString object
        shost = self.le.text()
        print(shost)

    def button_clicked(self):
        self.le.setText("shost")


    def mymorsecode(self):
        characters=self.le.text()
        DATA_FILE="morse_code.json"
        with open(DATA_FILE, 'rb') as fp:
             fcontent = fp.read()
        data = json.loads(fcontent)
        self.morseLabel.setText("\n\nMorse Code for given characters\n \n")
       
        for texts in range(len(characters)):
            char = (characters[texts])
            morsecode=str(data[char]) 
            print(morsecode)
            morseLbl=self.morseLabel.text() + morsecode+"\n"
            self.morseLabel.setText(morseLbl)
            for code in range(len(morsecode)):
                duration=0
                if(morsecode[code]=="."):
                    duration=0.4
                elif(morsecode[code]=="-"):
                    duration=0.8
                self.blinkLed(duration)    
                print(morsecode[code])


       

    def blinkLed(self,duration):
        GPIO.output(led,HIGH)
        time.sleep(duration)
        GPIO.output(led,LOW)
        time.sleep(duration)

    def blink_morse(self):
        text=self.le.text()
        if(len(text)>=12):
            self.label.setText("Number of entered characters are more than 12 so please enter less characters and try again")
        elif(text=="" or text==" " ):
            self.label.setText("You have not entered anything")
        else:
            self.label.setText(text)
            self.label.setText("You've entered  " +str(len(text))+ " characters \n now its blinking")
            self.mymorsecode()
    




 



def starttheapp():
    app=QApplication(sys.argv)

    window = UI_blinkMorse()
    window.resize(800,600)
    window.setWindowTitle("Blink Morse code using GUI")



    window.show()
    sys.exit(app.exec_())


starttheapp()


