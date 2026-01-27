#Uppgift 12 – Polymorfism i lista (8 p)

#Utgå från en basklass Spelkaraktar med metoden attack().

#Skapa minst två olika subklasser som:

#· ärver från Spelkaraktar

#· har olika implementationer av attack()

#Skapa sedan en lista med olika karaktärer och visa med kod att:

#· rätt attack()-metod anropas för varje objekt

class spelkaraktär:
    def attack():
        pass
    
class paladin(spelkaraktär):
    def attack():
        return "SvärdSving"

class Magiker(paladin):
    def attack():
        return "Fireball"
    
p = paladin
M = Magiker

print(p.attack())
print(M.attack())
