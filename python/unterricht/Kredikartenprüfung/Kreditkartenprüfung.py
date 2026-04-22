# Funktion die die Quersumme einer Zahl berechnet (z.B. 18 -> 1+8 = 9)
def quersumme(i):
    summe = 0
    for zahl in str(
        i
    ):  # Zahl in Text umwandeln, damit man jede Stelle einzeln durchgehen kann
        summe += int(zahl)  # jede Stelle wieder in eine Zahl umwandeln und aufaddieren
    return summe


# Die Kreditkartennummer als Liste, die letzte Stelle (6) ist die Prüfziffer
kreditkarten_nr = [9, 3, 4, 2, 5, 7, 1, 8, 6, 6, 7, 0, 1, 9, 9, 6]

# Schritt 1: jede zweite Ziffer raus ziehen (beginnend bei der vorletzten) -> diese werden verdoppelt
pz_verdoppeln = kreditkarten_nr[-2::-2]

# die restlichen Ziffern (ohne Prüfziffer) die nicht verdoppelt werden
pz_normal = kreditkarten_nr[-3::-2]

# die letzte Stelle ist die Prüfziffer, mit der wir am Ende vergleichen
pruefziffer = kreditkarten_nr[-1]

summe_gesamt = 0

# Schritt 2: alle zu verdoppelnden Ziffern verdoppeln und Quersumme aufaddieren
for i in pz_verdoppeln:
    verdoppelt = i * 2
    summe_gesamt += quersumme(verdoppelt)  # z.B. 9*2=18 -> quersumme(18) = 9

# die normalen Ziffern einfach direkt dazu addieren
for i in pz_normal:
    summe_gesamt += i

# Schritte 3 & 4: berechnete Prüfziffer ermitteln
# Schritt 3: Differenz zur nächsten durch 10 teilbaren Zahl (z.B. 74 % 10 = 4)
# Schritt 4: 10 minus dieses Ergebnis (z.B. 10 - 4 = 6), falls 10 rauskommt wird es 0
berechnete_pz = (10 - (summe_gesamt % 10)) % 10

# Vergleich: berechnete Prüfziffer mit der tatsächlichen Prüfziffer aus der Kreditkartennummer
if berechnete_pz == pruefziffer:
    print("Nummer gültig")
else:
    print("Nummer nicht gültig")
