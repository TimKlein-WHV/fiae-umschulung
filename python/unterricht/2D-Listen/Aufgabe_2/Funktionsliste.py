#1. Gesamtzahl aller Produkte
# Funktion definieren und den Parameter (lager) setzen
def produktanzahl_zählen(lager): 
    # reihe und regal mit 0 initiieren
    produkte_in_allen_reihen = 0 
    # reihe durchgehen
    for reihe in lager:         
        # regal durchgehen 
        for regal in reihe:                
            # Produkte in reihe zusammen rechnen 
            produkte_in_allen_reihen += regal   # Produkte in reihen zusammen rechnen
        # alle Produkte zusammen rechnen 
        ergebnis = produkte_in_allen_reihen
    # Ergebnis ausgeben
    return ergebnis



#2. Regal mit den meisten Produkten
# Funktion definieren und den Parameter (lager) setzen
def regal_meiste_produkte(lager): 

    for index, reihe in  enumerate(lager): 
        max_regal = 0 

        for regal in reihe: 

            if regal != 0: 


                max_regal += regal

        if max_regal > max_reihe: 
            max_reihe = max_regal
            beste_reihe = reihe
            beste_index = index 

    return beste_index, max_reihe
