# =============================================================================
# SCHLEIFEN IN PYTHON
# =============================================================================


# =============================================================================
# KAPITEL 1: Was ist eine Schleife und warum brauche ich die?
# =============================================================================
# Eine Schleife führt denselben Codeblock mehrfach aus.
# Ohne Schleife – du willst "Hallo" 5x ausgeben:

print("Hallo")
print("Hallo")
print("Hallo")
print("Hallo")
print("Hallo")
print("_____")
# Das ist dumm. Was wenn du es 1000x willst? Oder eine variable Anzahl?
# Mit Schleife:

for _ in range(5):
    print("Hallo")

# Dasselbe Ergebnis, 1 Zeile statt 5. Skaliert auf 1.000.000 ohne Änderung.
# Das ist der Punkt.


# =============================================================================
# KAPITEL 2: Die for-Schleife
# =============================================================================
# for geht durch eine Sequenz (Liste, String, range, ...) und führt für
# jedes Element den eingerückten Block aus.
#
# Syntax:
#   for VARIABLE in SEQUENZ:
#       BLOCK
#
# VARIABLE bekommt bei jeder Runde den aktuellen Wert aus der Sequenz.
# BLOCK wird für jedes Element einmal ausgeführt.
# Einrückung (4 Leerzeichen) ist Pflicht – kein {}!

print("\n--- for durch eine Liste ---")

namen = ["Tim", "Laura", "Markus", "Sandra"]

for name in namen:
    print(f"Hallo {name}!")

# Was Python intern macht:
# Runde 1: name = "Tim"    → print("Hallo Tim!")
# Runde 2: name = "Laura"  → print("Hallo Laura!")
# Runde 3: name = "Markus" → print("Hallo Markus!")
# Runde 4: name = "Sandra" → print("Hallo Sandra!")
# Sequenz leer → Schleife fertig

print("\n--- for durch einen String ---")

# Strings sind auch Sequenzen – aus Einzelzeichen
wort = "Python"
for buchstabe in wort:
    print(buchstabe, end=" ")   # P y t h o n
print()  # neue Zeile nach der Ausgabe

# Jedes Zeichen des Strings wird einzeln übergeben.

print("\n--- for durch eine Zahlensequenz mit range() ---")

# range() erzeugt eine Folge von Zahlen ohne sie alle im Speicher zu halten.

# range(stop)             → 0, 1, 2, ..., stop-1
# range(start, stop)      → start, start+1, ..., stop-1
# range(start, stop, step)→ start, start+step, ..., solange < stop

for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4
print()

for i in range(1, 6):
    print(i, end=" ")   # 1 2 3 4 5
print()

for i in range(0, 11, 2):
    print(i, end=" ")   # 0 2 4 6 8 10  (Schrittweite 2)
print()

for i in range(10, 0, -1):
    print(i, end=" ")   # 10 9 8 7 6 5 4 3 2 1  (rückwärts)
print()

# Merke: stop ist IMMER ausgeschlossen. range(1, 6) gibt 1,2,3,4,5 – NICHT 6.

print("\n--- Schleifenvariable ignorieren mit _ ---")

# Wenn du den Wert in der Schleife nicht brauchst, Konvention: _ statt i
for _ in range(3):
    print("Das passiert 3 mal, der Zähler ist mir egal")


# =============================================================================
# KAPITEL 3: enumerate() – Index UND Wert gleichzeitig
# =============================================================================

print("\n--- enumerate() ---")

# Oft brauchst du beim Durchlaufen einer Liste sowohl den Wert als auch
# den Index. enumerate() liefert beides.

fruechte = ["Apfel", "Banane", "Kirsche", "Mango"]

# Ohne enumerate – umständlich:
for i in range(len(fruechte)):
    print(f"{i}: {fruechte[i]}")

print()

# Mit enumerate – sauber:
for index, frucht in enumerate(fruechte):
    print(f"{index}: {frucht}")

# Ausgabe jeweils:
# 0: Apfel
# 1: Banane
# 2: Kirsche
# 3: Mango

# enumerate() kann auch bei einem anderen Index starten:
for index, frucht in enumerate(fruechte, start=1):
    print(f"Platz {index}: {frucht}")

# 1: Apfel, 2: Banane, ...


# =============================================================================
# KAPITEL 4: zip() – zwei Listen gleichzeitig durchlaufen
# =============================================================================

print("\n--- zip() ---")

# zip() kombiniert zwei (oder mehr) Listen und gibt Paare zurück.
# Hört auf wenn die kürzeste Liste leer ist.

