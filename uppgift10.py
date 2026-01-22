#Uppgift 10 – Inkapsling med property (6 p)

#Skapa en klass Produkt som:

#· har ett privat attribut för pris

#· använder property för att läsa och sätta priset

#· inte tillåter att priset sätts till ett negativt värde

class Produkt:
    def __init__(self, pris):
        self._pris = 0
        self.pris = pris
        
    @property
    def pris(self):
        return self._pris
    
    @pris.setter
    def pris(self, value):
        if value >= 0:
            self._pris = value
            
 
produkt = Produkt(100)
print(produkt.pris)  