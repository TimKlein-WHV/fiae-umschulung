## ------------------------- -Imports- ------------------------- ##
import Funktionsliste as FL


## ------------------------ -Variablen- ------------------------ ##
date = "Mai 2003"
mitarbeiter_id = 12345

zeiten = [[2, 480],
          [2, 1040],
          [3, 470],
          [6, 480],
          [6, 960],
          [7, 990],
          [8, 480],
          [8, 960],
          ["...", "..."],
          [30, 990]
          ]

## ------------------------- -Ausgabe- ------------------------- ##
print(f"\nMitarbeiter: {mitarbeiter_id}                    {date}")

print("\nTag   Kommen   Gehen   Anwesenheit   Bemerkung")
print("===============================================")
FL.zeiten_berechnen(zeiten)
