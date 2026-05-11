-- =============================================================================
-- SQL GRUNDLAGEN – MariaDB 
-- =============================================================================
-- SQL = Structured Query Language
-- Ausgesprochen: "S-Q-L" oder "Sequel" (beide sind akzeptiert, niemand stirbt)
--
-- Was macht SQL?
-- SQL ist die Sprache, mit der du mit Datenbanken redest.
-- Du fragst Daten ab, fügst ein, änderst oder löschst sie.
-- MariaDB ist das Datenbanksystem – SQL ist die Sprache dazu.
-- Vergleich: MariaDB = Küche, SQL = Rezeptsprache.
--
-- Kommentare in SQL:
-- Einzeilig:  -- Das ist ein Kommentar
-- Mehrzeilig: /* Das ist
--                auch ein Kommentar */


-- =============================================================================
-- 1. DATENBANK ERSTELLEN & AUSWÄHLEN
-- =============================================================================
-- Zuerst brauchst du eine Datenbank – wie ein Ordner für deine Tabellen.

CREATE DATABASE meine_datenbank;   -- Datenbank erstellen

USE meine_datenbank;               -- Datenbank auswählen (aktivieren)

-- Ohne USE läuft jeder Befehl ins Leere oder in die falsche Datenbank.
-- Immer zuerst USE machen!

SHOW DATABASES;                    -- alle Datenbanken anzeigen
DROP DATABASE meine_datenbank;     -- Datenbank löschen (VORSICHT: unwiderruflich)


-- =============================================================================
-- 2. TABELLEN – DIE GRUNDSTRUKTUR
-- =============================================================================
-- Daten leben in Tabellen. Tabellen = Excel-Tabellen, nur mit Hirn.
-- Jede Tabelle hat Spalten (Felder) und Zeilen (Datensätze).
--
-- Beispiel: Tabelle "personen"
-- +----+-------+-----+-------+
-- | id | name  | alter | stadt |
-- +----+-------+-----+-------+
-- |  1 | Tim   |  36 | Whv   |
-- |  2 | Jana  |  29 | Hbg   |
-- +----+-------+-----+-------+

CREATE TABLE personen (
    id     INT          NOT NULL AUTO_INCREMENT,  -- eindeutige ID, zählt automatisch hoch
    name   VARCHAR(100) NOT NULL,                 -- Text bis 100 Zeichen, Pflichtfeld
    alter  INT,                                   -- Ganzzahl, optional
    stadt  VARCHAR(100),                          -- Text, optional
    PRIMARY KEY (id)                              -- id ist der eindeutige Schlüssel
);

-- PRIMARY KEY = jede Zeile hat eine eindeutige Nummer → kein Chaos
-- AUTO_INCREMENT = MariaDB zählt selbst hoch (1, 2, 3, …), du musst nichts tun
-- NOT NULL = darf nicht leer sein
-- VARCHAR(n) = Text bis n Zeichen

-- Tabelle anzeigen / prüfen:
SHOW TABLES;                       -- alle Tabellen in aktiver Datenbank
DESCRIBE personen;                 -- Aufbau der Tabelle anzeigen
DESC personen;                     -- Kurzform von DESCRIBE


-- =============================================================================
-- 3. WICHTIGE DATENTYPEN
-- =============================================================================
--
-- Zahlen:
--   INT             Ganzzahl             (-2 Mrd bis +2 Mrd)
--   BIGINT          große Ganzzahl       für sehr große IDs
--   DECIMAL(10,2)   Kommazahl            z.B. Preise: 9.99
--   FLOAT / DOUBLE  Fließkomma           für wissenschaftliche Werte
--
-- Text:
--   VARCHAR(n)      variabler Text       bis n Zeichen, spart Platz
--   CHAR(n)         fixer Text           immer n Zeichen (z.B. Postleitzahl)
--   TEXT            langer Text          bis 65.000 Zeichen
--   LONGTEXT        sehr langer Text     für Artikel, Beschreibungen
--
-- Datum/Zeit:
--   DATE            nur Datum            2026-05-11
--   TIME            nur Uhrzeit          14:30:00
--   DATETIME        Datum + Uhrzeit      2026-05-11 14:30:00
--   TIMESTAMP       wie DATETIME         aktualisiert sich automatisch
--
-- Wahrheitswert:
--   BOOLEAN / TINYINT(1)   0 = false, 1 = true


-- =============================================================================
-- 4. DATEN EINFÜGEN – INSERT
-- =============================================================================
-- Zeilen in Tabelle einfügen.

-- Alle Spalten befüllen (id weglassen, AUTO_INCREMENT macht das):
INSERT INTO personen (name, alter, stadt)
VALUES ('Tim', 36, 'Wilhelmshaven');

