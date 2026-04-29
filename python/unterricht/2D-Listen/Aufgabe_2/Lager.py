import Funktionsliste as FL 

# Eine Liste in lager anlegen. 
lager = [
        [12, 4, 7, 0], #23
        [3, 15, 0, 9], #27
        [0, 2, 1, 8], #11
        ]          



#1. Gesamtzahl aller Produkte (61)
print("\n--- -1.- ---")
FL.produktanzahl_zaehlen(lager)

 #2. Regal mit den meisten Produkten (2, 27 Produkte)
print("\n--- -2.- ---")
FL.regal_meiste_produkte(lager)


#3. Liste die alle werte unter 5 auf 0 setzt 
print("\n--- -3.- ---")
print(f"Alte Lagerstruktur: {lager}")
FL.werte_zurück_setzen(lager)

# #4. Positionen mit leeren Regalen
print("\n--- -4.- ---")
print("work in progress!")
FL.leere_regale_zaehlen(lager)