#Uppgift 9 – Polymorfism (8 p)

#Skapa ett exempel som visar polymorfism:

#· minst en basklass

#· minst två subklasser

#· samma metodnamn i alla klasser

#· visa (med kod) att rätt metod anropas beroende på objektets typ

class Djur:
    def djurläte(self):
        pass
        
class Hund(Djur):
    def djurläte(self):
        print("voff")
        
class Katt(Djur):
    def djurläte(self):
        print("Mjau")
        
lista = [Hund(), Katt()]

for f in lista:
    f.djurläte() 