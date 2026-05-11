# =============================================================================
#  HASHING & SETS IN PYTHON – Von Null erklärt für Quereinsteiger
# =============================================================================
#
#  Was ist ein Hash überhaupt?
#  ----------------------------
#  Stell dir vor, jeder Mensch bekommt einen Personalausweis mit einer
#  eindeutigen Nummer. Statt den ganzen Namen zu vergleichen, vergleicht
#  Python nur diese Nummern – das ist viel schneller.
#
#  hash() macht genau das: wandelt jeden Wert in eine (möglichst eindeutige)
#  Zahl um. Diese Zahl heißt Hash.
#
#  Zwei Werte sind gleich wenn:
#   1) ihr Hash identisch ist  UND
#   2) sie auch wirklich gleich sind (== gibt True)
#
# =============================================================================
#  AUFBAU von hash()
# =============================================================================
#
#  hash( wert )
#  │     │
#  │     └─ beliebiger Wert (int, str, bool, float, tuple ...)
#  └─ eingebaute Python-Funktion
#
#       → gibt eine ganze Zahl zurück (den "Fingerabdruck")
#
#  Wichtig: Strings bekommen bei jedem Python-Start einen anderen Hash.
#           Zahlen haben immer denselben Hash (hash(42) == 42 immer).
#
# =============================================================================


# =============================================================================
#  1. DIE hash()-FUNKTION – Was gibt sie zurück?
# =============================================================================

print("1. Hashes von verschiedenen Typen:")
print("hash(42)      =", hash(42))       # immer: 42
print("hash(3.14)    =", hash(3.14))     # feste Zahl
print("hash(True)    =", hash(True))     # immer: 1
print("hash(False)   =", hash(False))    # immer: 0
print("hash('Otto')  =", hash("Otto"))   # ändert sich je Python-Start
print("hash((1,2,3)) =", hash((1,2,3)))  # Tuple hashbar

# Listen sind NICHT hashbar → würde Fehler werfen:
# hash([1,2,3])  →  TypeError: unhashable type: 'list'
# Grund: Listen können verändert werden → Hash wäre nicht stabil


# =============================================================================
#  2. WAS IST EIN SET?
# =============================================================================
#
#  Set = Sammlung ohne Duplikate, ohne feste Reihenfolge.
#  Wie eine Gästeliste: "Otto" steht einmal drauf, egal wie oft du ihn einlädst.
#
#  Intern arbeitet Set mit hash() um Duplikate zu erkennen:
#
#   Element rein  →  hash() berechnen  →  schon vorhanden?
#                                              │
#                                    ja → wegwerfen
#                                    nein → speichern
#

gaesteliste = {"Otto", "Anna", "Otto", "Klaus", "Anna"}
print("\n2. Set ohne Duplikate:")
print(gaesteliste)   # {'Otto', 'Anna', 'Klaus'} — Duplikate weg, Reihenfolge egal


# =============================================================================
#  3. DUPLIKAT-ERKENNUNG – Die zwei Bedingungen
# =============================================================================
#
#  Ein Wert wird als Duplikat erkannt wenn BEIDE Bedingungen erfüllt sind:
#
#  Bedingung 1: hash(x) == hash(y)      ← gleicher Fingerabdruck
#  Bedingung 2: x == y                  ← wirklich gleicher Wert
#
#  Beispiele:
#  ┌──────────────┬──────────────┬─────────────┬──────────────┬───────────┐
#  │    x         │     y        │  hash gleich │  x == y      │ Duplikat? │
#  ├──────────────┼──────────────┼─────────────┼──────────────┼───────────┤
#  │    1         │    True      │     ✓ (1)    │   ✓ (True)   │    JA     │
#  │    0         │    False     │     ✓ (0)    │   ✓ (True)   │    JA     │
#  │    0         │    0.0       │     ✓ (0)    │   ✓ (True)   │    JA     │
#  │   "1"        │     1        │     ✗        │   ✗ (False)  │   NEIN    │
#  │  "Otto"      │   "otto"     │     ✗        │   ✗ (False)  │   NEIN    │
#  └──────────────┴──────────────┴─────────────┴──────────────┴───────────┘

