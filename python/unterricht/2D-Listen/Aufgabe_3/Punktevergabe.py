import Funktionsliste as FL


# Reihe = Spieler
# Spalte = Kategorie
# Wert = Punkte in Kategorie
punkte =[
        [8, 7, 9, 6], 
        [5, 6, 5, 4],
        [9, 9, 10, 8],
        [3, 4, 2, 5]
        ]

## 1. Gesamtpunktzahl aller Punkte 
#--------------------------------------------------#
print("\n--- -1.- ---")
print("Gesamtpunktzahle der Einzelnen Spieler")
print(f"Spieler 1: {FL.punkte_gesamt(punkte)[0]}")
print(f"Spieler 2: {FL.punkte_gesamt(punkte)[1]}")
print(f"Spieler 3: {FL.punkte_gesamt(punkte)[2]}")
print(f"Spieler 4: {FL.punkte_gesamt(punkte)[3]}")
#--------------------------------------------------#



## 2. Teilnehmer mit höchster Punktzahl  
#--------------------------------------------------#
print("\n--- -2.- ---")
print("Teilnehmer mit Höchster Punktzahl")
# Gesamtpunkte berechnen und speichern
bester_spieler_speicher = FL.punkte_gesamt(punkte)
# Besten Spieler ermitteln und Index + Punkte entpacken
spieler_nr, max_punkte = FL.bester_spieler(bester_spieler_speicher)

print(f"Bester Spieler: {spieler_nr + 1}")
print(f"Punkte: {max_punkte}")
#--------------------------------------------------#



## 3.Durchschnitt jeder Kategorie
#--------------------------------------------------#
print("\n--- -3.- ---")
print("Durchschnitt der einzelnen Kategorien")
print(f"Kategorie 1: {FL.kategorie_durchschnitt(punkte)[0]}")
print(f"Kategorie 2: {FL.kategorie_durchschnitt(punkte)[1]}")
print(f"Kategorie 3: {FL.kategorie_durchschnitt(punkte)[2]}")
print(f"Kategorie 4: {FL.kategorie_durchschnitt(punkte)[3]}")
#--------------------------------------------------#



## 4. Neue Liste mit Teilnehmern mit > 25 Punkte
#--------------------------------------------------#
print("\n--- -4.- ---")
print("Teilnehmer mit > 25 Punkten")
print(f"Spieler: {FL.liste_mit_mehr_25(punkte)}")

#--------------------------------------------------#