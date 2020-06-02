#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:19:45 2020

@author: pi
"""
# importing whole module 
from tkinter import * 
from tkinter.ttk import *         
# importing strftime function to 
# retrieve system's time
import RPi.GPIO as GPIO# libreria para utitlizar los puertos GPIO de la raspberry 
from time import strftime 
from time import sleep


# creating tkinter window 
root = Tk() 
root.title('Clock') 

#definir artibutos GPIO's
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=23  
GPIO.setup(buzzer,GPIO.OUT)
  
# This function is used to   
# display time on the label 
def time():
    horas_medicinas = ['11:58:00 AM','11:58:10 AM','11:58:15 AM']
    string = strftime('%H:%M:%S %p') 
    if string in horas_medicinas: 
        string = "Please take your medicines"
        GPIO.output(buzzer,GPIO.HIGH)
        print ("Beep")
        sleep(0.2) # Delay in seconds
        GPIO.output(buzzer,GPIO.LOW)
        print ("No Beep")
        sleep(0.2)

    lbl.config(text = string) 
    lbl.after(1000, time) 
  
# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'green', 
            foreground = 'white') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
time() 
  
mainloop() 
