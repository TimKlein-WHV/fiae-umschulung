import Funktionsliste as FL 

# Eine Liste in lager anlegen. 
lager = [
        [12, 4, 7, 0], #23
        [3, 15, 0, 9], #27
        [0, 2, 1, 8], #11
        ]
            



#1. Gesamtzahl aller Produkte (61)
print("\n--- -1.- ---")
print(f"Produkte: {FL.produktanzahl_zählen(lager)}")

 #2. Regal mit den meisten Produkten (2)
print("\n--- -2.- ---")
print(f"Regal: {FL.regal_meiste_produkte(lager)}")

# #3. Liste die alle werte unter 5 auf 0 setzt 
# print("\n--- -3.- ---")


# #4. Positionen mit leeren Regalen
# print("\n--- -4.- ---")
