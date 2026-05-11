# =============================================================================
# 2D-LISTEN IN PYTHON 
# =============================================================================


# -----------------------------------------------------------------------------
# KAPITEL 1: Was ist überhaupt eine Liste?
# -----------------------------------------------------------------------------
# Erstmal Basics, damit wir auf derselben Wellenlänge sind.
#
# Eine normale Liste ist wie eine Einkaufsliste – eine Reihe von Dingen:

einkauf = ["Brot", "Milch", "Käse", "Bier"]

# Du greifst auf einzelne Elemente zu mit dem Index (Zählnummer), die bei 0 anfängt:
#
#   Index:     0       1       2       3
#   Wert:   "Brot"  "Milch" "Käse"  "Bier"
#
# Also:  einkauf[0]  →  "Brot"
#        einkauf[2]  →  "Käse"
#        einkauf[3]  →  "Bier"  (das wichtigste steht am Ende)

print(einkauf[0])  # Brot
print(einkauf[3])  # Bier


# -----------------------------------------------------------------------------
# KAPITEL 2: Was ist eine 2D-Liste?
# -----------------------------------------------------------------------------
# Eine 2D-Liste ist eine Liste, die andere Listen enthält.
# Klingt komisch, macht aber Sinn – versprochen.
#
# Stell dir ein Tabellenblatt vor (wie Excel, nur ohne das Leiden):
#
#         Spalte 0   Spalte 1   Spalte 2
# Zeile 0:    1          2          3
# Zeile 1:    4          5          6
# Zeile 2:    7          8          9
#
# In Python sieht das so aus:

matrix = [
    [1, 2, 3],   # ← Das ist Zeile 0
    [4, 5, 6],   # ← Das ist Zeile 1
    [7, 8, 9]    # ← Das ist Zeile 2
]

# Jede innere Liste ist eine Zeile.
# Die äußere Liste hält alle Zeilen zusammen.


# -----------------------------------------------------------------------------
# KAPITEL 3: Auf Elemente zugreifen
# -----------------------------------------------------------------------------
# Syntax: liste[zeile][spalte]
#
# Erst sagst du WELCHE Zeile, dann WELCHE Spalte.
# Beide Indizes starten bei 0.
#
#              Spalte 0  Spalte 1  Spalte 2
# Zeile 0:       [0][0]    [0][1]    [0][2]
# Zeile 1:       [1][0]    [1][1]    [1][2]
# Zeile 2:       [2][0]    [2][1]    [2][2]

print(matrix[0][0])  # 1  ← oben links
print(matrix[0][2])  # 3  ← oben rechts
print(matrix[1][1])  # 5  ← genau in der Mitte
print(matrix[2][0])  # 7  ← unten links
print(matrix[2][2])  # 9  ← unten rechts

# Eselsbrücke: "Zeile zuerst, dann Spalte" = genau wie Koordinaten lesen,
# nur halt andersrum als in der Schule. Python macht halt manchmal sein eigenes Ding.


# -----------------------------------------------------------------------------
# KAPITEL 4: Einzelne Zeilen auslesen
# -----------------------------------------------------------------------------
# Eine ganze Zeile bekommst du einfach mit dem Zeilen-Index allein:

erste_zeile = matrix[0]
print(erste_zeile)  # [1, 2, 3]

letzte_zeile = matrix[2]
print(letzte_zeile)  # [7, 8, 9]

# Das ist einfach eine normale Liste – du kannst damit alles machen,
# was du mit einer normalen Liste machen kannst.
print(len(matrix[0]))  # 3  ← wie viele Elemente hat Zeile 0?


# -----------------------------------------------------------------------------
# KAPITEL 5: Elemente ändern
# -----------------------------------------------------------------------------
# Genauso wie du zugreifst, kannst du auch überschreiben:

matrix[1][1] = 99  # Die 5 in der Mitte wird zu 99
print(matrix)      # [[1, 2, 3], [4, 99, 6], [7, 8, 9]]

matrix[1][1] = 5   # Zurücksetzen für spätere Beispiele


# -----------------------------------------------------------------------------
# KAPITEL 6: Durch eine 2D-Liste iterieren (verschachtelte Schleifen)
# -----------------------------------------------------------------------------
# Um ALLE Elemente zu durchlaufen brauchst du zwei Schleifen – eine in der anderen.
# Die äußere geht durch die Zeilen, die innere durch die Elemente jeder Zeile.
#
# Schritt für Schritt:
#
# Erste Runde der äußeren Schleife:
#   i = [1, 2, 3]   ← Zeile 0
#   innere Schleife: j = 1, dann j = 2, dann j = 3
#
# Zweite Runde der äußeren Schleife:
#   i = [4, 5, 6]   ← Zeile 1
#   innere Schleife: j = 4, dann j = 5, dann j = 6
#
# usw.

