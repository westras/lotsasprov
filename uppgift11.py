#Uppgift 11 – Arv med gemensam basklass (6 p)

#Skapa:

#· en basklass Anstalld med attribut namn

#· en metod beskrivning() som skriver ut något generellt

#· två subklasser: Larare och Rektor

#· båda subklasserna ska skriva över beskrivning()

#Visa gärna ett exempel på hur metoden anropas.

class Anställd:
    def __init__(self, namn):
        self.namn = namn
        
    def beskrivning(self):
        print("Information")
    
class Lärare(Anställd):
    def __init__(self, namn):
        super().__init__(namn)
    
    def beskrivning(self):
        return super().beskrivning()
    
class Rektor(Anställd):
    def __init__(self, namn):
        super().__init__(namn)
    
    def beskrivning(self):
        return super().beskrivning()
    
r = Rektor
l = Lärare
