# Autor: Noah Kronhardt
# Datum: 02.07.2025
# Beschreibung: Dieses Python-Programm misst die CPU- und RAM-Auslastung alle 2 Sekunden
# für 30 Sekunden lang und schreibt sie in eine .csv-Datei.

import psutil
import csv
import datetime
import time
import os

# CPU-Auslastung abrufen
def Get_processorUsage():
    return psutil.cpu_percent(interval=0.5)

# RAM-Auslastung (verwendeter Speicher)
def Get_RAMusage():
    return int(psutil.virtual_memory().used)

# CSV-Header in bestehende Datei schreiben
def Create_LogAttributes(Path):
    fields = ["Time", "CPU Auslastung", "RAM Auslastung (GB)"]
    if os.path.exists(Path):
        if Path.endswith(".csv"):
            with open(Path, "a", newline='') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow(fields)
        else:
            print(f"{Path} ist keine CSV-Datei.")
    else:
        print(f"{Path} existiert nicht.")

# Neue CSV-Datei erstellen inkl. Header
def Create_NewLogfile(Path):
    with open(Path, "w", newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["Time", "CPU Auslastung", "RAM Auslastung (GB)"])

def main():
    print("1: Logdatei (.csv) vorhanden und ohne Attribute")
    print("2: Logdatei (.csv) vorhanden mit Attributen")
    print("3: Noch keine Logdatei vorhanden")

    AntwortLogdatei = int(input("Auswahl (1/2/3): "))

    Path = ""

    if AntwortLogdatei in [1, 2]:
        Path = input("Gebe den Pfad zu deiner Logdatei an: ")

        if AntwortLogdatei == 1:
            Create_LogAttributes(Path)
        else:
            if os.path.exists(Path) and Path.endswith(".csv"):
                print(f"{Path} ist gültig.")
            else:
                print(f"{Path} ist ungültig.")
                return  # abbrechen

    elif AntwortLogdatei == 3:
        Ordner = input("Gebe den Ordnerpfad an, in dem die Datei gespeichert werden soll: ")
        Dateiname = input("Gebe den Dateinamen ein (ohne .csv): ")

        if not os.path.exists(Ordner):
            print(f"Der Ordner '{Ordner}' existiert nicht.")
            return

        Path = os.path.join(Ordner, f"{Dateiname}.csv")
        Create_NewLogfile(Path)
        print(f"Neue Logdatei erstellt: {Path}")

    else:
        print("Ungültige Eingabe.")
        return

    # --- Aufzeichnung starten ---
    print("Starte Systemüberwachung für 30 Sekunden...")
    start_time = time.time()

    while time.time() - start_time < 30:
        timestamp = datetime.datetime.now()
        cpu_usage = Get_processorUsage()
        ram_usage = Get_RAMusage()

        row = [
            f"{timestamp}",
            f"{cpu_usage:.2f} %",
            f"{ram_usage / 1024 / 1024 / 1024:.2f} GB"
        ]

        with open(Path, "a", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)

        print(f"[{timestamp}] CPU: {cpu_usage:.2f} %, RAM: {ram_usage / 1024 / 1024 / 1024:.2f} GB")
        time.sleep(2)

    print("Messung abgeschlossen. Logdatei gespeichert unter:")
    print(Path)

if __name__ == "__main__":
    main()
