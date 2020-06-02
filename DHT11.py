#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:19:51 2020
Código extraídoy modificado de sitio web https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/
https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/
@author: pi
"""

import Adafruit_DHT  
import time 
import RPi.GPIO as GPIO# libreria para utitlizar los puertos GPIO de la raspberry
#print("I miss u")
class DHT11(object): 
    def __init__(self,sensor = Adafruit_DHT.DHT11, pin = 4 ):
        self.sensor = sensor
        self.pin = pin
#sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
#pin = 4 #Pin en la raspberry donde conectamos el sensor
    def lectura(self):
        _,temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        time.sleep(10) #Cada segundo se evalúa el sensor
        #print("La temperatura es: ",temperatura)
        return temp
    def imprimir(self):
        
        print("La temperatura es: ",self.lectura())
 # print ('Humedad: ' , humedad)
  #print ('Temperatura: ' , temperatura)
#dht11 = DHT11()
#dht11.imprimir()
