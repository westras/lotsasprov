# lotsasprov
låtsas prov för programmering 2 i oop

del 1 grundbegrebb

a) Vad menas med inkapsling? (2 p)
    Inkapsling är ett sätt att gömma eller skydda vissa bitar av information. Säg att vi har en bank. Varje person har olika saldon med olika mängder pengar. Banker behöver att denna information är privat precis som bank nummer och liknande grejer. Med hjälp av inkaplsing så kan man göra att informationen i en variabel inte kan åtkommas hur som helst. det måste öppnas med en getter och ändras med en setter. saldo = _saldo
 b) Vad menas med arv? (2 p) 
Arv är ett sätt att undvika att skriva samma kod flera gånger inom oop. Säg att vi har en basklass som heter bil. Vi har bland annat information om bilens längd och bredd. Dethär är information som alla bilar i hela världen har. Om vi har en subklass som heter ferrari, en som eter lamborghini etc. och så har vi bil som basklass så kan vi använda oss av längd och bredd variablarna samt lägga till flera om det skulle bheövas. Men vi slipper skriva om en del av koden vilket sparar tid. 

 c) Vad menas med polymorfism? (2 p)
 Polymorfism kan på sätt och vis sägas vara att samma variabel har flera olika värden beroende på vilken subklass de tillhör. säg att vi har fem olika djur. Sen har vi en varaibel som heter djurläten. Vi kan då i en subklass tilldela olika ljud till de olika djuren. när vis tillkallar funktionen för alla djuren så kommer de ge olika ljudläten även fast alla variabler heter djurläten. Det gör koden mycket mer robus och lättförtåelig.
--------------------------------------------------------------

 Uppgift 2 – Inkapsling i praktiken (4 p)

Varför är inkapsling viktigt i objektorienterad programmering? Ge två olika anledningar.

Anledning ett gick jag lote igeom i föregående fråga. Om man ska ha hemlig informatione eller information som inte ska synas så kan man använda sig av inkaplsing för att gömma undan koden och bara visa den i specefika sammanhang.
Den andra anledningen är för att man inte ska kunna komma in och ändra en bit kod eller information hur som helst. Säg att vi har t. ex ett bankkonto med pengar på. då ska jag inte kunna gå in och öka nummret hur jag vill eftersom det hade varit pengarfusk. 
------------------------------------------------------------
Uppgift 3 – Arv och polymorfism (5 p)

Beskriv med ord vad som händer när:

· en metod skrivs i en basklass

· och sedan skrivs om (överskuggas) i en subklass

Hur hänger detta ihop med polymorfism?

Detta kan först beskrivas som arv. Vi har en basklass som
 Djur() den läggs till i subklassen Hund(Djur) Den koden vi har i basklassen kan nu enkelt återanvändas i subklassen. Det innebär inte att informationen vi sparar i Djur kommer att vara i hund. Säg att vi säger att funktionen djurläte har en variabel som säger ... i basklassen. Den kan överskuggas genom att vi returnerar ett annat värde/variabel i subklassen t. ex vow! Detta är polymorfism. När vi överskuggar så har vi samma variabel eller funktion namn. Eftersom namnen är likadana men ger olika världen så är detta polymorfism vilket gör koden mer robus och återanvändbar.
--------------------------------------------------------------

DEL 2 – KODTOLKNING (15 p)

Uppgift 4 – Inkapsling och properties (5 p)

Studera koden:


class Person:

def __init__(self, namn, alder):

self._namn = namn

self._alder = alder

@property

def alder(self):

return self._alder

@alder.setter

def alder(self, value):

if value >= 0:

self._alder = value


a) Vad är syftet med att använda _alder istället för alder? (2 p)
Anledningen varför man anväder sig av _ålder och för att använda inkapsling. Man gör alltså så att åldder bara kan åtkommas genom en getter eller en setter. Det gör koden mer säker, vem som helst kan ju inte komma åt det. och det blir inte lika enkelt att ändra.

b) Vad händer om man försöker sätta p.alder = -5? (1 p) 
som vi ser i slutet av koden så kommer då den nya åldern få samma value som den hade innan. Värdet kommer alltså vara helt oförändrar.

c) Ge en fördel med att använda property i detta exempel. (2 p)
Gör koden säkrare och mer robust eftersom man inte kan komma åt det hur som helst. Det ser ut som en vanlig attribut.
----------------------------------------------------------------

Uppgift 5 – Arv (5 p)


class Djur:

def lat(self):

print("Djuret låter")


class Hund(Djur):

def lat(self):

print("Voff")


d = Djur()

h = Hund()


d.lat()

h.lat()


a) Vad skrivs ut när koden körs? (2 p) 
Djuret låter
Voff

b) Varför anropas olika metoder trots samma metodnamn? (3 p)
För att man använder sig av polymorfism och överskuggar basklassen i subklassen och får därmed olika värden på samma funktion.
--------------------------------------------------------------
Uppgift 6 – Polymorfism (5 p)


class Fordon:

def beskrivning(self):

return "Ett fordon"


class Bil(Fordon):

def beskrivning(self):

return "En bil"


class Cykel(Fordon):

def beskrivning(self):

return "En cykel"


lista = [Bil(), Cykel(), Fordon()]


for f in lista:

print(f.beskrivning())

a) Vad skrivs ut? (3 p) 
En bil En cykel Ett fordon

b) Varför fungerar detta trots att listan innehåller olika typer av objekt? (2 p)
Eftersom att vi använder oss av polymorfism så kan basklassen samt de två subklasser ha samma funktion/namn på funktionen. Eftersom de alla har har samma funktion så kan de därför användas i en lista och printas ut som olika objekt. 