print("\n--- Alle Elemente einzeln ---")
for i in matrix:        # i ist jeweils eine Zeile (eine Liste)
    for j in i:         # j ist jeweils ein Element in dieser Zeile
        print(j)        # gibt 1, 2, 3, 4, 5 ... einzeln aus

# Wenn du lieber die ganze Zeile auf einmal ausgeben willst:
print("\n--- Jede Zeile als Block ---")
for zeile in matrix:
    print(zeile)        # gibt [1, 2, 3], dann [4, 5, 6], dann [7, 8, 9] aus


# -----------------------------------------------------------------------------
# KAPITEL 7: Mit Indizes iterieren (range + len)
# -----------------------------------------------------------------------------
# Manchmal brauchst du die Position (den Index), nicht nur den Wert.
# Zum Beispiel wenn du Elemente ändern oder vergleichen willst.
#
# len(matrix)     → wie viele Zeilen gibt es?       = 3
# len(matrix[0])  → wie viele Spalten in Zeile 0?   = 3

print("\n--- Mit Indizes ---")
for i in range(len(matrix)):           # i = 0, 1, 2  (Zeilen-Index)
    for j in range(len(matrix[i])):    # j = 0, 1, 2  (Spalten-Index)
        print(f"[{i}][{j}] = {matrix[i][j]}")

# Das gibt dir z.B. aus:
# [0][0] = 1
# [0][1] = 2
# [0][2] = 3
# [1][0] = 4  ... usw.

# Diese Methode brauchst du zwingend, wenn du Elemente überschreiben willst!
# Mit "for j in i" kriegst du nur eine Kopie des Wertes – Änderungen gehen verloren.
# Mit "matrix[i][j] = ..." änderst du das Original.


# -----------------------------------------------------------------------------
# KAPITEL 8: 2D-Listen erstellen
# -----------------------------------------------------------------------------

# --- Methode 1: Direkt hinschreiben (für kleine, feste Daten) ---
stundenplan = [
    ["Mathe",   "Deutsch", "Sport"],   # Montag
    ["Python",  "SQL",     "WiSo"],    # Dienstag
    ["Englisch","Chemie",  "Kunst"]    # Mittwoch
]
print(stundenplan[1][1])  # SQL  ← Dienstag, 2. Stunde


# --- Methode 2: Per Schleife befüllen (für dynamische/berechnete Daten) ---
# Beispiel: 3x4-Matrix, alles mit 0 befüllt

zeilen = 3
spalten = 4
nullmatrix = []

for i in range(zeilen):
    neue_zeile = []
    for j in range(spalten):
        neue_zeile.append(0)
    nullmatrix.append(neue_zeile)

print(nullmatrix)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# --- Methode 3: List Comprehension (Kurzschreibweise für Profis) ---
# Das ist dasselbe wie Methode 2, nur in einer Zeile.
# Erst verstehen, dann nutzen – nicht copy-pasten ohne Hirn.

nullmatrix2 = [[0 for _ in range(spalten)] for _ in range(zeilen)]
print(nullmatrix2)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# ACHTUNG – häufiger Anfängerfehler:
# Nie so erstellen: matrix = [[0] * spalten] * zeilen
# Das sieht aus wie es funktioniert, aber alle Zeilen zeigen auf
# DASSELBE Listen-Objekt. Änderst du eine Zeile, änderst du alle.
# Das ist Python's Art, dir einen Streich zu spielen.


# -----------------------------------------------------------------------------
# KAPITEL 9: Zeilen hinzufügen und entfernen
# -----------------------------------------------------------------------------

klasse = [
    ["Tim",    2, 3, 1],
    ["Laura",  1, 2, 2],
    ["Markus", 3, 4, 3]
]

# Neue Zeile hinzufügen (neuer Schüler):
klasse.append(["Sandra", 1, 1, 2])
print(len(klasse))  # 4

# Letzte Zeile entfernen:
klasse.pop()
print(len(klasse))  # 3

# Bestimmte Zeile entfernen (z.B. Index 1):
klasse.pop(1)       # entfernt Laura
print(klasse)       # [["Tim", ...], ["Markus", ...]]