vornamen = ["Tim",   "Laura", "Markus"]
noten    = [2,       1,       3      ]

for person, note in zip(vornamen, noten):
    print(f"{person} hat eine {note}")

# Tim hat eine 2
# Laura hat eine 1
# Markus hat eine 3


# =============================================================================
# KAPITEL 5: Die while-Schleife
# =============================================================================
# while läuft solange eine Bedingung True ist.
# Nützlich wenn du NICHT weißt wie viele Runden nötig sind.
#
# Syntax:
#   while BEDINGUNG:
#       BLOCK
#
# BEDINGUNG wird vor jeder Runde geprüft.
# Ist sie False → Schleife endet.
# Ist sie nie False → Endlosschleife → Programm hängt.

print("\n--- while Grundform ---")

zaehler = 0
while zaehler < 5:
    print(f"Zaehler ist {zaehler}")
    zaehler += 1   # PFLICHT: Bedingung muss irgendwann False werden!

# Was Python macht:
# Prüfe: 0 < 5? Ja → Block ausführen → zaehler = 1
# Prüfe: 1 < 5? Ja → Block ausführen → zaehler = 2
# Prüfe: 2 < 5? Ja → Block ausführen → zaehler = 3
# Prüfe: 3 < 5? Ja → Block ausführen → zaehler = 4
# Prüfe: 4 < 5? Ja → Block ausführen → zaehler = 5
# Prüfe: 5 < 5? NEIN → Schleife fertig

print("\n--- while mit unbekannter Anzahl Runden ---")

# Klassischer Anwendungsfall: auf gültige Eingabe warten
# (hier simuliert ohne echten input)

geheimzahl = 42
raten = 0
tipp = 0  # simulierter Start-Tipp

# Simulierte Tipps (würden normalerweise per input() kommen)
tipps = [10, 99, 42]  # dritter Tipp ist richtig
versuch_index = 0

while tipp != geheimzahl:
    tipp = tipps[versuch_index]
    versuch_index += 1
    raten += 1
    if tipp != geheimzahl:
        print(f"Falsch ({tipp}), weiter raten...")
    else:
        print(f"Richtig! Gebraucht: {raten} Versuche")

print("\n--- GEFAHR: Endlosschleife ---")
# Das hier würde für immer laufen – NICHT ausführen:
#
# while True:
#     print("Hallo")   # läuft bis Strg+C oder Prozess stirbt
#
# while True ist manchmal aber auch GEWOLLT, mit break zum Beenden (→ Kapitel 6)


# =============================================================================
# KAPITEL 6: break – Schleife sofort beenden
# =============================================================================

print("\n--- break ---")

# break verlässt die Schleife sofort, egal wie viele Runden noch kommen würden.

for i in range(10):
    if i == 5:
        print(f"Stopp bei {i}!")
        break
    print(i, end=" ")   # 0 1 2 3 4

print()

# break in while – das ist der saubere Weg eine "Endlosschleife" zu nutzen:
versuche = 0
while True:
    versuche += 1
    if versuche >= 3:
        print(f"Nach {versuche} Versuchen aufgegeben")
        break
    print(f"Versuch {versuche}")

# "Suche nach einem Element" – typisches break-Muster:
daten = [3, 7, 1, 9, 4, 15, 2]
gesucht = 9

for i, wert in enumerate(daten):
    if wert == gesucht:
        print(f"Gefunden: {gesucht} an Index {i}")
        break
else:
    # Das else gehört zur for-Schleife – läuft NUR wenn kein break ausgeführt wurde
    print(f"{gesucht} nicht gefunden")


# =============================================================================
# KAPITEL 7: continue – aktuelle Runde überspringen
# =============================================================================

print("\n--- continue ---")

# continue springt direkt zur nächsten Runde, ohne den Rest des Blocks auszuführen.

# Alle ungeraden Zahlen von 0-9 ausgeben:
for i in range(10):
    if i % 2 == 0:
        continue    # gerade Zahlen überspringen
    print(i, end=" ")  # 1 3 5 7 9
print()

# Leere Einträge in einer Liste ignorieren:
eintraege = ["Tim", "", "Laura", None, "Markus", ""]

for eintrag in eintraege:
    if not eintrag:     # leerer String und None sind beide "falsy"
        continue
    print(eintrag)

# Gibt nur "Tim", "Laura", "Markus" aus


# =============================================================================
# KAPITEL 8: pass – Platzhalter für leeren Block
# =============================================================================

print("\n--- pass ---")

# Python braucht nach : immer mindestens eine Zeile Code (Einrückung).
# pass ist ein "tu-nichts"-Befehl – hält die Syntax gültig.

