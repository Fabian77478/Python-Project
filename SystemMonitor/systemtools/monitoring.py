#Autor : Noah Kronhardt
#Datum : 02.07.2025
#Beschreibung : Dieses Python-Programm, misst die CPU- und RAM Auslastung alle 2 Sekunden für 30 Sekunden lang und schreibt sie in eine .csv Datei

#Dieses Modul für Systemdaten:
import psutil

#Dieses Modul ist für Dateischreiben
import csv

#Dieses Modul für Zeitstempel
import datetime

#Modul für Zeitsteuerung
import time

def Get_processorload():
    return psutil.cpu_percent(interval=0.5)

print (Get_processorload())