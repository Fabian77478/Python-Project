#Autor : Fabian Cina
#Datum : 02.07.2025
#Beschreibung : Netzwerk- und Systeminformationen auslesen und speichern

# Importieren von Modulen
import socket
from getmac import get_mac_address as gma
import platform
from datetime import datetime
import os

import subprocess

# Funktion zum Prüfen, ob ein Host erreichbar ist
def ping(host, Count):
    if platform.system() == "Windows":
        parameter = "-n"
    else:
        parameter = "-c"

    command = ["ping", parameter, Count, host]
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if response == 0:
        return True
    else:
        return False

# Hauptfunktion
def main():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    mac = gma()
    system = platform.system()
    version = platform.version()
    now = datetime.now()
    zeit = now.strftime("%Y-%m-%d %H:%M:%S")
    Google = ping("google.com", "1") 
    # Pfad zur Textdatei
    pfad = r"C:\Users\fabia\Desktop\Projekt-Python\Python-Project\Python-Project\Taschenrechner\Netzwerk-Monitoring & Systeminformation mit Python\system_report.txt"

    # Konsolenausgabe
    print("-------------------------------------------------------------------")
    print(f"Hostname: {hostname}")
    print(f"Ip-Adresse: {ip_address}")
    print("-------------------------------------------------------------------")
    print(f"MAC: {mac}")
    print("-------------------------------------------------------------------")
    print(f"System: {system}")
    print(f"Version: {version}")
    print("-------------------------------------------------------------------")
    print(f"Datetime: {now}")
    print(f"Zeit: {zeit}")

    # Ausgabe in Datei schreiben (anhängen)
    with open(pfad, "a") as Skript:
        Skript.write("-------------------------------------------------------------------\n")
        Skript.write(f"Hostname: {hostname}\n")
        Skript.write(f"IP-Adresse: {ip_address}\n")
        Skript.write(f"MAC-Adresse: {mac}\n")
        Skript.write(f"Betriebssystem: {system}\n")
        Skript.write(f"Version: {version}\n")
        Skript.write(f"Zeitpunkt: {zeit}\n")
        Skript.write("-------------------------------------------------------------------\n\n")
    print (Google)

if __name__ == "__main__":
    main()


# Ende des Skripts
# Autor : Fabian Cina
# Datum : 02.07.2025
# Beschreibung : Netzwerk- und Systeminformationen auslesen und speichern