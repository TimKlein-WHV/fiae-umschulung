import Funktionsliste as FL


# Reihe = Spieler 
# Wert = Punkte in Kategorie
punkte =[
        [8, 7, 9, 6], 
        [5, 6, 5, 4],
        [9, 9, 10, 8],
        [3, 4, 2, 5]
        ]

x = FL.punkte_gesamt(punkte)
y = FL.bester_spieler(x) 


#1 Gesamtzahl aller Punkte 
print("\n--- -1.- ---")
print(f"Die gesamtpunkte der Spieler:{FL.punkte_gesamt(punkte)}")


# #2. Teilnehmer mit höchster Punktzahl  
print("\n--- -2.- ---")
print(f"Der Beste spieler hat {y}")

# #3.Durchschnitt jeder Kategorie
# print("\n--- -3.- ---")

# Neue Liste mit Teilnehmern mit > 25 Punkte
# print("\n--- -4.- ---")