for i in range(5):
    pass   # Schleife läuft durch, macht aber gar nichts

# Nützlich wenn du den Code noch schreiben willst:
# for eintrag in daten:
#     pass  # TODO: Verarbeitung kommt noch


# =============================================================================
# KAPITEL 9: else bei Schleifen
# =============================================================================

print("\n--- for/while else ---")

# Schleifen haben ein optionales else: – läuft wenn die Schleife
# NORMAL beendet wurde (also OHNE break).

zahlen = [1, 3, 5, 7, 9]
gesucht = 4

for zahl in zahlen:
    if zahl == gesucht:
        print(f"{gesucht} gefunden!")
        break
else:
    print(f"{gesucht} nicht in der Liste")
# Gibt aus: "4 nicht in der Liste"

# Mit vorhandener Zahl:
gesucht = 5
for zahl in zahlen:
    if zahl == gesucht:
        print(f"{gesucht} gefunden!")
        break
else:
    print(f"{gesucht} nicht in der Liste")
# Gibt aus: "5 gefunden!" (kein else, weil break ausgeführt)

# while else funktioniert genauso:
n = 0
while n < 3:
    n += 1
else:
    print(f"while normal beendet, n ist jetzt {n}")


# =============================================================================
# KAPITEL 10: Verschachtelte Schleifen
# =============================================================================

print("\n--- Verschachtelte Schleifen ---")

# Eine Schleife in einer Schleife. Für jede Runde der äußeren
# läuft die innere komplett durch.

for i in range(1, 4):       # äußere: i = 1, 2, 3
    for j in range(1, 4):   # innere: j = 1, 2, 3  (für jedes i)
        print(f"{i}x{j}={i*j}", end="  ")
    print()  # neue Zeile nach jeder Zeile

# Ausgabe:
# 1x1=1  1x2=2  1x3=3
# 2x1=2  2x2=4  2x3=6
# 3x1=3  3x2=6  3x3=9

# Dreieck ausgeben:
print()
for i in range(1, 6):
    print("*" * i)
# *
# **
# ***
# ****
# *****

# break in verschachtelten Schleifen bricht nur die INNERE Schleife:
print()
for i in range(3):
    for j in range(5):
        if j == 3:
            break           # bricht nur die j-Schleife
        print(f"[{i},{j}]", end=" ")
    print()
# [0,0] [0,1] [0,2]
# [1,0] [1,1] [1,2]
# [2,0] [2,1] [2,2]


# =============================================================================
# KAPITEL 11: List Comprehension – Schleifen in einer Zeile
# =============================================================================

print("\n--- List Comprehension ---")

# Kurzschreibweise um eine neue Liste aus einer Schleife zu bauen.
# Sieht komisch aus, ist aber sehr pythonisch und überall anzutreffen.
#
# Syntax: [AUSDRUCK for VARIABLE in SEQUENZ]
# Mit Filter: [AUSDRUCK for VARIABLE in SEQUENZ if BEDINGUNG]

# Normal mit for:
quadrate_lang = []
for i in range(1, 6):
    quadrate_lang.append(i ** 2)
print(quadrate_lang)   # [1, 4, 9, 16, 25]

# Als List Comprehension:
quadrate_kurz = [i ** 2 for i in range(1, 6)]
print(quadrate_kurz)   # [1, 4, 9, 16, 25]

# Mit Bedingung (Filter) – nur gerade Quadrate:
gerade_quadrate = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(gerade_quadrate)   # [4, 16, 36, 64, 100]

# Strings transformieren:
woerter = ["hallo", "WELT", "Python"]
klein = [w.lower() for w in woerter]
print(klein)   # ['hallo', 'welt', 'python']

# Faustregel: Wenn die Comprehension länger als eine Zeile wird → normale Schleife.
# Lesbarkeit schlägt Kürze.


# =============================================================================
# KAPITEL 12: Häufige Muster mit Schleifen
# =============================================================================

print("\n--- Häufige Muster ---")

daten = [4, 7, 2, 9, 1, 5, 8, 3, 6]

# --- Summe berechnen (ohne sum()) ---
gesamt = 0
for zahl in daten:
    gesamt += zahl
print(f"Summe: {gesamt}")   # 45

# --- Maximum finden (ohne max()) ---
groesste = daten[0]   # erster Wert als Startwert
for zahl in daten:
    if zahl > groesste:
        groesste = zahl
print(f"Maximum: {groesste}")   # 9