menge = {1, True, "1", "Otto", "Otto", 0, False}
print("\n3. Set aus {1, True, '1', 'Otto', 'Otto', 0, False}:")
print(menge)
# Ausgabe: {0, 1, '1', 'Otto'}
# True  fliegt raus → Duplikat von 1
# False fliegt raus → Duplikat von 0
# "Otto" doppelt   → einmal weg
# "1"   bleibt     → String, anderer Hash als int 1


# =============================================================================
#  4. DIE ÜBERRASCHUNG: bool IST int
# =============================================================================
#
#  In Python ist bool eine Unterklasse von int.
#  True  ist intern 1.
#  False ist intern 0.
#
#  Deshalb kann man mit True/False auch rechnen:

print("\n4. bool ist int:")
x, y = 1, True
print("1 == True       :", x == y)     # True  → gleichwertig
print("1 is True       :", x is y)     # False → verschiedene Objekte im Speicher
print("type(True)      :", type(True)) # <class 'bool'>
print("isinstance(True, int):", isinstance(True, int))  # True → bool erbt von int

print("\nRechnen mit bool:")
print("2 + True   =", 2 + True)        # 3
print("2 + False  =", 2 + False)       # 2
print("True  * 5  =", True * 5)        # 5
print("False * 5  =", False * 5)       # 0
# Macht man normalerweise nicht — aber Python lässt es zu.


# =============================================================================
#  5. SET ERSTELLEN – vier Wege
# =============================================================================

print("\n5. Sets erstellen:")

# Weg 1: direkt mit geschweiften Klammern
s1 = {1, 2, 3}
print("Direkt          :", s1)

# Weg 2: aus einer Liste (Duplikate werden entfernt)
s2 = set([1, 2, 2, 3, 3, 3])
print("Aus Liste       :", s2)          # {1, 2, 3}

# Weg 3: leeres Set — ACHTUNG: {} ist ein leeres Dict, nicht Set!
s3 = set()
print("Leer (richtig)  :", s3, type(s3))   # set()
s4 = {}
print("Leer (falsch)   :", s4, type(s4))   # {} → dict!

# Weg 4: aus einem String (jedes Zeichen einzeln)
s5 = set("hallo")
print("Aus String      :", s5)          # {'h', 'a', 'l', 'o'} — l nur einmal


# =============================================================================
#  6. SET VERÄNDERN – Elemente hinzufügen und entfernen
# =============================================================================

print("\n6. Set verändern:")
menge = {1, 2, 3}

menge.add(4)            # Element hinzufügen
print("Nach add(4)    :", menge)    # {1, 2, 3, 4}

menge.add(2)            # Duplikat → passiert nichts, kein Fehler
print("Nach add(2)    :", menge)    # {1, 2, 3, 4}

menge.remove(3)         # Element entfernen → Fehler wenn nicht vorhanden
print("Nach remove(3) :", menge)    # {1, 2, 4}

menge.discard(99)       # entfernen ohne Fehler wenn nicht vorhanden
print("Nach discard(99):", menge)   # {1, 2, 4} — kein Fehler

print("5 in menge     :", 5 in menge)   # False
print("2 in menge     :", 2 in menge)   # True


