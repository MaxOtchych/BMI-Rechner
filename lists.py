# Hier werden Variablen erstellt, die jewaeils den Namen eines Teilnehmers speichern
# jeder Variable enthält einen String 
teilnehmer_1 = "Max"
teilnehmer_2 = "Anna"
teilnehmer_3 = "Erik"
teilnehmer_4 = "Monika"
teilnehmer_5 = "Laura"

# Eine Liste (teilnehmer_K16) wird erstellt, die die Namen der Teilnehmer enthält
teilnehmer_K16 = ["Max", "Anna", "Erik", "Monika", "Laura"]
print(teilnehmer_K16) # gibt die Liste der Teilnehmer aus
teilnehmer_K16.pop() # pop() entfernt das letzte Element der Liste
print(teilnehmer_K16)

# Bestimmtes Element entfernen
# pop(3) entfernt das Element an Index 3 (in Python beginnt die Zählung bei 0, also ist das Elemenz Monika)
p = teilnehmer_K16.pop(3) # pop() gibt das entfernte Element zurück
print(p) # Das entfernte Element wird in der Variablen p geschpeichert und ausgegeben.


# Länge der Liste mit len().
eilnehmer_K16 = ["Max", "Anna", "Erik", "Monika", "Laura"]
print(len(teilnehmer_K16)) # len() gibt die Anzahl der Elemente in der Liste zurück
teilnehmer_K16.append("Hans") # append() fügt ein Element am Ende der Liste hinzu
neue_teilnehmer = ["Lena", "Peter", "Klaus"]
teilnehmer_K16.extend(neue_teilnehmer) # extend() fügt eine Liste am Ende der Liste hinzu
print(teilnehmer_K16)


# Auf Elemente der  Liste zugreifen
print(teilnehmer_K16[0]) # gibt das ertse Element der Liste zurück ("Max")
print(teilnehmer_K16[5]) # gibt das 6. Element der Liste zurück ("Hans")

# Teile der Liste ausgeben (slicing)
print(teilnehmer_K16[0:3]) # gibt die Elemente 0 bis 2 zurück
print(teilnehmer_K16[:2]) # gibt die Elemente 0 bis 1 zurück
print(teilnehmer_K16[0:4:1])# start:stop und step

'''Zusammenfassung des Codes
1. Listen werde verwendet, um mehrere Werte in einer Variablen zu speichern.
2. Methoden wie pop(), append(), extend(), und len() ermöglichen es, Listen zu manipulieren und Information über sie zu erhalten.
3. Slicing ([start:stop:step]) ermöglicht es, Teile einer Liste auszugeben.
4. Lndizes beginnen bei 0.'''


##############################
#### Python_Listen ####

# len() zegt die Anzahl der Elemente in einer Liste an
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist)) # zeigt die Anzahl der Elemente.


#type() gibt den Typ einer Variablen zurück
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # gibt den Typ der Variable mylist zurück

# list() - Konstruktor
thislist = list(("apple", "banana", "cherry")) # doppelte Klammern
print(thislist)

'''Zusammenfassung des Codes
1. list() wird verwendet, um eine neue Liste zu erstellen.
2. len() gibt die Anzahl der Elemente in einer Liste an.
3. type() gibt den Typ einer Variablen zurück.
'''

###############################
#### Zugriff auf Elemente ####

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # gibt das 2. Element der Liste zurück ("banana")

# Negative Indizes, bedeutet , von Ende anzufangen
thislist = ["apple", "nanana", "cherry"]
print(thislist[-1]) # gibt das letzte Element der Liste zurück ("cherry")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print(thislist[2:5]) 

##################################
#### Elemente ändern ####

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # gibt ["apple", "blackcurrant", "watermelon"] zurück 


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # gibt ["apple", "watermelon"] zurück

############################################
#### Elemente hinzufügen: insert() ####
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # gibt ["apple", "banana", "watermelon", "cherry"] zurück   