-- Mehrere Zeilen auf einmal:
INSERT INTO personen (name, alter, stadt)
VALUES
    ('Jana',  29, 'Hamburg'),
    ('Max',   41, 'Berlin'),
    ('Sara',  33, 'München');

-- Reihenfolge der Spalten muss zur Reihenfolge der VALUES passen!
-- Falsch:  VALUES ('Tim', 'Wilhelmshaven', 36)  ← Stadt und Alter vertauscht


-- =============================================================================
-- 5. DATEN ABFRAGEN – SELECT
-- =============================================================================
-- Der wichtigste Befehl in SQL. Du wirst ihn 1000x benutzen.

-- Alle Spalten, alle Zeilen:
SELECT * FROM personen;

-- Nur bestimmte Spalten:
SELECT name, stadt FROM personen;

-- Mit Alias – Spalte umbenennen in der Ausgabe:
SELECT name AS 'Vorname', alter AS 'Lebensalter' FROM personen;

-- Duplikate entfernen:
SELECT DISTINCT stadt FROM personen;


-- =============================================================================
-- 6. FILTERN – WHERE
-- =============================================================================
-- Nicht alle Daten, nur die die du willst.

SELECT * FROM personen WHERE alter = 36;
SELECT * FROM personen WHERE stadt = 'Hamburg';
SELECT * FROM personen WHERE alter > 30;
SELECT * FROM personen WHERE alter >= 30 AND alter <= 40;
SELECT * FROM personen WHERE alter < 30 OR stadt = 'Berlin';
SELECT * FROM personen WHERE NOT stadt = 'München';

-- Vergleichsoperatoren:
--   =     gleich
--   !=    ungleich   (auch: <>)
--   >     größer als
--   <     kleiner als
--   >=    größer gleich
--   <=    kleiner gleich

-- BETWEEN – Bereich (inklusive Grenzen):
SELECT * FROM personen WHERE alter BETWEEN 30 AND 40;

-- IN – Liste von Werten:
SELECT * FROM personen WHERE stadt IN ('Hamburg', 'Berlin', 'München');

-- LIKE – Muster suchen (% = beliebig viele Zeichen, _ = genau ein Zeichen):
SELECT * FROM personen WHERE name LIKE 'T%';      -- beginnt mit T
SELECT * FROM personen WHERE name LIKE '%a';      -- endet mit a
SELECT * FROM personen WHERE name LIKE '%im%';    -- enthält "im"
SELECT * FROM personen WHERE name LIKE '_ara';    -- 4 Buchstaben, endet auf "ara"

-- NULL prüfen (NULL ist NICHT gleich 0 oder ''):
SELECT * FROM personen WHERE alter IS NULL;       -- kein Alter eingetragen
SELECT * FROM personen WHERE alter IS NOT NULL;   -- Alter vorhanden


-- =============================================================================
-- 7. SORTIEREN – ORDER BY
-- =============================================================================

SELECT * FROM personen ORDER BY name;              -- alphabetisch aufsteigend (A→Z)
SELECT * FROM personen ORDER BY name ASC;          -- gleich (ASC = aufsteigend, Standard)
SELECT * FROM personen ORDER BY alter DESC;        -- absteigend (groß→klein)

-- Nach mehreren Spalten sortieren:
SELECT * FROM personen ORDER BY stadt ASC, alter DESC;
-- → erst nach Stadt alphabetisch, bei gleichem Ort dann ältere zuerst


-- =============================================================================
-- 8. BEGRENZEN – LIMIT
-- =============================================================================
-- Nicht immer willst du alle Zeilen – LIMIT stoppt nach n Zeilen.

SELECT * FROM personen LIMIT 10;                   -- nur die ersten 10
SELECT * FROM personen ORDER BY alter DESC LIMIT 3; -- Top 3 älteste

-- LIMIT mit OFFSET – ab Zeile x starten (für Paginierung):
SELECT * FROM personen LIMIT 10 OFFSET 20;         -- Zeilen 21–30


-- =============================================================================
-- 9. DATEN ÄNDERN – UPDATE
-- =============================================================================
-- VORSICHT: Ohne WHERE → ALLE Zeilen werden geändert!

UPDATE personen SET alter = 37 WHERE id = 1;
UPDATE personen SET stadt = 'Oldenburg', alter = 36 WHERE name = 'Tim';

-- Mehrere Felder gleichzeitig:
UPDATE personen
SET alter = 30, stadt = 'Kiel'
WHERE id = 2;

-- NIEMALS:
-- UPDATE personen SET alter = 0;   ← alle Altersangaben weg. Tschüss, Daten.


-- =============================================================================
-- 10. DATEN LÖSCHEN – DELETE
-- =============================================================================
-- Auch hier: Ohne WHERE → ALLES weg!

DELETE FROM personen WHERE id = 3;
DELETE FROM personen WHERE stadt = 'Berlin';

