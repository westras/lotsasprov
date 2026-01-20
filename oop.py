#DEL 3 – KODSKRIVNING (20 p)

#Uppgift 7 – Inkapsling (6 p)

#Skapa en klass Bankkonto som:

#· har ett privat attribut för saldo

#· har en metod satt_in(belopp)

#· har en metod ta_ut(belopp)

#· inte tillåter att saldot blir negativt

#Det räcker att visa klassdefinitionen, ingen testkod krävs.

class Bankkonto:
    def __init__(self):
        self.__saldo = 0

    def satt_in(self, belopp):
        if belopp > 0:
            self.__saldo += belopp

    def ta_ut(self, belopp):
        if 0 < belopp <= self.__saldo:
            self.__saldo -= belopp
        else:
            print("Otillräckligt saldo eller ogiltigt belopp.")

    def get_saldo(self):
        return self.__saldo