############################################
#### Elemente anhängen: append() ####
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # fügt "orange" am Ende der Liste hinzu
print(thislist) 

#Elemente einfügen: insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # fügt "orange" an Index 1 hinzu
print(thislist)

### Liste erweitern: extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #  fügt die Liste tropical am Ende der Liste hinzu
print(thislist) # gibt ["apple", "banana", "cherry", "mango", "pineapple", "papaya"] zurück

###########################
### Python-Listenelemente entfernen ###

#angegebenes Element entfernen: remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # entfernt "banana" aus der Liste
print(thislist)

#angegebenen Index entfernen: pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # entfernt das Element an Index 1 ("banana")
print(thislist)
#Wenn Sie den Index nicht angeben, entfernt die Methode das letzte Element.pop()

# Das Schlüsselwort entfernt auch die angegebene Index: del
thislist = ["apple", "banana", "cherry"]
del thislist[0] # entfernt das Element an Index 0 ("apple")
print(thislist)

#Mit dem Keyword kann die Liste auch komplett gelöscht werden.del
thislist = ["apple", "banana", "cherry"]
del thislist # löscht die Liste komplett

# Löschen Sie die Liste: clear()
# Die Liste ist immer noch vorhande, aver sie hat keinen Inhalt
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

############################################
### Schleifen_Listen ###
#Durchlaufen einer Liste in einer Schleife: for : Schleifen (for) sind nützlich, um über Listen zu iterieren und jeden Eintrag zu verarbeiten oder auszugeben.
thislist = ["apple", "banana", "cherry"]
for x in thislist:# Eine Schleife, die jeden Eintrag in der Liste duchläuft.
    print(x) # Gibt jedes Element der Lister aus.


#Durchlaufen Sie die Indexnummern in einer Schleife:
#Verwenden Sie die range() und len() Funktionen, um ein geeignetes Iterable zu erstellen.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): # gibt die Indexnummern der Liste aus
    print(thislist[i])

#Verwenden eine While-Schleife: while, len()
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Schleife mit Listenverständnis: for
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # gibt jedes Element der Liste aus

######################################################
###Python - Listenverständnis ###
#Listenverständns 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:# gibt jedes Element der Liste aus
    if "a" in x:
        newlist.append(x)
        
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Die Bedingung ist wie ein Filter, der nur die Elemente akzeptiert, die als ausgewertet werden.True

#Akzeptiren Sie nur Artikel, die nicht "apple" sind:
newlist = [x for x in fruits if x != "apple"] # gibt ["banana", "cherry", "kiwi", "mango"] zurück

newlist = [x for x in fruits] # kopiert die Liste

# Iterierbar 
newlist = [x for x in range(10)] # gibt [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] zurück


######################################################
### Liste aiphanumerisch sortieren ###
# Liste-Objekte verfügen über eine Methode, die die Liste standardmäßig alphanumerisch aufsteigend sortiert: sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()# sortiert die Liste alphanumerisch aufsteigend
print(thislist)

#Sortieren Sie die Liste numerisch:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Absteigend sortieren: reverse=True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)# sortiert die Liste alphanumerisch absteigend
print(thislist)

#Sortieren Sie die Liste absteigend:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

######################################################
### Liste kopieren ###
#Verwenden Sie die copy() -Methode

#erstellen Sie eine Kopie einer Liste der folgenden Mrthode: copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()# kopiert die Liste
print(mylist)

#Verwenden Sie die Methode list() Konstruktor
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) # kopiert die Liste
print(mylist)

#Vervenden  des Slice-Operators
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] # kopiert die Liste
print(mylist)

######################################################
### Zweil Listen beitreten ###

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 # fügt list2 an list1 an
print(list3)

#Variant zwei
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x) # fügt jedes Element von list2 an list1 an
    
print(list1)

#Verwenden Sie die Methode, um list2 am Ende von list1 hinzuzufügen:extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2) # fügt list2 am Ende von list1 hinzu
print(list1)

######################################################
##List-Methode 