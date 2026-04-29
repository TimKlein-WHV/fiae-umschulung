# Aufrufen der Moduldatei mit den Funktionen. Durch "as FL" ist die Funktion über FL aufrufbar
import Funktionsliste as FL

# Erstellen einer 2D-Liste. 
kinosaal = [
    [25, 34, 0, 18, 42], 
    [0, 0, 51, 60, 33],
    [19, 22, 23, 0, 0],
    [45, 38, 0, 29, 31]]

# Anzahl der Belegten Plätze
print("\n--- -1.- ---")
print(f"Belegte Plätze: {FL.belegte_sitze_zählen(kinosaal)}") # Belegte Plätze: 14

# Durchschnittsalter
print("\n--- -2.- ---")
print(f"Durchschnittsalter: {FL.durchschnitt_alter_berechnen(kinosaal):.2f}") # Durchschnittsalter: 33.57

# Reihe mit den meisten belegten Plätzen. 
print("\n--- -3.- ---")
print(f"Vollste Reihe {FL.meist_belegte_reihe(kinosaal)}") # Vollste Reihe 1 - [25, 34, 0, 18, 42]

