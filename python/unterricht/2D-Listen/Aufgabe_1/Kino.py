# Aufrufen der Moduldatei mit den Funktionen. Durch "as FL" ist die Funktion über FL aufrufbar
import Funktionsliste as FL

# Erstellen einer 2D-Liste. Index ist "Platz" Liste ist "Reihe". 
# Es sind zwei for-schleifen nötig. Die erste um die Reihen durch zu gehen, die zweite um die einzelnen reihen durch zu gehen.
kinosaal = [
    [25, 34, 0, 18, 42], 
    [0, 0, 51, 60, 33],
    [19, 22, 23, 0, 0],
    [45, 38, 0, 29, 31],
]

print("\n--- -1.- ---")
# Ausgabe: f für nen F-String {Modul.Funktion(Parameter)} aufrufen. 
print(f"Belegte Plätze: {FL.belegte_sitze_zählen(kinosaal)}")
# --- -1.- ---
# Belegte Plätze: 14

print("\n--- -2.- ---")
# Ausgabe: f für nen F-String {Modul.Funktion(Parameter)} aufrufen. Mit :.2f auf zwei stellen nach dem Komma reduzieren.
print(f"Durchschnittsalter: {FL.durchschnitt_alter_berechnen(kinosaal):.2f}")
# --- -2.- ---
# Durchschnittsalter: 33.57


print("\n--- -3.- ---")
# Ausgabe: f für nen F-String {Modul.Funktion(Parameter)} aufrufen. 
print(f"Vollste Reihe {FL.meist_belegte_reihe(kinosaal)}")
#--- -3.- ---
#Vollste Reihe 1 - [25, 34, 0, 18, 42]


