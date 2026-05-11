
-- Datenbank: `outerdatenbank`
--
DROP DATABASE IF EXISTS `outerdatenbank`;
CREATE DATABASE IF NOT EXISTS `outerdatenbank` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `outerdatenbank`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `abteilungen`
--

CREATE TABLE `abteilungen` (
  `ID` int(11) NOT NULL,
  `Abteilungsname` varchar(24) COLLATE utf8_german2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `abteilungen`
--

INSERT INTO `abteilungen` (`ID`, `Abteilungsname`) VALUES
(1, 'Lager'),
(2, 'Vertrieb');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `abteilungen2`
--

CREATE TABLE `abteilungen2` (
  `abteilungsname` varchar(20) COLLATE utf8_german2_ci DEFAULT 'Lager',
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `abteilungen2`
--

INSERT INTO `abteilungen2` (`abteilungsname`, `ID`) VALUES
('Lager', 1),
('Vertrieb', 2),
('Einkauf', 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `deleteme`
--

CREATE TABLE `deleteme` (
  `id` int(11) NOT NULL DEFAULT 0,
  `nachname` varchar(40) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL,
  `vorname` varchar(40) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL,
  `geschlecht` char(2) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL DEFAULT 'm',
  `gehalt` decimal(8,2) DEFAULT 1100.00,
  `Abteilung` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `fahrzeuge3`
--

CREATE TABLE `fahrzeuge3` (
  `kennzeichen` varchar(12) COLLATE utf8_german2_ci NOT NULL,
  `id_mitarbeiter` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `fahrzeuge3`
--

INSERT INTO `fahrzeuge3` (`kennzeichen`, `id_mitarbeiter`) VALUES
('HH-JK-101', 3),
('HH-JK-111', 5),
('OL-JK-103', 0),
('HH-JK-117', 0);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `gehaelter2`
--

CREATE TABLE `gehaelter2` (
  `id` int(11) NOT NULL DEFAULT 0,
  `nachname` varchar(40) COLLATE utf8_german2_ci NOT NULL,
  `vorname` varchar(40) COLLATE utf8_german2_ci NOT NULL,
  `geschlecht` char(2) COLLATE utf8_german2_ci NOT NULL DEFAULT 'm',
  `gehalt` decimal(8,2) DEFAULT 1100.00,
  `Abteilung` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `gehaelter2`
--

INSERT INTO `gehaelter2` (`id`, `nachname`, `vorname`, `geschlecht`, `gehalt`, `Abteilung`) VALUES
(1, 'Meyer', 'Michael', 'm', '1248.70', 1),
(2, 'Müller', 'Martin', 'm', '1430.20', 1),
(3, 'Lenz', 'Ludwig', 'm', '1304.90', 1),
(4, 'Freisenbruch', 'Frank', 'm', '1334.00', 1),
(5, 'Jäger', 'Jaqueline', 'w', '1367.70', 2),
(6, 'Montagne', 'Marcel', 'm', '1881.10', 2),
(7, 'Schröder', 'Manfred', 'm', '1702.40', 2),
(8, 'Richter', 'Jörg', 'm', '1768.30', 2),
(0, 'Praktisch', 'Peter', 'm', NULL, NULL),
(-1, 'M%ller', 'V%', 'm', '1100.00', NULL),
(666, 'N.', 'N.', 'f', '3000.00', NULL),
(9, 'Freigeist', 'Frank', 'm', '1484.81', 3),
(10, 'Hurtig', 'Heike', 'w', '1659.94', 3),
(11, 'Clever', 'Claas', 'm', '1835.06', 3),
(12, 'Denker', 'Desiree', 'w', '1310.19', 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kursnutzungen`
--

CREATE TABLE `kursnutzungen` (
  `id_kurs` int(11) NOT NULL,
  `id_mitarbeiter` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `kursnutzungen`
--

INSERT INTO `kursnutzungen` (`id_kurs`, `id_mitarbeiter`) VALUES
(3, 4),
(4, 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `lehrgaenge`
--

CREATE TABLE `lehrgaenge` (
  `id` int(11) NOT NULL,
  `bezeichnung` varchar(40) COLLATE utf8_german2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `lehrgaenge`
--

INSERT INTO `lehrgaenge` (`id`, `bezeichnung`) VALUES
(3, 'Steuerrecht 2016'),
(4, 'Grundlagen des Verwaltungsrechts'),
(5, 'Work/Life Balance'),
(1, 'First steps in Business English');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `mitarbeiter`
--

CREATE TABLE `mitarbeiter` (
  `id` int(11) NOT NULL,
  `nachname` varchar(40) COLLATE utf8_german2_ci NOT NULL,
  `vorname` varchar(40) COLLATE utf8_german2_ci NOT NULL,
  `geschlecht` char(2) COLLATE utf8_german2_ci NOT NULL DEFAULT 'm'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `mitarbeiter`
--

INSERT INTO `mitarbeiter` (`id`, `nachname`, `vorname`, `geschlecht`) VALUES
(1, 'Meyer', 'Michael', 'm'),
(2, 'Müller', 'Martin', 'm'),
(3, 'Lenz', 'Ludwig', 'm'),
(4, 'Freisenbruch', 'Frank', 'm'),
(5, 'Jäger', 'Jaqueline', 'w'),
(6, 'Montagne', 'Marcel', 'm'),
(7, 'Schröder', 'Manfred', 'm'),
(8, 'Richter', 'Jörg', 'm'),
(9, 'Lancôme', 'René', 'm'),
(11, 'Mustermann', 'Max', 'm');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `mitarbeiter2`
--

CREATE TABLE `mitarbeiter2` (
  `id` int(11) NOT NULL DEFAULT 0,
  `nachname` varchar(40) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL,
  `vorname` varchar(40) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL,
  `geschlecht` char(2) CHARACTER SET utf8 COLLATE utf8_german2_ci NOT NULL DEFAULT 'm'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Daten für Tabelle `mitarbeiter2`
--

INSERT INTO `mitarbeiter2` (`id`, `nachname`, `vorname`, `geschlecht`) VALUES
(1, 'Meyer', 'Michael', 'm'),
(2, 'Müller', 'Martin', 'm'),
(3, 'Lenz', 'Ludwig', 'm'),
(4, 'Freisenbruch', 'Frank', 'm'),
(5, 'Jäger', 'Jaqueline', 'w'),
(6, 'Montagne', 'Marcel', 'm'),
(7, 'Schröder', 'Manfred', 'm'),
(8, 'Richter', 'Jörg', 'm'),
(9, 'Lancôme', 'René', 'm'),
(11, 'Mustermann', 'Max', 'm');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `parkplaetze`
--

CREATE TABLE `parkplaetze` (
  `pid` int(11) NOT NULL,
  `name` varchar(20) COLLATE utf8_german2_ci NOT NULL,
  `id_mitarbeiter` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

--
-- Daten für Tabelle `parkplaetze`
--

INSERT INTO `parkplaetze` (`pid`, `name`, `id_mitarbeiter`) VALUES
(1000, 'West I', NULL),
(1001, 'Nord II', 3),
(1002, 'Nord III', NULL),
(2000, 'Nord II', NULL),
(2001, 'Ost I', NULL),
(2002, 'Ost II', 1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `telefonnummern`
--

CREATE TABLE `telefonnummern` (
  `telefon` varchar(18) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `telefonnummern`
--

INSERT INTO `telefonnummern` (`telefon`) VALUES
('06669574760'),
('060728148250'),
('0472418703324'),
('0457985739'),
('06715515948'),
('061104372071'),
('0475198915093'),
('0462470646'),
('06761751595'),
('0477995176518');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `abteilungen`
--
ALTER TABLE `abteilungen`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `abteilungen2`
--
ALTER TABLE `abteilungen2`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `gehaelter2`
--
ALTER TABLE `gehaelter2`
  ADD KEY `fk_abteilungen2_gehaelter2` (`Abteilung`);

--
-- Indizes für die Tabelle `mitarbeiter`
--
ALTER TABLE `mitarbeiter`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `parkplaetze`
--
ALTER TABLE `parkplaetze`
  ADD PRIMARY KEY (`pid`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `abteilungen2`
--
ALTER TABLE `abteilungen2`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT für Tabelle `mitarbeiter`
--
ALTER TABLE `mitarbeiter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `gehaelter2`
--
ALTER TABLE `gehaelter2`
  ADD CONSTRAINT `fk_abteilungen2_gehaelter2` FOREIGN KEY (`Abteilung`) REFERENCES `abteilungen2` (`ID`);
COMMIT;

