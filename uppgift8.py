#Uppgift 8 – Arv (6 p)

#Skapa:

#· en basklass Fordon med metoden kora()

#· en subklass Bil som ärver från Fordon

#· Bil ska skriva ut något mer specifikt än basklassen när kora() anropas

class Fordon:
    def kora(self):
        return "..."
    
class Bil(Fordon):
    def kora(self):
        return "brum BrumBRUM"
    
f = Fordon()
b = Bil()

print(f.kora())
print(b.kora())
    