# =============================================================================
#  FUNKTIONEN IN PYTHON – Von Null erklärt für Quereinsteiger
# =============================================================================
#
#  Was ist eine Funktion überhaupt?
#  ---------------------------------
#  Stell dir vor du machst jeden Morgen Kaffee. Immer dieselben Schritte.
#  Statt die Schritte jeden Tag neu aufzuschreiben, packst du sie einmal
#  in eine "Kaffeemaschine" – drückst auf den Knopf, fertig.
#
#  Genau das macht eine Funktion im Code:
#  Einmal schreiben → beliebig oft aufrufen → kein Copy-Paste-Chaos.
#
# =============================================================================
#  AUFBAU einer Funktion
# =============================================================================
#
#  def  name  (parameter):
#  │    │      │
#  │    │      └─ Eingabe(n) – was die Funktion braucht (optional)
#  │    └─ frei wählbarer Name (wie Variablennamen)
#  └─ Keyword = "define" → Funktion definieren
#
#       [eingerückter Block] ← Körper der Funktion (4 Leerzeichen oder Tab)
#       return ergebnis      ← Ausgabe zurückgeben (optional)
#
# =============================================================================


# =============================================================================
#  1. EINFACHSTE FUNKTION – ohne Parameter, ohne return
# =============================================================================

def hallo():
    print("Hallo Welt!")       # Funktion tut was, gibt aber nichts zurück

hallo()                        # -> Hallo Welt!
hallo()                        # -> Hallo Welt!   (beliebig oft aufrufbar)


# =============================================================================
#  2. FUNKTION MIT PARAMETER – sie bekommt etwas zum Verarbeiten
# =============================================================================
#
#  Parameter = Platzhalter für Werte die beim Aufruf übergeben werden.
#  Erst beim Aufruf kriegt der Platzhalter einen echten Wert (Argument).

def begrüße(name):             # "name" ist der Platzhalter (Parameter)
    print("Hallo " + name + "!")

begrüße("Tim")                 # -> Hallo Tim!      ("Tim" ist das Argument)
begrüße("Alter")               # -> Hallo Alter!


# =============================================================================
#  3. FUNKTION MIT RETURN – sie gibt ein Ergebnis zurück
# =============================================================================
#
#  Ohne return: Funktion macht was, aber man kann das Ergebnis nicht nutzen.
#  Mit return:  Ergebnis wird zurückgegeben → kann gespeichert oder direkt
#               genutzt werden.

def addiere(a, b):
    ergebnis = a + b
    return ergebnis            # Ergebnis rausgeben

summe = addiere(3, 5)          # Rückgabe in Variable speichern
print(summe)                   # -> 8

print(addiere(10, 20))         # Direkt nutzen ohne Variable -> 30


# -- Was passiert OHNE return? --

def addiere_ohne_return(a, b):
    _ = a + b                  # wird berechnet, aber verschwunden danach

print(addiere_ohne_return(3, 5))  # -> None   (Python gibt "nichts" zurück)


# =============================================================================
#  4. MEHRERE PARAMETER – Reihenfolge ist wichtig
# =============================================================================

def beschreibe_person(name, alter, stadt):
    print(name + " ist " + str(alter) + " Jahre alt und wohnt in " + stadt)

beschreibe_person("Tim", 37, "Wilhelmshaven")
# -> Tim ist 37 Jahre alt und wohnt in Wilhelmshaven

# FALSCH – Reihenfolge durcheinander: alter=Tim, name=37 → Chaos
# beschreibe_person(37, "Tim", "Wilhelmshaven")


# =============================================================================
#  5. KEYWORD-ARGUMENTE – Reihenfolge egal, Name entscheidet
# =============================================================================
#
#  Statt Reihenfolge zu merken → Parameter per Name ansprechen.

beschreibe_person(alter=37, stadt="Wilhelmshaven", name="Tim")
# -> Tim ist 37 Jahre alt und wohnt in Wilhelmshaven  ✓ (Reihenfolge egal)


# =============================================================================
#  6. DEFAULT-WERTE – Parameter mit Fallback
# =============================================================================
#
#  Wenn beim Aufruf kein Wert übergeben wird → nimmt der Default-Wert.

def begrüße_mit_titel(name, titel="Herr"):   # titel hat Default "Herr"
    print("Hallo " + titel + " " + name)

begrüße_mit_titel("Klein")                   # -> Hallo Herr Klein
begrüße_mit_titel("Klein", "Dr.")            # -> Hallo Dr. Klein  (überschrieben)


# =============================================================================
#  7. MEHRERE RÜCKGABEWERTE – return kann mehr als einen Wert liefern
# =============================================================================
#
#  Python gibt dann ein Tuple zurück (mehrere Werte gepackt).

def min_und_max(zahlen):
    return min(zahlen), max(zahlen)   # zwei Werte zurück

kleinste, größte = min_und_max([4, 1, 9, 2, 7])
print(kleinste)    # -> 1
print(größte)      # -> 9


# =============================================================================
#  8. DOCSTRING – Funktion dokumentieren
# =============================================================================
#
#  Direkt nach def-Zeile: dreifache Anführungszeichen → Beschreibung.
#  Kein Kommentar für Außenstehende, sondern offiziell abrufbare Doku.

def multipliziere(a, b):
    """
    Multipliziert zwei Zahlen und gibt das Ergebnis zurück.
    a: erste Zahl
    b: zweite Zahl
    """
    return a * b

print(multipliziere(4, 5))         # -> 20
print(multipliziere.__doc__)       # Zeigt den Docstring an


# =============================================================================
#  9. LOKALE vs. GLOBALE VARIABLEN – Scope (Gültigkeitsbereich)
# =============================================================================
#
#  Variablen IN einer Funktion existieren NUR in dieser Funktion.
#  Von außen nicht sichtbar → "lokal".
#  Variablen außerhalb → "global" → überall lesbar (aber aufpassen!).

zahl = 100          # global

def zeige_lokal():
    lokale_zahl = 42        # nur innerhalb der Funktion
    print(lokale_zahl)      # -> 42

zeige_lokal()
print(zahl)                 # -> 100  (global, kein Problem)
# print(lokale_zahl)        # -> NameError: nicht definiert außerhalb!


# =============================================================================
#  10. FUNKTIONEN IN FUNKTIONEN aufrufen
# =============================================================================
#
#  Funktionen können andere Funktionen aufrufen → Bausteine kombinieren.

def berechne_mwst(netto):
    return netto * 0.19

def gesamtpreis(netto):
    mwst = berechne_mwst(netto)    # andere Funktion aufrufen
    return netto + mwst

print(gesamtpreis(100))   # -> 119.0
print(gesamtpreis(50))    # ->  59.5


# =============================================================================
#  ZUSAMMENFASSUNG
# =============================================================================
#
#  def name(parameter):     ← Funktion definieren
#      [Code]               ← Körper (eingerückt)
#      return ergebnis      ← optional: Ergebnis zurückgeben
#
#  name(argument)           ← Funktion aufrufen
#
#  Parameter  = Platzhalter in der Definition
#  Argument   = echter Wert beim Aufruf
#  return     = Rückgabe (ohne return → None)
#  Scope      = lokal (in Funktion) vs. global (außerhalb)
#  Default    = Fallback-Wert wenn kein Argument übergeben
#  Docstring  = dreifache Anführungszeichen direkt nach def
#
# =============================================================================