# =============================================================================
#  7. SET-OPERATIONEN – Mengenlehre aus der Schule
# =============================================================================
#
#   a = {1, 2, 3, 4}          b = {3, 4, 5, 6}
#
#   Vereinigung  a | b:    {1, 2, 3, 4, 5, 6}  ← alles aus beiden
#                ┌───┐ ┌───┐
#                │1,2│█│5,6│     █ = gemeinsam
#                │   │3,4│   │
#                └───┘ └───┘
#
#   Schnittmenge a & b:    {3, 4}              ← nur gemeinsame
#   Differenz    a - b:    {1, 2}              ← in a, nicht in b
#   Sym.Diff.    a ^ b:    {1, 2, 5, 6}        ← in einem, nicht in beiden

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\n7. Set-Operationen:")
print("a =", a)
print("b =", b)
print("a | b  Vereinigung     :", a | b)
print("a & b  Schnittmenge    :", a & b)
print("a - b  Differenz       :", a - b)
print("a ^ b  Sym. Differenz  :", a ^ b)

# Auch als Methoden nutzbar (gleichwertig):
# a.union(b)        ==  a | b
# a.intersection(b) ==  a & b
# a.difference(b)   ==  a - b


# =============================================================================
#  8. FROZENSET – eingefrorenes Set
# =============================================================================
#
#  Normales Set: veränderbar (.add(), .remove() möglich)
#  Frozenset:    eingefroren → keine Änderungen möglich
#
#  Wann nutzen? Wenn die Menge als Dict-Key genutzt werden soll,
#  oder wenn sichergestellt sein muss, dass sich nichts ändert.

print("\n8. Frozenset:")
fs = frozenset({1, 2, 3})
print("frozenset:", fs)
print("2 in fs  :", 2 in fs)   # True — lesen geht

# fs.add(4)    → AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1) → AttributeError: eingefroren!

# Als Dict-Key nutzbar (normales Set nicht):
d = {frozenset({1, 2}): "Gruppe A"}
print("Als Dict-Key:", d)


# =============================================================================
#  9. HÄUFIGE FEHLER
# =============================================================================

# FEHLER 1: Leeres Set mit {} erstellen
# leer = {}         ← Dict, nicht Set! → type(leer) = dict
# Lösung: leer = set()

# FEHLER 2: Liste in Set packen wollen
# menge = {[1,2], [3,4]}  ← TypeError: unhashable type: 'list'
# Lösung: Tuple statt Liste → menge = {(1,2), (3,4)}

# FEHLER 3: Set hat keine Reihenfolge – Index funktioniert nicht
menge = {10, 20, 30}
# menge[0]  → TypeError: 'set' object is not subscriptable
# Lösung: in Liste umwandeln wenn Reihenfolge nötig
liste = list(menge)
print("\n9. Set zu Liste:", liste)   # Reihenfolge nicht garantiert

# FEHLER 4: Wert ändern nach .add() und wundern warum Duplikat bleibt
# Sets merken sich den Hash zum Zeitpunkt des Einfügens.
# Deshalb sind veränderliche Typen (list, dict) nicht hashbar → kein Reinpacken.


# =============================================================================
#  ZUSAMMENFASSUNG
# =============================================================================
#
#  HASH = Fingerabdruck eines Wertes als Zahl
#         hash(42) == 42,  hash(True) == 1,  hash(False) == 0
#
#  SET  = Sammlung ohne Duplikate, ohne Reihenfolge
#
#  Erstellen:         menge = {1, 2, 3}
#  Leer (richtig):    menge = set()          ← {} wäre Dict!
#  Element rein:      menge.add(4)
#  Element raus:      menge.remove(4)        ← Fehler wenn nicht vorhanden
#                     menge.discard(4)       ← kein Fehler
#  Prüfen:            4 in menge             → True/False
#
#  DUPLIKAT-REGEL: hash(x) == hash(y)  UND  x == y  → Duplikat → weg
#    True  == 1   → Duplikat     "1" != 1  → kein Duplikat
#    False == 0   → Duplikat     0.0 == 0  → Duplikat
#
#  OPERATIONEN:
#    a | b   Vereinigung       a & b   Schnittmenge
#    a - b   Differenz         a ^ b   Sym. Differenz
#
#  FROZENSET = unveränderliches Set
#    fs = frozenset({1, 2, 3})    kein .add() / .remove()
#
# =============================================================================