-- ALLE Zeilen löschen (Tabelle bleibt, Inhalt weg):
DELETE FROM personen;

-- Noch schneller (kein Rollback möglich, setzt AUTO_INCREMENT zurück):
TRUNCATE TABLE personen;


-- =============================================================================
-- 11. AGGREGATFUNKTIONEN – RECHNEN MIT DATEN
-- =============================================================================
-- Funktionen die mehrere Zeilen zusammenfassen.

SELECT COUNT(*) FROM personen;                    -- wie viele Zeilen insgesamt?
SELECT COUNT(alter) FROM personen;                -- wie viele mit Altersangabe (NULL zählt nicht)
SELECT AVG(alter) FROM personen;                  -- Durchschnittsalter
SELECT MIN(alter) FROM personen;                  -- jüngste Person
SELECT MAX(alter) FROM personen;                  -- älteste Person
SELECT SUM(alter) FROM personen;                  -- Summe aller Altersangaben (sinnfrei, aber möglich)

-- Mit Alias schöner:
SELECT
    COUNT(*) AS 'Anzahl',
    AVG(alter) AS 'Durchschnitt',
    MIN(alter) AS 'Jüngster',
    MAX(alter) AS 'Ältester'
FROM personen;


-- =============================================================================
-- 12. GRUPPIEREN – GROUP BY
-- =============================================================================
-- Zeilen nach Wert zusammenfassen und dann aggregieren.
-- Beispiel: Wie viele Personen wohnen in jeder Stadt?

SELECT stadt, COUNT(*) AS anzahl
FROM personen
GROUP BY stadt;

-- Durchschnittsalter pro Stadt:
SELECT stadt, AVG(alter) AS schnitt_alter
FROM personen
GROUP BY stadt;

-- HAVING – wie WHERE, aber für Gruppen (nach GROUP BY):
SELECT stadt, COUNT(*) AS anzahl
FROM personen
GROUP BY stadt
HAVING anzahl > 1;   -- nur Städte mit mehr als 1 Person

-- Reihenfolge der Klauseln:
-- SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT


-- =============================================================================
-- 13. TABELLE ÄNDERN – ALTER TABLE
-- =============================================================================

-- Spalte hinzufügen:
ALTER TABLE personen ADD COLUMN email VARCHAR(200);

-- Spalte umbenennen:
ALTER TABLE personen RENAME COLUMN email TO mail;

-- Spaltentyp ändern:
ALTER TABLE personen MODIFY COLUMN mail VARCHAR(255);

-- Spalte löschen:
ALTER TABLE personen DROP COLUMN mail;

-- Tabelle umbenennen:
RENAME TABLE personen TO users;


-- =============================================================================
-- 14. TABELLE LÖSCHEN
-- =============================================================================

DROP TABLE personen;              -- Tabelle komplett weg (Daten + Struktur)

-- Sicher löschen (kein Fehler wenn nicht vorhanden):
DROP TABLE IF EXISTS personen;


-- =============================================================================
-- 15. JOINS – TABELLEN VERBINDEN
-- =============================================================================
-- Daten aus mehreren Tabellen zusammenführen.
-- Das ist der Kern relationaler Datenbanken.

-- Beispiel: zwei Tabellen
-- Tabelle "kunden":          Tabelle "bestellungen":
-- id | name                  id | kunde_id | produkt
-- 1  | Tim                   1  | 1        | Laptop
-- 2  | Jana                  2  | 1        | Maus
-- 3  | Max                   3  | 2        | Tastatur

