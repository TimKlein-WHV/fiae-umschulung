# =============================================================================
# PYTHON LISTEN – Erklärung für Quereinsteiger
# =============================================================================
# Was ist eine Liste?
# -------------------
# Stell dir vor, du schreibst einen Einkaufszettel.
# Auf Papier schreibst du:
#   1. Bier
#   2. Chips
#   3. Ibuprofen (für den nächsten Morgen)
#
# In Python sieht das so aus:
einkauf = ["Bier", "Chips", "Ibuprofen"]
#
# Das ist eine Liste. Eine geordnete Sammlung von Werten.
# Die eckigen Klammern [] zeigen Python: "Hey, das ist eine Liste."
# Die Werte darin heißen "Elemente" oder "Items".


# =============================================================================
# LISTEN ERSTELLEN
# =============================================================================

# Leere Liste (noch nix drauf, wie ein leerer Einkaufszettel)
leere_liste = []

# Liste mit Zahlen
zahlen = [1, 2, 3, 4, 5]

# Liste mit Strings (Texten)
namen = ["Anna", "Ben", "Chris"]

# Liste mit gemischten Typen (geht in Python, andere Sprachen fluchen dafür)
gemischt = [42, "Hallo", True, 3.14]

# Liste in einer Variable speichern – immer gleich aufbauen:
#   variablenname = [element1, element2, element3]


# =============================================================================
# AUF ELEMENTE ZUGREIFEN – DER INDEX
# =============================================================================
# Jedes Element hat eine Nummer – den "Index".
# WICHTIG: Python fängt bei 0 an, nicht bei 1!
#
#   ["Bier",  "Chips",  "Ibuprofen"]
#      0         1          2
#
# Das ist wie Stockwerke in einem Fahrstuhl – Erdgeschoss ist 0.

fruechte = ["Apfel", "Banane", "Kirsche", "Mango"]

print(fruechte[0])   # → Apfel   (erstes Element)
print(fruechte[1])   # → Banane  (zweites Element)
print(fruechte[3])   # → Mango   (viertes Element)

# NEGATIVER INDEX – von hinten zählen
print(fruechte[-1])  # → Mango   (letztes Element)
print(fruechte[-2])  # → Kirsche (vorletztes Element)

# Fehler den JEDER macht:
# print(fruechte[4])  → IndexError: list index out of range
# Es gibt nur Index 0–3 bei 4 Elementen. Index 4 existiert nicht.


# =============================================================================
# ELEMENTE ÄNDERN
# =============================================================================
# Liste ist "mutable" – veränderbar. Du kannst Werte überschreiben.

noten = [1, 2, 3, 4, 5]
print(noten)         # → [1, 2, 3, 4, 5]

noten[2] = 6         # Index 2 (das dritte Element) wird zu 6
print(noten)         # → [1, 2, 6, 4, 5]

# Syntax: liste[index] = neuer_wert


# =============================================================================
# ELEMENTE HINZUFÜGEN
# =============================================================================

# .append() – ans ENDE anhängen (der Klassiker)
aufgaben = ["einkaufen", "putzen"]
aufgaben.append("schlafen")
print(aufgaben)  # → ['einkaufen', 'putzen', 'schlafen']

# .insert(index, wert) – an bestimmter POSITION einfügen
aufgaben.insert(1, "kochen")   # einfügen an Index 1
print(aufgaben)  # → ['einkaufen', 'kochen', 'putzen', 'schlafen']

# .extend() – andere Liste ANHÄNGEN (nicht als Element, sondern aufklappen)
mehr_aufgaben = ["sport", "lernen"]
aufgaben.extend(mehr_aufgaben)
print(aufgaben)  # → ['einkaufen', 'kochen', 'putzen', 'schlafen', 'sport', 'lernen']

# Unterschied append vs extend:
test: list = [1, 2, 3]
test.append([4, 5])    # Liste als EIN Element rein → [1, 2, 3, [4, 5]]
test2 = [1, 2, 3]
test2.extend([4, 5])   # Elemente einzeln rein     → [1, 2, 3, 4, 5]


# =============================================================================
# ELEMENTE ENTFERNEN
# =============================================================================

tiere = ["Hund", "Katze", "Vogel", "Fisch"]

# .remove(wert) – entfernt erstes Vorkommen dieses WERTES
tiere.remove("Katze")
print(tiere)  # → ['Hund', 'Vogel', 'Fisch']

# .pop(index) – entfernt Element an INDEX und gibt es zurück
entfernt = tiere.pop(1)   # Index 1 = 'Vogel'
print(entfernt)           # → Vogel
print(tiere)              # → ['Hund', 'Fisch']

# .pop() ohne Index → letztes Element entfernen
letztes = tiere.pop()
print(letztes)  # → Fisch
print(tiere)    # → ['Hund']

# del – löscht direkt (gibt nix zurück)
zahlen2 = [10, 20, 30, 40]
del zahlen2[1]
print(zahlen2)  # → [10, 30, 40]

# .clear() – ALLES löschen
zahlen2.clear()
print(zahlen2)  # → []


# =============================================================================
# LISTE DURCHLAUFEN – FOR-SCHLEIFE
# =============================================================================
# Das Brot-und-Butter der Listenarbeit.

