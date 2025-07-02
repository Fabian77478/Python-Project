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

import os

import subprocess

def Get_processorUsage():
    return psutil.cpu_percent(interval=0.5)

def Get_RAMavailable():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

def Create_LogAttributes(Path):
    fields = ["Time", "CPU Auslastung", "RAM Auslastung(GB)"]
    if os.path.exists(Path):
            if Path.endswith(".csv"):
                 with open (Path, "a") as F:
                      csvwriter = csv.writer(F)
                      csvwriter.writerow(fields)
            else:
                 print (f"{Path} ist keine CSV Datei")
    else:
         print (f"{Path} existiert nicht")

def Create_NewLogfile(Directory, Name):
    if os.path.exists(Directory) and os.path.isdir(Directory):
          Command = ["mkdir", Name, ".csv"]
          subprocess.call(Command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
         print (f"{Directory} exists")

def main():
    print ("1: Logdatei(.csv) vorhanden und ohne Attribute")
    print ("2: Logdatei(.csv) vorhanden mit Attributen")
    print ("3. Noch keine Logdatei vorhanden")
    AntwortLogdatei = int(input())
    if (AntwortLogdatei == 1 or AntwortLogdatei == 2):
         print ("Gebe den Pfad zur deiner Logdatei an")
         Path = input()
         if (AntwortLogdatei == 1):
              Create_LogAttributes(Path)
         else:
            if os.path.exists(Path) and Path.endswith(".csv"):
                 print(f"{Path} ist gültig")
            else:
                 print(f"{Path} ist ungültig")
    else:
        print ("Gebe den Ordner ein in welchem du die Datei speichern möchtest:")
    #Path = "C:\\Users\\oha_n\\Desktop\\Projekte\\Pyhton\\SystemMonitorGit\\Python-Project\\SystemMonitor\\logs\\systemlog.csv"
    start_time = time.time()
    #print ("System CPU Usage is {} %".format(Get_processorUsage()))
    #print (f"System RAM Usage is {int(Get_RAMusage() /1024 /1024 /1024)} GB") 
    while time.time() - start_time < 30:
        #zeitstempel generieren
        Zeitstempel = datetime.datetime.now()
        Processor_Usage = Get_processorUsage()
        RAM_Available = Get_RAMavailable()
        row = []
        
        row.append(f"{Zeitstempel}")
        row.append(f"{Processor_Usage: .2f} %")
        row.append(f"{int(RAM_Available /1024 /1024 /1024)} GB")
        with open(Path, "a") as csvfile:
             csvwriter = csv.writer(csvfile)
             csvwriter.writerow(row)

if __name__ == "__main__":
    main()
