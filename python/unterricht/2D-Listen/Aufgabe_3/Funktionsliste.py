import copy


## 1. Gesamtpunktzahl der Spieler
def punkte_gesamt(punkte):

    # Leere Liste anlegen um Gesamtpunkte zu speichern.
    gesamt = []

    # Die Spieler durchgehen
    for spieler in punkte:

        # Gesamtpunkte des Spielers berechnen und speichern.
        gesamt.append(sum(spieler))

    # Liste mit Gesamtpunktzahl zurück geben.
    return gesamt

## 2. Teilnehmer mit höchster Punktzahl
def bester_spieler(punkte_gesamt):

    # Startwert für Vergleich setzen
    max_punkte = -1

    # Alle Spieler mit Index durchgehen
    for spieler_index, spieler in enumerate(punkte_gesamt):

        # Punkte des aktuellen Spielers mit bisherigem Maximum vergleichen
        if spieler > max_punkte:

            # Neues Maximum und zugehörigen Index speichern
            max_punkte = spieler
            max_punkte_index = spieler_index

    # Index und Punkte des besten Spielers zurück geben.
    return max_punkte_index, max_punkte

## 3. Durchschnitt jeder Kategorie
def kategorie_durchschnitt(punkte):

    # Leere Liste für Durchschnittswerte anlegen
    gesamt = []

    # Jede Kategorie (Spalte) durchgehen
    for spieler in range(len(punkte[0])):

        # Summe für diese Kategorie zurücksetzen
        kategorie_punkte = 0

        # Jeden Spieler durchgehen und Wert der Kategorie addieren
        for kategorie in punkte:
            kategorie_punkte += kategorie[spieler]

        # Durchschnitt berechnen und speichern
        gesamt.append(kategorie_punkte / len(punkte))

    # Liste mit Durchschnittswerten zurück geben
    return gesamt

## 4. Neue Liste mit Spielern > 25 Punkte
def liste_mit_mehr_25(punkte):

    # Leere Liste für Spieler-Indizes anlegen
    index_liste = []

    # Alle Spieler mit Index durchgehen
    for spieler_index, spieler in enumerate(punkte):

        # Gesamtpunkte prüfen — nur Spieler über 25 speichern
        if sum(spieler) > 25:

            # Spielernummer (ab 1) in Liste speichern
            index_liste.append(spieler_index + 1)

    # Liste mit Spielernummern zurück geben
    return index_liste
