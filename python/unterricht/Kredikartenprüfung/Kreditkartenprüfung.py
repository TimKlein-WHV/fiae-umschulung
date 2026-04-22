def quersumme(i):
    summe = 0
    for zahl in str(i):
        summe += int(zahl)
    return summe


kreditkarten_nr = [9, 3, 4, 2, 5, 7, 1, 8, 6, 6, 7, 0, 1, 9, 9, 6]

pz_verdoppeln = kreditkarten_nr[-2::-2]
pz_normal = kreditkarten_nr[-3::-2]
pruefziffer = kreditkarten_nr[-1]
summe_gesamt = 0

for i in pz_verdoppeln:
    verdoppelt = i * 2
    summe_gesamt += quersumme(verdoppelt)

for i in pz_normal:
    summe_gesamt += i

berechnete_pz = (10 - (summe_gesamt % 10)) % 10

if berechnete_pz == pruefziffer:
    print("Nummer gültig")
else:
    print("Nummer nicht gültig")