mitglieder = ["Tim", "Jana", "Max", "Sara"]

for person in mitglieder:
    print(f"Hallo, {person}!")
# → Hallo, Tim!
# → Hallo, Jana!
# → Hallo, Max!
# → Hallo, Sara!

# Mit Index – wenn du die Position auch brauchst:
for i, person in enumerate(mitglieder):
    print(f"{i}: {person}")
# → 0: Tim
# → 1: Jana
# → 2: Max
# → 3: Sara


# =============================================================================
# NÜTZLICHE FUNKTIONEN & METHODEN
# =============================================================================

nummern = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(nummern))      # → 8        Anzahl der Elemente
print(min(nummern))      # → 1        kleinster Wert
print(max(nummern))      # → 9        größter Wert
print(sum(nummern))      # → 31       Summe aller Zahlen

# Sortieren
nummern.sort()           # sortiert DIE LISTE selbst (verändert sie!)
print(nummern)           # → [1, 1, 2, 3, 4, 5, 6, 9]

nummern.sort(reverse=True)  # absteigend
print(nummern)           # → [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() – gibt NEUE sortierte Liste zurück, Original bleibt unverändert
original = [5, 2, 8, 1]
neu_sortiert = sorted(original)
print(original)          # → [5, 2, 8, 1]  (unverändert!)
print(neu_sortiert)      # → [1, 2, 5, 8]

# Prüfen ob Element IN Liste ist
print("Apfel" in fruechte)   # → True oder False
print("Pizza" in fruechte)   # → False

# Wie oft kommt ein Wert vor?
buchstaben = ["a", "b", "a", "c", "a"]
print(buchstaben.count("a"))  # → 3

# An welchem Index ist ein Wert?
print(buchstaben.index("b"))  # → 1

# Reihenfolge umkehren
buchstaben.reverse()
print(buchstaben)  # → ['a', 'c', 'a', 'b', 'a']


# =============================================================================
# SLICING – TEILBEREICHE AUSSCHNEIDEN
# =============================================================================
# Syntax: liste[start:stop]  (stop ist NICHT inklusive!)

alphabet = ["a", "b", "c", "d", "e", "f", "g"]

print(alphabet[1:4])   # → ['b', 'c', 'd']  (Index 1 bis 3)
print(alphabet[:3])    # → ['a', 'b', 'c']  (Anfang bis Index 2)
print(alphabet[4:])    # → ['e', 'f', 'g']  (Index 4 bis Ende)
print(alphabet[:])     # → komplette Liste (Kopie)
print(alphabet[::2])   # → ['a', 'c', 'e', 'g']  (jeden 2. nehmen)
print(alphabet[::-1])  # → ['g', 'f', 'e', 'd', 'c', 'b', 'a']  (umgekehrt)


# =============================================================================
# LISTE KOPIEREN – ACHTUNG FALLE!
# =============================================================================
# Das ist der Klassiker, der jeden mal in die Knie zwingt.

original = [1, 2, 3]

# FALSCH – keine echte Kopie, beide zeigen auf DASSELBE Objekt:
kopie_falsch = original
kopie_falsch.append(4)
print(original)      # → [1, 2, 3, 4]  ← ORIGINAL wurde verändert! Scheiße.

# RICHTIG – echte Kopien erstellen:
original2 = [1, 2, 3]

kopie1 = original2.copy()       # Methode
kopie2 = original2[:]           # Slicing
kopie3 = list(original2)        # list()-Funktion

kopie1.append(99)
print(original2)    # → [1, 2, 3]  ← Original bleibt sauber


# =============================================================================
# LIST COMPREHENSION – PYTHON-MAGIE (FORTGESCHRITTEN)
# =============================================================================
# Kurze Schreibweise um neue Listen aus alten zu bauen.

# Normal (lang):
quadrate = []
for x in range(1, 6):
    quadrate.append(x ** 2)
print(quadrate)  # → [1, 4, 9, 16, 25]

# Comprehension (kurz, pythonisch):
quadrate2 = [x ** 2 for x in range(1, 6)]
print(quadrate2)  # → [1, 4, 9, 16, 25]

# Mit Bedingung – nur gerade Zahlen:
gerade = [x for x in range(10) if x % 2 == 0]
print(gerade)  # → [0, 2, 4, 6, 8]

# Syntax: [ausdruck for variable in iterable if bedingung]


# =============================================================================
# ZUSAMMENFASSUNG
# =============================================================================
#
#  Erstellen:         liste = [1, 2, 3]
#  Zugriff:           liste[0]          → erstes Element
#  Ändern:            liste[0] = 99
#  Hinzufügen:        liste.append(x)   → ans Ende
#                     liste.insert(i, x)→ an Position i
#  Entfernen:         liste.remove(x)   → nach Wert
#                     liste.pop(i)      → nach Index
#  Länge:             len(liste)
#  Suchen:            x in liste        → True/False
#                     liste.index(x)    → Index
#  Sortieren:         liste.sort()      → in-place
#                     sorted(liste)     → neue Liste
#  Kopieren:          liste.copy()      → echte Kopie
#  Slice:             liste[1:3]        → Teilbereich
#  Alle löschen:      liste.clear()
#
# =============================================================================