CREATE TABLE kunden (
    id   INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE bestellungen (
    id        INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    kunde_id  INT NOT NULL,
    produkt   VARCHAR(100) NOT NULL
);

INSERT INTO kunden (name) VALUES ('Tim'), ('Jana'), ('Max');
INSERT INTO bestellungen (kunde_id, produkt)
VALUES (1, 'Laptop'), (1, 'Maus'), (2, 'Tastatur');

-- INNER JOIN – nur Zeilen, die in BEIDEN Tabellen vorkommen:
SELECT kunden.name, bestellungen.produkt
FROM kunden
INNER JOIN bestellungen ON kunden.id = bestellungen.kunde_id;
-- → Tim: Laptop, Tim: Maus, Jana: Tastatur
-- Max fehlt – hat keine Bestellung

-- LEFT JOIN – ALLE aus linker Tabelle, auch ohne Match rechts:
SELECT kunden.name, bestellungen.produkt
FROM kunden
LEFT JOIN bestellungen ON kunden.id = bestellungen.kunde_id;
-- → Tim: Laptop, Tim: Maus, Jana: Tastatur, Max: NULL

-- RIGHT JOIN – ALLE aus rechter Tabelle (seltener genutzt):
SELECT kunden.name, bestellungen.produkt
FROM kunden
RIGHT JOIN bestellungen ON kunden.id = bestellungen.kunde_id;

-- Mit Alias für Tabellennamen (kürzer schreiben):
SELECT k.name, b.produkt
FROM kunden AS k
INNER JOIN bestellungen AS b ON k.id = b.kunde_id;


-- =============================================================================
-- 16. FREMDSCHLÜSSEL – FOREIGN KEY
-- =============================================================================
-- Sorgt dafür, dass Beziehungen zwischen Tabellen gültig bleiben.
-- Kein Einfügen von bestellung.kunde_id=99 wenn Kunde 99 nicht existiert.

CREATE TABLE bestellungen (
    id        INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    kunde_id  INT NOT NULL,
    produkt   VARCHAR(100) NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

-- Mit Fremdschlüssel kannst du Kaskadenaktionen definieren:
-- ON DELETE CASCADE  → wenn Kunde gelöscht, auch seine Bestellungen löschen
-- ON DELETE SET NULL → wenn Kunde gelöscht, kunde_id auf NULL setzen

CREATE TABLE bestellungen (
    id        INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    kunde_id  INT,
    produkt   VARCHAR(100) NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id) ON DELETE SET NULL
);


-- =============================================================================
-- 17. NÜTZLICHE FUNKTIONEN
-- =============================================================================

-- Text:
SELECT UPPER('hallo');                  -- → HALLO
SELECT LOWER('HALLO');                  -- → hallo
SELECT LENGTH('Tim');                   -- → 3
SELECT CONCAT('Vor', 'name');           -- → Vorname
SELECT CONCAT(name, ' aus ', stadt) AS info FROM personen;
SELECT SUBSTRING('Python', 2, 3);       -- → yth  (Start, Länge)
SELECT TRIM('  hallo  ');               -- → 'hallo' (Leerzeichen weg)
SELECT REPLACE('Hallo Welt', 'Welt', 'SQL');  -- → Hallo SQL

-- Zahlen:
SELECT ROUND(3.14159, 2);              -- → 3.14
SELECT FLOOR(4.9);                     -- → 4  (abrunden)
SELECT CEIL(4.1);                      -- → 5  (aufrunden)
SELECT ABS(-42);                       -- → 42 (absoluter Betrag)

-- Datum:
SELECT NOW();                          -- aktuelles Datum + Uhrzeit
SELECT CURDATE();                      -- nur Datum
SELECT CURTIME();                      -- nur Uhrzeit
SELECT YEAR(NOW());                    -- nur Jahr
SELECT MONTH(NOW());                   -- nur Monat
SELECT DAY(NOW());                     -- nur Tag
SELECT DATEDIFF('2026-12-31', CURDATE());  -- Tage bis Silvester

-- NULL-Behandlung:
SELECT IFNULL(alter, 0) FROM personen;        -- NULL durch 0 ersetzen
SELECT COALESCE(alter, 0) FROM personen;      -- gleiche Funktion, flexibler
SELECT IF(alter >= 18, 'volljährig', 'minderjährig') FROM personen;


-- =============================================================================
-- 18. UNTERABFRAGEN – SUBQUERIES
-- =============================================================================
-- SELECT innerhalb eines SELECT. Wie verschachtelte Schleifen in Python.

-- Wer ist älter als der Durchschnitt?
SELECT name, alter
FROM personen
WHERE alter > (SELECT AVG(alter) FROM personen);

-- In welchen Städten wohnen Kunden die etwas bestellt haben?
SELECT DISTINCT stadt
FROM personen
WHERE id IN (SELECT DISTINCT kunde_id FROM bestellungen);


-- =============================================================================
-- SCHNELLÜBERSICHT – SPICKZETTEL
-- =============================================================================
--
--  Datenbank:      CREATE DATABASE name;
--                  USE name;
--
--  Tabelle:        CREATE TABLE name (spalten...);
--                  DROP TABLE name;
--                  ALTER TABLE name ADD COLUMN ...;
--
--  Einfügen:       INSERT INTO tabelle (spalten) VALUES (...);
--
--  Abfragen:       SELECT spalten FROM tabelle
--                  WHERE bedingung
--                  GROUP BY spalte
--                  HAVING bedingung
--                  ORDER BY spalte ASC|DESC
--                  LIMIT n;
--
--  Ändern:         UPDATE tabelle SET spalte=wert WHERE bedingung;
--
--  Löschen:        DELETE FROM tabelle WHERE bedingung;
--
--  Verbinden:      INNER JOIN ... ON a.id = b.fremdkey
--                  LEFT JOIN  ... ON a.id = b.fremdkey
--
--  Aggregat:       COUNT(*), AVG(), MIN(), MAX(), SUM()
--
--  Wichtig:        IMMER WHERE bei UPDATE und DELETE!
--                  NULL != 0 != ''  →  IS NULL / IS NOT NULL
--
-- =============================================================================
