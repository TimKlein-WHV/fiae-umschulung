# Copy - Damit kann die Liste (lager) kopiert werden um diese zu verändern. 
import copy

#1. Gesamtzahl aller Produkte
# Funktion definieren und Parameter (lager) setzen
def produktanzahl_zaehlen(lager):
    # Zähler mit 0 initiieren
    produkte_in_allen_reihen = 0
    # Reihen durchgehen
    for reihe in lager:
        # Regale in der Reihe durchgehen
        for regal in reihe:
            # Wert zum Zähler addieren
            produkte_in_allen_reihen += regal
        # Zwischenstand merken
        ergebnis = produkte_in_allen_reihen
    # Ergebnis ausgeben
    return print(f"Das ganze Lager umfasst aktuell {ergebnis} Produkte.")



#2. Regal mit den meisten Produkten
# Funktion definieren und Parameter (lager) setzen
def regal_meiste_produkte(lager):
    # Variable für höchste Summe mit 0 initiieren
    vollste_reihe = 0
    # Reihen mit Index durchgehen
    for index, reihe in enumerate(lager):
        # Summe der Reihe mit bisherigem Maximum vergleichen
        if sum(reihe) > vollste_reihe:
            # Neue höchste Summe merken
            vollste_reihe = sum(reihe)
            # Index merken 
            vollste_index = index + 1
    # Ergebnis ausgeben
    return print(f"Reihe: {vollste_index} mit {vollste_reihe} Produkten.")


#3. 2D-Liste welche alle Werte unter 5 auf 0 setzt
# Funktion definieren und Parameter (lager) setzen
def werte_zurück_setzen(lager):
    #neue liste copy der alten zuweisen
    lager_sortiert = copy.deepcopy(lager)
    # Reihen mit Index durchgehen
    for reihe_index, reihe in enumerate(lager):
        # Regale mit Index durchgehen
        for regal_index, regal in enumerate(reihe):
            # Prüfen ob Wert unter 5
            if regal < 5:
                # Wert direkt in der Liste auf 0 setzen
                lager_sortiert[reihe_index][regal_index] = 0
    # Neue Liste ausgeben
    return print(f"Neue Lagerstruktur: {lager_sortiert}")


#4. Positionen mit leeren Regalen
# Funktion definieren und Parameter (lager) setzen
def leere_regale_zaehlen(lager):
    # Leere Liste anlegen um Positionen als Tupel zu speichern
    leere_positionen = []
    # Reihen mit Index durchgehen
    for reihe_index, reihe in enumerate(lager):
        # Regale mit Index durchgehen
        for regal_index, regal in enumerate(reihe):
            # Prüfen ob Regal leer ist
            if regal == 0:
                # Position als Tupel (Reihe, Regal) in Liste speichern
                leere_positionen.append((reihe_index, regal_index))
    # Alle leeren Positionen ausgeben
    return print(f"Leere Positionen im Lager: {leere_positionen}.")