# =============================================================================
# PYTHON GRUNDLAGEN – Von Null auf "ich check das" (für Quereinsteiger)
# =============================================================================



# =============================================================================
# KAPITEL 1: Was ist Python überhaupt?
# =============================================================================
# Python ist eine Programmiersprache. Du schreibst Anweisungen als Text,
# Python liest sie von oben nach unten und führt sie aus.
#
# Python ist:
# - Interpretiert: Code wird direkt ausgeführt, nicht zuerst kompiliert
# - Dynamisch getypt: Du musst nicht sagen "das ist eine Zahl", Python checkt das selbst
# - Einrückungsbasiert: Blöcke werden durch Leerzeichen definiert, nicht durch {}
#
# Das hier ist dein erstes Programm. Revolutionär, ich weiß:

print("Hallo Welt")

# print() ist eine Funktion. Sie nimmt was du ihr gibst und zeigt es im Terminal an.
# Die Klammern () bedeuten: "ruf die Funktion auf".
# Was in den Klammern steht nennt man Argument.


# =============================================================================
# KAPITEL 2: Kommentare
# =============================================================================
# Alles hinter einem # ist ein Kommentar. Python ignoriert das komplett.
# Kommentare sind für Menschen, nicht für den Computer.

# Das hier ist ein einzeiliger Kommentar

"""
Das hier ist ein mehrzeiliger Kommentar (technisch gesehen ein String,
aber wird genauso benutzt wenn man viel zu sagen hat).
Nützlich für längere Erklärungen oder wenn man vorübergehend
Code auskommentieren will.
"""

# Schreib Kommentare fürs WARUM, nicht fürs WAS.
# Schlecht: x = x + 1  # x um 1 erhöhen   (sieht man doch)
# Gut:      x = x + 1  # Offset wegen nullbasierter Indexierung


# =============================================================================
# KAPITEL 3: Variablen
# =============================================================================
# Eine Variable ist ein benannter Speicherplatz für einen Wert.
# Stell dir vor: ein Zettel mit Name drauf, auf dem ein Wert steht.
# Du kannst den Wert jederzeit lesen oder überschreiben.

name = "Tim"        # Zettel "name" enthält den Text "Tim"
alter = 36          # Zettel "alter" enthält die Zahl 36
groesse = 1.80      # Zettel "groesse" enthält die Kommazahl 1.80
ist_schueler = True  # Zettel "ist_schueler" enthält Ja/Nein-Wert

# Das = ist kein Gleichheitszeichen wie in Mathe.
# Es heißt: "weise rechts dem linken Namen zu".
# name = "Tim"  →  "Der Name 'name' soll ab jetzt 'Tim' sein"

print(name)         # Tim
print(alter)        # 36

# Variablen können überschrieben werden:
alter = 38
print(alter)        # 38  ← der alte Wert ist weg

# Regeln für Variablennamen:
# ✓  klein_mit_unterstrich    (Python-Konvention: snake_case)
# ✓  buchstaben_und_123       (Zahlen im Namen OK, nur nicht am Anfang)
# ✗  1name                   (darf nicht mit Zahl beginnen)
# ✗  mein-name                (Bindestrich = Minus-Operator)
# ✗  class, if, for, while    (reservierte Schlüsselwörter)

# Sprechende Namen sind Pflicht:
# Gut:   punkte_gesamt = 100
# Mies:  p = 100  (was ist p???)
# Mies:  x1 = 100 (noch schlimmer)


# =============================================================================
# KAPITEL 4: Datentypen
# =============================================================================
# Python hat verschiedene Typen für verschiedene Arten von Daten.
# Du musst den Typ nicht angeben – Python erkennt ihn automatisch.
# Mit type() kannst du nachschauen was Python denkt.

print("\n--- Datentypen ---")

# --- int (Integer = Ganzzahl) ---
punkte = 42
jahr = 2026
negativ = -5
print(type(punkte))   # <class 'int'>
print(punkte)         # 42

# --- float (Fließkommazahl) ---
# WICHTIG: In Python (und fast allen Sprachen) ist der Dezimaltrenner ein PUNKT, kein Komma
preis = 9.99
temperatur = -3.5
pi_wert = 3.14159
print(type(preis))    # <class 'float'>

# --- str (String = Zeichenkette = Text) ---
# Strings stehen in einfachen oder doppelten Anführungszeichen
vorname = "Tim"
nachname = 'Klein'
satz = "Ich lerne Python"
print(type(vorname))  # <class 'str'>

