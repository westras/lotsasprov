#Uppgift 13 – Kombinerad uppgift (Inkapsling + Arv) (10 p)
#Skapa en basklass Konto som:
#· har ett privat attribut för saldo
#· har en metod för att läsa saldot
#Skapa sedan en subklass Sparkonto som:
#· ärver från Konto
#· har en metod lagg_till_ranta() som ökar saldot med ränta

class Konto:
    def __init__(self, saldo):
        self._saldo = saldo
        
    def läsKonsto(saldo):
        print(saldo)

class Sparkonto(Konto):
        
    def lägg_till_ränta(self, ränta):
        if ränta >=0:
            self._saldo += self._saldo * ränta / 100


sparkonto = Sparkonto(1000)
sparkonto.lägg_till_ränta(5)
print(sparkonto._saldo)