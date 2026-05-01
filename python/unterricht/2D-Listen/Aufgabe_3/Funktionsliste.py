import copy


#1. Gesamtpunktzahl der Spieler
#Funktion definieren und parameter (punkte) setzen 
def punkte_gesamt(punkte):
    
    #leere Liste anlegen um Punkte zu speichern.
    gesamt = []
    
    # Die Spieler durchgehen
    for spieler in punkte: 

        # Die Gesamtpunkte der Spieler in der Liste speichern. 
        gesamt.append(sum(spieler))
        
    #Liste mit Gesamtpunktzahl zurück geben.
    return gesamt
              
#2. Teilnehmer mit höchster Punktzahl  
def bester_spieler(punkte_gesamt):
    # Variable zum Speichern der Punkte
    max_punkte = -1

    # Spieler durchgehen
    for spieler_index, spieler in enumerate(punkte_gesamt):
              
        # Punkte der Spieler vergleichen 
        if spieler > max_punkte: 
            
            # Besten Spieler in max_punkte speichern 
            max_punkte = spieler
        max_punkte_index = spieler_index  
            
    # max_punkte zurück geben.         
    return max_punkte_index, max_punkte, 
            

# #3.Durchschnitt jeder Kategorie
# def kategorie_durchschnitt(punkte):
    
#     katergorie_punkte = []
#     index = 0     
    
#     for spieler in punkte:
#        kategorie = 0 
#        for kategorie in spieler: 
            