# Strings können mit + zusammengefügt werden (Konkatenation):
voller_name = vorname + " " + nachname
print(voller_name)    # Tim Klein

# Wichtig: "3" + "5" = "35"  (Textverkettung)
#              3  +  5  = 8   (Mathematik)
print("3" + "5")   # 35
print(3 + 5)       # 8

# --- bool (Boolean = Wahrheitswert) ---
# Nur zwei mögliche Werte: True oder False (Großschreibung wichtig!)
ist_online = True
hat_fehler = False
print(type(ist_online))  # <class 'bool'>

# Boolean ist im Grunde Binär: True = 1, False = 0
print(True + True)   # 2  (ja, das geht)
print(True + False)  # 1

# --- None (kein Wert / nichts) ---
# None bedeutet "es gibt keinen Wert" – ähnlich wie null in anderen Sprachen
ergebnis = None
print(type(ergebnis))  # <class 'NoneType'>
print(ergebnis)        # None


# =============================================================================
# KAPITEL 5: Typkonvertierung (Casting)
# =============================================================================
# Manchmal muss man Typen umwandeln. Zum Beispiel kommt input() immer als String.

print("\n--- Typkonvertierung ---")

# Umwandlungsfunktionen:
# int()    → macht eine Ganzzahl draus
# float()  → macht eine Kommazahl draus
# str()    → macht einen String draus
# bool()   → macht einen Boolean draus

zahl_als_text = "42"
zahl_als_int = int(zahl_als_text)
print(type(zahl_als_int), zahl_als_int)   # <class 'int'> 42

kommazahl = float("3.14")
print(type(kommazahl), kommazahl)         # <class 'float'> 3.14

# Achtung – das geht NICHT:
# int("hallo")   → ValueError: keine Zahl im String

# Was bool() aus verschiedenen Dingen macht:
print(bool(0))       # False  (0 ist immer False)
print(bool(1))       # True   (alles außer 0 ist True)
print(bool(""))      # False  (leerer String ist False)
print(bool("Tim"))   # True   (nichtleerer String ist True)
print(bool(None))    # False  (None ist immer False)


# =============================================================================
# KAPITEL 6: Ausgabe mit print()
# =============================================================================

print("\n--- Ausgabe ---")

# Einfache Ausgaben:
print("Hallo")           # Text
print(42)                # Zahl
print(True)              # Boolean
print(name)              # Variable

# Mehrere Sachen auf einmal (durch Komma getrennt, print fügt Leerzeichen ein):
print("Name:", name, "Alter:", alter)   # Name: Tim Alter: 38

# \n = neue Zeile innerhalb eines Strings:
print("Zeile 1\nZeile 2\nZeile 3")

# \t = Tabulator:
print("Spalte1\tSpalte2\tSpalte3")

# end="" verhindert den automatischen Zeilenumbruch von print:
print("A", end="")
print("B", end="")
print("C")   # ergibt: ABC

# sep= ändert das Trennzeichen zwischen Argumenten (Standard: " "):
print("2026", "05", "11", sep="-")   # 2026-05-11


# =============================================================================
# KAPITEL 7: f-Strings (der beste Weg Text zu bauen)
# =============================================================================

print("\n--- f-Strings ---")

# f-Strings = formatierte Strings. Ein f vor dem Anführungszeichen,
# dann kannst du mit {} direkt Variablen und Ausdrücke reinschreiben.

alter = 36
print(f"Ich bin {vorname}, {alter} Jahre alt.")
# → Ich bin Tim, 36 Jahre alt.

# Du kannst auch Berechnungen direkt reinschreiben:
print(f"In 10 Jahren bin ich {alter + 10} Jahre alt.")

# Formatierung von Zahlen:
pi_val = 3.14159265
print(f"Pi auf 2 Stellen: {pi_val:.2f}")    # 3.14   (.2f = 2 Nachkommastellen)
print(f"Pi auf 4 Stellen: {pi_val:.4f}")    # 3.1416

# Mehrzeilige f-Strings mit dreifachen Anführungszeichen:
print(f"""
Zusammenfassung:
  Name:    {vorname}
  Alter:   {alter}
  Größe:   {groesse:.2f} m
""")


# =============================================================================
# KAPITEL 8: Eingabe mit input()
# =============================================================================

