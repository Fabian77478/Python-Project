def sum(Zahl1, Zahl2):
    return Zahl1 + Zahl2

def Minus(Minuszahl1, Minuszahl2):
    return Minuszahl1 - Minuszahl2

def Multiplikation (Multiplikationszahl1, Multiplikationszahl2):
    return Multiplikationszahl1 * Multiplikationszahl2

def Division (DivisionsZahl1, DivisionsZahl2):
    return DivisionsZahl1 / DivisionsZahl2

Zahleingabe1 = int(input("Geben sie eine Belibige Zahl ein : "))
Zahleingabe2 = int(input ("Geben Sie eine weitere Zahl ein :"))

Rechnungseingabe = input ("Geben Sie ein mit welcher Rechenfunktion Sie die Zahl erechnen wollen :")

if Rechnungseingabe == "sum":
    Resultat = sum(Zahleingabe1, Zahleingabe2)
    print(f"Das ist das Resultat {Resultat}")

elif Rechnungseingabe == "Minus":
    MinusResultat = Minus(Zahleingabe1, Zahleingabe2)
    print(f"Das ist das Resultat {MinusResultat}")

elif Rechnungseingabe == "Multiplikation":
    Multiplikationsresultat = Multiplikation(Zahleingabe1, Zahleingabe2)
    print(f"Das ist das Resultat {Multiplikationsresultat}")
    


elif Rechnungseingabe  == "Division":
    Divisionresultat = Division(Zahleingabe1, Zahleingabe2)
    print(f"Das ist das Resultat {Divisionresultat}")