# -----------------------------------------------------------------------------
# KAPITEL 10: Nützliche Operationen – Summe, Durchschnitt, Maximum
# -----------------------------------------------------------------------------

noten = [
    [2, 3, 1, 2],   # Schüler 1
    [4, 3, 2, 3],   # Schüler 2
    [1, 1, 2, 1]    # Schüler 3
]

# --- Summe aller Elemente ---
gesamt = 0
for zeile in noten:
    for note in zeile:
        gesamt += note
print(f"Summe: {gesamt}")  # 25

# --- Durchschnitt einer einzelnen Zeile (= Notendurchschnitt Schüler 1) ---
schueler1 = noten[0]
durchschnitt = sum(schueler1) / len(schueler1)
print(f"Ø Schüler 1: {durchschnitt}")  # 2.0

# --- Größtes Element ohne max() ---
bisher_groesst = noten[0][0]  # Startwert = erstes Element
for zeile in noten:
    for wert in zeile:
        if wert > bisher_groesst:
            bisher_groesst = wert
print(f"Höchste Note: {bisher_groesst}")  # 4


# -----------------------------------------------------------------------------
# KAPITEL 11: Häufige Fehler und wie du sie erkennst
# -----------------------------------------------------------------------------

# FEHLER 1: Index out of range
# matrix[5][0]  ← wenn matrix nur 3 Zeilen hat → IndexError
# Lösung: print(len(matrix)) vor dem Zugriff prüfen

# FEHLER 2: Elemente ändern ohne Index
# for zeile in matrix:
#     for wert in zeile:
#         wert = 0  ← ändert NUR die lokale Variable, nicht die Liste!
# Lösung: for i in range(...): for j in range(...): matrix[i][j] = 0

# FEHLER 3: [[0]*n]*m Falle (siehe Kapitel 8)
# Lösung: immer Schleife oder List Comprehension nutzen

# FEHLER 4: Zeilen haben unterschiedliche Längen (wenn das nicht gewollt ist)
# Python erlaubt das – eine 2D-Liste MUSS keine rechteckige Form haben.
# Das kann gewollt sein (z.B. Dreieck), oder ein Bug.
# Lösung: bei Erstellung darauf achten, oder len(zeile) prüfen.

ungleich = [[1, 2], [3, 4, 5], [6]]  # völlig valides Python, aber Vorsicht


# -----------------------------------------------------------------------------
# KAPITEL 12: Kleines Beispielprojekt – Sitzplan
# -----------------------------------------------------------------------------
# Stell dir einen Kinosaal vor: 3 Reihen, 4 Sitze pro Reihe.
# 0 = frei, 1 = belegt

sitzplan = [
    [0, 1, 1, 0],   # Reihe 0
    [1, 1, 0, 0],   # Reihe 1
    [0, 0, 0, 1]    # Reihe 2
]

# Wie viele Plätze sind frei?
freie_plaetze = 0
for reihe in sitzplan:
    for sitz in reihe:
        if sitz == 0:
            freie_plaetze += 1
print(f"Freie Plätze: {freie_plaetze}")  # 7

# Ersten freien Platz finden:
for i in range(len(sitzplan)):
    for j in range(len(sitzplan[i])):
        if sitzplan[i][j] == 0:
            print(f"Erster freier Platz: Reihe {i}, Sitz {j}")
            break               # innere Schleife stoppen
    else:
        continue                # äußere Schleife weiter wenn innere NICHT durch break beendet
    break                       # äußere Schleife stoppen wenn break in innerer ausgeführt wurde


# =============================================================================
# ZUSAMMENFASSUNG
# =============================================================================
#
# 2D-Liste = Liste von Listen
#
# Erstellen:    matrix = [[1,2,3], [4,5,6], [7,8,9]]
# Zugriff:      matrix[zeile][spalte]
# Ändern:       matrix[i][j] = neuer_wert  (immer mit Indizes!)
# Iterieren:    for zeile in matrix: for element in zeile: ...
# Mit Index:    for i in range(len(matrix)): for j in range(len(matrix[i])): ...
# Zeile rein:   matrix.append([a, b, c])
# Zeile raus:   matrix.pop()  oder  matrix.pop(index)
#
# Faustregel: Wenn du etwas LESEN willst → "for element in zeile" reicht.
#             Wenn du etwas ÄNDERN willst → immer range(len(...)) + Indizes.
#
# =============================================================================