print("\n--- Eingabe ---")

# input() wartet auf Tastatureingabe und gibt sie als String zurück.
# IMMER als String – auch wenn der User "42" eintippt.

# Im Script auskommentiert damit das nicht bei jedem Ausführen nach Input fragt.
# Zum Testen die # entfernen.

# eingabe = input("Wie heißt du? ")
# print(f"Hallo {eingabe}!")

# Wenn du eine Zahl brauchst, musst du konvertieren:
# alter_eingabe = int(input("Wie alt bist du? "))
# print(f"In 10 Jahren bist du {alter_eingabe + 10}.")


# =============================================================================
# KAPITEL 9: Operatoren
# =============================================================================

print("\n--- Operatoren ---")

# --- Arithmetische Operatoren ---
a = 10
b = 3

print(a + b)    # 13   Addition
print(a - b)    # 7    Subtraktion
print(a * b)    # 30   Multiplikation
print(a / b)    # 3.333... Division (gibt IMMER float zurück)
print(a // b)   # 3    Ganzzahldivision (Ergebnis ohne Rest, rundet ab)
print(a % b)    # 1    Modulo (Rest bei Ganzzahldivision)
print(a ** b)   # 1000 Potenz (10 hoch 3)

# Modulo-Trick: gerade/ungerade Zahlen prüfen
zahl = 7
print(zahl % 2)   # 1 → ungerade (Rest 1 bei Division durch 2)
zahl = 8
print(zahl % 2)   # 0 → gerade (kein Rest)

# --- Vergleichsoperatoren ---
# Geben immer True oder False zurück
x = 5
y = 10

print(x == y)   # False  (gleich?)
print(x != y)   # True   (ungleich?)
print(x < y)    # True   (kleiner als?)
print(x > y)    # False  (größer als?)
print(x <= y)   # True   (kleiner gleich?)
print(x >= y)   # False  (größer gleich?)

# ACHTUNG: = ist Zuweisung, == ist Vergleich
# x = 5   → x bekommt den Wert 5
# x == 5  → ist x gleich 5? (gibt True/False zurück)

# --- Logische Operatoren ---
# and: beide Bedingungen müssen True sein
print(True and True)    # True
print(True and False)   # False

# or: mindestens eine Bedingung muss True sein
print(True or False)    # True
print(False or False)   # False

# not: dreht den Wert um
print(not True)    # False
print(not False)   # True

# Praxisbeispiel:
alter_check = 20
hat_ausweis = True
darf_rein = alter_check >= 18 and hat_ausweis
print(f"Darf rein: {darf_rein}")   # True

# --- Zuweisungsoperatoren (Kurzschreibweisen) ---
punkte = 100
punkte += 10    # punkte = punkte + 10  → 110
punkte -= 5     # punkte = punkte - 5   → 105
punkte *= 2     # punkte = punkte * 2   → 210
punkte //= 3    # punkte = punkte // 3  → 70
print(punkte)   # 70


# =============================================================================
# KAPITEL 10: Bedingungen (if / elif / else)
# =============================================================================

print("\n--- Bedingungen ---")

# if prüft eine Bedingung. Ist sie True, wird der eingerückte Block ausgeführt.
# Die Einrückung (4 Leerzeichen oder 1 Tab) ist in Python PFLICHT – kein {}!

temp = 22

if temp > 30:
    print("Es ist heiß")         # wird ausgeführt wenn temp > 30
elif temp > 20:
    print("Es ist angenehm")     # wird ausgeführt wenn 20 < temp <= 30
elif temp > 10:
    print("Es ist kühl")         # wird ausgeführt wenn 10 < temp <= 20
else:
    print("Es ist kalt")         # wird ausgeführt wenn temp <= 10

# Bei temp = 22 kommt: "Es ist angenehm"
# Python prüft von oben nach unten, stoppt beim ersten True.

# Kurzform (Ternary) für einfache Fälle:
alter_val = 20
status = "volljährig" if alter_val >= 18 else "minderjährig"
print(status)   # volljährig

# Verschachtelte Bedingungen:
note = 2
if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
elif note <= 6:
    print("Schlechter als befriedigend")
else:
    print("Ungültige Note")


# =============================================================================
# KAPITEL 11: Scope (Geltungsbereich von Variablen)
# =============================================================================

print("\n--- Scope ---")

# Variablen die IN einer Funktion definiert werden, leben nur IN dieser Funktion.
# Von außen nicht sichtbar → lokaler Scope.
# Variablen außerhalb von Funktionen → globaler Scope.

globale_variable = "ich bin überall sichtbar"


def scope_demo():
    lokale_variable = "ich lebe nur hier"
    print(globale_variable)   # globale Variable lesbar
    print(lokale_variable)    # lokale Variable lesbar


scope_demo()
print(globale_variable)   # funktioniert
# print(lokale_variable)  # NameError: lokale_variable nicht definiert

# Wenn du in einer Funktion eine globale Variable ÄNDERN willst: global keyword
zaehler2 = 0


def erhöhe_zaehler():
    global zaehler2    # sagt Python: ich meine die globale Variable
    zaehler2 += 1


erhöhe_zaehler()
erhöhe_zaehler()
print(zaehler2)   # 2
# In der Praxis: global vermeiden wenn möglich, lieber return nutzen.


# =============================================================================
# KAPITEL 12: String-Methoden
# =============================================================================

print("\n--- String-Methoden ---")

# Strings haben viele eingebaute Methoden. Aufruf: string.methode()

text = "  Hallo Python Welt  "

print(text.upper())          # HALLO PYTHON WELT   (alles groß)
print(text.lower())          # hallo python welt   (alles klein)
print(text.strip())          # "Hallo Python Welt" (Leerzeichen außen weg)
print(text.lstrip())         # links trimmen
print(text.rstrip())         # rechts trimmen
print(text.replace("Python", "Welt"))   # ersetzen

satz2 = "Ich,lerne,Python,in,Wilhelmshaven"
teile = satz2.split(",")           # nach Komma aufteilen → Liste
print(teile)                       # ['Ich', 'lerne', 'Python', 'in', 'Wilhelmshaven']

wieder_zusammen = " ".join(teile)  # Liste mit Leerzeichen verbinden
print(wieder_zusammen)             # Ich lerne Python in Wilhelmshaven

print("python".startswith("py"))   # True
print("python".endswith("on"))     # True
print("python".find("th"))         # 2  (Index wo "th" beginnt, -1 wenn nicht)
print("na" in "Banane")            # True (ist "na" enthalten?)
print(len("Python"))               # 6   (Länge)

# Groß-/Kleinschreibung normalisieren – nützlich für Vergleiche:
user_eingabe = "  HALLO  "
bereinigt = user_eingabe.strip().lower()
print(bereinigt)   # "hallo"


# =============================================================================
# KAPITEL 13: Fehlertypen kennen (damit du nicht ausrastest)
# =============================================================================

print("\n--- Häufige Fehler ---")

# SyntaxError: Du hast Python-Syntax falsch geschrieben
# Beispiel: print("hallo"   ← fehlende Klammer zu)

# NameError: Variable nicht definiert
# Beispiel: print(nicht_vorhanden)  ← wurde nie erstellt

# TypeError: Falscher Datentyp für Operation
# Beispiel: "5" + 5   ← String + Integer geht nicht

# ValueError: Richtiger Typ, aber ungültiger Wert
# Beispiel: int("hallo")  ← kann nicht zu int werden

# IndexError: Index außerhalb der Liste
# Beispiel: [1,2,3][5]   ← Index 5 existiert nicht

# ZeroDivisionError: Division durch 0
# Beispiel: 10 / 0

# Fehlermeldungen immer komplett lesen!
# Letzte Zeile = Was ist passiert
# Zeilen davor = Wo ist es passiert (Traceback)


# =============================================================================
# ZUSAMMENFASSUNG
# =============================================================================
#
# Datentypen:   int, float, str, bool, None
# Ausgabe:      print("text", variable, f"inline {var}")
# Eingabe:      input("Prompt: ")  → immer str, bei Bedarf konvertieren
# Operatoren:   + - * / // % **   ==  !=  <  >  <=  >=   and or not
# Bedingung:    if ... elif ... else ...  (Einrückung ist Pflicht!)
# Scope:        Lokal = nur in Funktion. Global = überall.
# Strings:      .upper()  .lower()  .strip()  .split()  .replace()
#
# Goldene Regel: Fehlermeldung lesen, nicht ignorieren. Sie sagt dir genau
#                was falsch ist. Python ist da ehrlicher als die meisten Menschen.
#
# =============================================================================
