import Funktionsliste as FL 


lager = [
        [12, 4, 7, 0], #23
        [3, 15, 0, 9], #27
        [0, 2, 1, 8]] #11          

#1. Gesamtzahl aller Produkte 
print("\n--- -1.- ---")
FL.produktanzahl_zaehlen(lager) # Das ganze Lager umfasst aktuell 61 Produkte.

 #2. Regal mit den meisten Produkten 
print("\n--- -2.- ---")
FL.regal_meiste_produkte(lager) # Reihe: 2 mit 27 Produkten.

#3. Liste die alle werte unter 5 auf 0 setzt 
print("\n--- -3.- ---")
print(f"Alte Lagerstruktur: {lager}") # Alte Lagerstruktur: [[12, 4, 7, 0], [3, 15, 0, 9], [0, 2, 1, 8]]
FL.werte_zurück_setzen(lager) # Neue Lagerstruktur: [[12, 0, 7, 0], [0, 15, 0, 9], [0, 0, 0, 8]

#4. Positionen mit leeren Regalen (Reihe, Regal)
print("\n--- -4.- ---")
FL.leere_regale_zaehlen(lager) # Leere Positionen im Lager: [(0, 3), (1, 2), (2, 0)]