# --- Elemente filtern (nur bestimmte behalten) ---
grosse_zahlen = []
for zahl in daten:
    if zahl > 5:
        grosse_zahlen.append(zahl)
print(f"Größer als 5: {grosse_zahlen}")   # [7, 9, 8, 6]

# --- Vorkommen zählen ---
werte = [1, 3, 2, 3, 1, 3, 2, 1]
anzahl_dreien = 0
for wert in werte:
    if wert == 3:
        anzahl_dreien += 1
print(f"Anzahl der 3en: {anzahl_dreien}")   # 3

# --- Elemente transformieren (neue Liste mit geänderten Werten) ---
preise = [10.0, 25.0, 8.0, 50.0]
mit_rabatt = []
for preis in preise:
    mit_rabatt.append(preis * 0.9)   # 10% Rabatt
print(f"Rabattpreise: {mit_rabatt}")   # [9.0, 22.5, 7.2, 45.0]

# --- Alle Elemente ausgeben mit Trennlinie ---
kategorien = ["Mathe", "Python", "SQL", "WiSo"]
print("\nKategorien:")
print("-" * 20)
for kategorie in kategorien:
    print(f"  • {kategorie}")
print("-" * 20)


# =============================================================================
# KAPITEL 13: for vs while – wann was?
# =============================================================================
#
# for:  Du weißt wie viele Runden, oder hast eine fertige Sequenz
#       → for i in range(10)
#       → for element in liste
#       → for zeile in datei
#
# while: Du weißt NICHT wie viele Runden – du wartest auf eine Bedingung
#        → while nicht_fertig
#        → while eingabe != "exit"
#        → while verbindung_aktiv
#
# Fast alles was man mit while kann, kann man auch mit for – aber while
# ist klarer wenn die Anzahl der Durchläufe unbekannt ist.


# =============================================================================
# KAPITEL 14: Häufige Fehler
# =============================================================================

print("\n--- Häufige Fehler ---")

# FEHLER 1: Endlosschleife wegen vergessener Änderung der Bedingung
# i = 0
# while i < 5:
#     print(i)
#     # i += 1  ← fehlt! i bleibt 0, Bedingung immer True → hängt

# FEHLER 2: Off-by-One mit range
for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4  ← NICHT 1 2 3 4 5
print()
# Wenn du 1 bis 5 willst: range(1, 6)

# FEHLER 3: Liste während des Iterierens ändern → unvorhersehbares Verhalten
# FALSCH:
zahlen_liste = [1, 2, 3, 4, 5]
# for zahl in zahlen_liste:
#     if zahl % 2 == 0:
#         zahlen_liste.remove(zahl)   # BÖSE – modifiziert Liste während du drüber gehst

# RICHTIG: Kopie iterieren oder neue Liste bauen
zahlen_liste = [1, 2, 3, 4, 5]
ungerade = [z for z in zahlen_liste if z % 2 != 0]
print(ungerade)   # [1, 3, 5]

# FEHLER 4: Einrückung falsch → falsche Logik
# for i in range(5):
#     print(i)
# print("fertig")   # ← außerhalb der Schleife, einmal am Ende (gewollt)
#
# for i in range(5):
#     print(i)
#     print("fertig")   # ← innerhalb der Schleife, 5x ausgegeben (oft ungewollt)

# FEHLER 5: break bricht nur die innerste Schleife
for i in range(3):
    for j in range(3):
        if j == 1:
            break       # bricht NUR die j-Schleife, i läuft weiter
    print(f"i={i} weitergelaufen")


# =============================================================================
# ZUSAMMENFASSUNG
# =============================================================================
#
# for:          für bekannte Sequenzen und Anzahlen
#               for x in liste:  /  for i in range(n):
#
# while:        wenn Anzahl unbekannt, wartet auf Bedingung
#               while bedingung:   ← vergiss nie die Änderung der Bedingung!
#
# break:        Schleife sofort verlassen (nur innerste)
# continue:     Rest der aktuellen Runde überspringen
# pass:         Platzhalter, tut nichts
#
# else:         läuft nach Schleife wenn kein break ausgeführt wurde
#
# enumerate():  Index + Wert gleichzeitig:  for i, x in enumerate(liste)
# zip():        zwei Listen parallel:       for a, b in zip(liste1, liste2)
#
# List Comprehension: [ausdruck for x in seq if bed]  → neue Liste in einer Zeile
#
# Verschachtelt: äußere Schleife × innere Schleife Runden = Gesamtrunden
#                break bricht nur die Schleife in der es steht
#
# for vs while:  Sequenz bekannt → for.  Warten auf Bedingung → while.
#
# =============================================================================
