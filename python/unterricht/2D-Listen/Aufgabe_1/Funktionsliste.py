## 1. Belegte Sitze zählen
# Funktion definieren und den (Parameter) setzen
# in diesem Fall die Liste (Kinosaal)

def belegte_sitze_zählen(kinosaal):

    # Erstelle eine Liste in belegt. 
    belegt = []

    # Für die Reihe in Kinosaal
    for reihe in kinosaal:

        # eine_reihe definiere: [nimm sitz für sitz in reihe wenn sitz nicht 0]
        eine_reihe = [sitz for sitz in reihe if sitz != 0]

        # füge der Liste in belegt das Ergebnis aus eine_reihe zu.
        belegt.append(eine_reihe)

    # definiere eine neue Variable belegt_count: summe aus der länge von reihe für Reige in belegt
    belegt_count = sum([len(reihe) for reihe in belegt])

    # das Ergebnis von belegt_count zurückgeben. 
    return belegt_count

# ------------------------------------------------------------------------------

## 2. Durchschnitts Alter berechnen
#Funktion definieren und den (Parameter) setzen
# in diesem Fall die Liste (Kinosaal)
def durchschnitt_alter_berechnen(kinosaal): 

    # alter mit 0 initiieren. 
    alter = 0

    # Da die belegten sitze bereits in einer Funktion gezählt werden, wird diese Funktion der variable sitze zugewiesen. 
    sitze = belegte_sitze_zählen(kinosaal)

    # Die Reihen durchgehen 
    for reihe in kinosaal: 

        # Die Plätze durchgehen
        for platz in reihe:
        
            # prüfen ob platz belegt
            if platz != 0:

                # wenn platz belegt wird alter mit platz verrechnet.
                alter += platz
    # um den durchschnitt zu errechnen nehme ich das gesamte alter und dividiere es durch sitze
    duschschnitt = alter / sitze

    # den durchschnitt zurück geben
    return duschschnitt

# ------------------------------------------------------------------------------

## 3. Reihe mit den meisten belegten Plätzen
#Funktion definieren und den (Parameter) setzen
# in diesem Fall die Liste (Kinosaal)
def meist_belegte_reihe(kinosaal):

    # Variable für den Höchstwert
    max_belegt = 0 
 

    # index und reihen durchgehen
    for index, reihe in enumerate(kinosaal): 

        # Platzzähler Variable mit 0 
        platz_zaehler = 0

        # Plätze in der Reihe durchgehen 
        for platz in reihe: 
            
            # prüfen ob Platz belegt (>0)
            if platz != 0: 

                # dem platz Zähler einen dazu addieren
                platz_zaehler += 1

        # prüfen ob platz Zähler > max_belegt Zähler
        if max_belegt < platz_zaehler:

            # max_belegt Zähler den wert vom Platzzähler zuweisen
            max_belegt = platz_zaehler

            # eine Variable die die aktuell beste Reihe festhält
            beste_reihe = reihe

            # den Index (die Reihennummer) einer Variable zuweisen 
            beste_index = index

    # index und beste_reihe zurück geben. Index +1 da Kinoreihen nicht bei 0 Anfangen sondern meistens bei 1. 
    return f"{beste_index +1} - {beste_reihe}"