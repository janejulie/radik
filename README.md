# Radik Portfolio

Dieses Portfolio entstand im Rahmen der Vorlesung "Raumbezogene Daten im interdisziplinären Kontext" im WiSe 2021/2022 an der Johannes-Gutenberg Universität Mainz.

Die weiterführenden Dateien die im Rahmen dieser Übungen entstanden sind befinden sich in den zugehörigen Ordnern des Hauptsverzeichnisses.

## 1 - Atlantis Rekonstruktion

Abgabe zum 2. November 2021

### Problemstellung

Rekonstruktion der fiktiven Insel Atlantis nach Platons-Dialog "Kritias"

### Ergebnis

#### Liste der Geoobjekt

| **#**   | **Name**                               | **Eigenschaften**                                            | **Geometrie** | **Topologie**                               | **Dynamik** | **Proportionen**                                             | **Textstelle**         |
| ------- | -------------------------------------- | ------------------------------------------------------------ | ------------- | ------------------------------------------- | ----------- | ------------------------------------------------------------ | ---------------------- |
| **1**   | Insel Atlantis                         | gehört Poseidon                                              | Polygon       |                                             | ja          |                                                              | 113c                   |
| **2**   | Ebene                                  | schönste; zufriedenstellend an Fruchtbarkeit                 | Polygon       | Mitte von 1; nahe am Meer                   | nein        |                                                              | 113c                   |
| **3**   | Berg/Anhöhe                            |                                                              | Polygon       | Am Rand von 2; ungefähr 50 Stadien vom Meer | nein        | Von allen Seiten von geringer Höhe                           | 113c                   |
| **4**   | Wohngebäude                            | Wohnort einer dreiköpfigen Familie                           | Polygon       | Auf 4  Mittelpunkt von 5*, 6*               | ja          |                                                              | 113c                   |
| **5a**  | Zentrum der Ringe                      |                                                              | Polygon       | Auf 3                                       | ja          |                                                              | 113c                   |
| **6a**  | 1. Ring aus Meer                       |                                                              | Polygon       | Zentral um 5a                               | ja          | 1 Stadien breit                                              | 113d                   |
| **5b**  | 1. Ring aus Land                       |                                                              | Polygon       | Zentral um 6a                               | ja          | 3 Stadien breit; später breiter                              | 113d; 116a             |
| **6b**  | 2. Ring aus Meer                       |                                                              | Polygon       | Zentral um 5b                               | ja          | 2 Stadien breit                                              | 113d                   |
| **5c**  | 2. Ring aus Land                       |                                                              | Polygon       | Zentral um 6b                               | ja          | 3 Stadien breit; später breiter                              | 113d; 113e; 115e; 116a |
| **6c**  | 2. Ring aus Meer                       |                                                              | Polygon       | Zentral um 5c                               | ja          | 3 Stadien breit                                              | 113d                   |
| **7a**  | Kaltwasserquelle                       |                                                              | Punkt         | Auf 5a                                      | ja          |                                                              | 113e                   |
| **7b**  | Warmwasserquelle                       |                                                              | Punkt         | Auf 5a                                      | ja          |                                                              | 113e                   |
| **8**   | Heiliger Bezirk                        | Kleito und Poseidon geweiht; unbetretbar                     | Polygon       | Auf 5a                                      | nein        |                                                              | 116a                   |
| **9**   | Akropolis                              | innerer Stadtkreis                                           | Polygon       | Auf 5a                                      | nein        | 5 Stadien Durchmesser                                        | 113e; 116a             |
| **10**  | Königspalast                           |                                                              | Polygon       | Ehemals 4  innerhalb 9                      | ja          |                                                              | 115c; 116a; 116c       |
| **11a** | Brücke 1. Ring                         |                                                              | Linie         | Über 6a                                     | nein        | 1 Plethron breit                                             | 115c; 116a             |
| **11b** | Brücke 2. Ring                         |                                                              | Linie         | Über 6b                                     | nein        |                                                              | 115c                   |
| **11c** | Brücke 3. Ring                         |                                                              | Linie         | Über 6c                                     | nein        |                                                              | 115c                   |
| **12**  | Kanal                                  |                                                              | Polygon       | Angefangen im Meer  Mündet in 6a            | ja          | 3 Plethren breit; 100 Fuß tief; 50 Stadien lang; breit genug für Schiffe | 115d                   |
| **13a** | Mauer um gesamte Stadt                 | mit Kupfer eingefaßt                                         | Linienring    | Um 6c  50 Stadien Abstand von 6c            | nein        | 1 Plethron breit                                             | 116a                   |
| **13b** | Mauer um innere Stadt                  | mit Zinn überzogen                                           | Linienring    | Um 5a                                       | nein        |                                                              | 116a                   |
| **13c** | Mauer um Akropolis                     | mit Oreichalkos überzogen                                    | Linienring    | Um 9                                        | nein        |                                                              | 116c                   |
| **14a** | Türme der Mauer 13a                    | Steine weiß/rot/schwarz/gemischt                             | Polygon       | An Brücken und Durchlässen zum Meer         | nein        |                                                              | 115d                   |
| **14b** | Türme der Mauer 13b                    | Steine weiß/rot/schwarz/gemischt                             | Polygon       | An Brücken und Durchlässen zum Meer         | nein        |                                                              | 115d                   |
| **15**  | Hohlraum/Durchfahrt                    |                                                              | Linie         | Innerhalb des Felsens                       | ja          | Doppelte Schiffshäuser hoch                                  | 115e; 116b             |
| **16**  | Tempel des Poseidon                    | nicht griechisches Aussehen; mit Silber überzogen; Akrotere gold überzogen; Innenausstattung siehe 116d, 116e | Polygon       |                                             | nein        | 1 Stadion breit; 3 Plethen breit; passend hoch               | 116d                   |
| **17**  | Altar                                  |                                                              | Polygon       | Vor 16 gelegen                              | nein        |                                                              | 117a                   |
| **18a** | Außenbecken                            | unter freiem Himmel                                          | Polygon       | An 7a, 7b                                   | ja          |                                                              | 117b                   |
| **18b** | Innenbecken                            | überdacht; getrennte Bereiche (Könige, Privatleute, Frauen, Zugtiere/Pferde) | Polygon       | An 7a, 7b                                   | ja          |                                                              | 117b                   |
| **19**  | Hain des Poseidon                      |                                                              | Polygon       |                                             | ja          |                                                              | 117b                   |
| **20**  | Hippodrom                              | Für Pferdewettrennen                                         | Linienring    | Auf 5c                                      | nein        | 1 Stadion breit, ganzer Ring                                 | 117c                   |
| **21**  | Wasserabfluss des Beckens              |                                                              | Linie         | Fließt durch 19                             | nein        |                                                              | 117b                   |
| **22a** | Wohnstätte der Leibwache 1             |                                                              | Polygon       | An der Seite von 20  gegenüber 22b          | nein        |                                                              | 117d                   |
| **22b** | Wohnstätte der Leibwache 2             |                                                              | Polygon       | An der Seite von 20  gegenüber 22a          | nein        |                                                              | 117d                   |
| **22c** | Wohnstätte der Leibwache 3 (1. Ring)   |                                                              | Polygon       | Auf 7  näher an Akropolis als 22a, 22b      | nein        |                                                              | 117d                   |
| **22d** | Wohnstätte der Leibwache 4 (Akropolis) |                                                              | Polygon       | Innerhalb der Akropolis                     | nein        |                                                              | 117d                   |
| **23a** | Schiffshaus 1                          |                                                              | Polygon       | An 24a                                      | nein        |                                                              | 115c; 117d             |
| **23b** | Schiffshaus 2                          |                                                              | Polygon       | An 24b                                      | nein        |                                                              | 115c; 117d             |
| **23c** | Schiffshaus 3                          |                                                              | Polygon       | An 25c                                      | nein        |                                                              | 115c; 117d             |
| **24a** | Hafen 1                                |                                                              | Polygon       | An 5a                                       | nein        |                                                              | 117e                   |
| **24b** | Hafen 2                                |                                                              | Polygon       | An 5b                                       | nein        |                                                              | 117e                   |
| **24c** | Hafen 3                                |                                                              | Polygon       | An 5c                                       | nein        |                                                              | 117e                   |
| **25**  | Wohngebiet                             |                                                              | Polygon       | Außerhalb von 6c                            | nein        |                                                              | 117e                   |

### Visualisierung als Vektorzeichnung

![visualisierung](./1-atlantis/visualisierung.png)


# 2 - Erstellung eines eigenen Geopackages

Abgabe zum 9. November 2021

## Problemstellung

Die folgende Abbildung soll mithilfe von QGIS als Geopackage erstellt werden.

![original](./2-owngeopackage/original.png)

## Vorgehensweise

Nach dem Erstellen von Layern kann die "Toggle Editing" Funktion angestellt werden. Diese schaltet das "Vertex Tool" frei mit der die Vorlage "abgepaust" werden kann. Die gegebene Bildvorlage wurde als getrenntes Layer eingeladen um diese nachzuzeichnen. Mit dem Messwerkzeug wurden dann die Durchmesser der Baumkronen als Attribut "duration" hinzugefügt.

Es wurde ein Mercator Projektion verwendet, die jedoch auch verändert werden kann.

![geopackage_comparison](./2-owngeopackage/geopackage_comparison.png)

## Ergebnis

Das Geopackage besteht aus 3 Layern.

| Layer        | Beschreibung                                            |
| ------------ | ------------------------------------------------------- |
| nature_point | Bäume und Quellen. Spezifiert mit Attribut "type"       |
| walls        | Mauern und Brunnenmauer. Spezifiert mit Attribut "type" |
| ways         | alle Wege                                               |

Die Visualisierung ohne der Bildvorlage resultiert in folgender Layer. Dabei haben die Bäume auch die Radien der Baumkronen abgespeichert. Für eine genauer Visualisierung kann man die Punktgröße in Relation dazu setzen.

![geopackage_final](./2-owngeopackage/geopackage_final.png)


# 3 - Bomber's Baedeker

Abgabe zum 16. November 2021

In der Übung wurde bereits das Projekt des Digital Humanities Lab zum "Bomber's Baedeker" [^dhl_bombers] vorgestellt. Die Daten konnten dort erfolgreich extrahiert werden und mithilfe des Dariah-DE Geo-Browsers [^dariah]visualisiert. Es wurde ein Raster in den Daten erkennbar, da die Koordinaten nicht in Grad'Dezimal Einheit, sondern in Grad'Minute angegeben wurde. Diese Visualisierung bezieht sich auf den Datensatz [^git_data] aufgerufen am 13. November 2021 

## Problemstellung

Visualisierung der Geodaten des "Bomber's Baedeker" mit Brücksichtigung der Einheit (Grad'Minuten)

## Vorgehensweise

### Anpassung der Formatierung im csv-Datensatz

In QGIS steht die Funktion zum Einlesen von csv-Daten über den Daten Source Manager bereit. Um die Eingabe in Dezimalwerte umzurechnen, müssen die Längen- und Breitengrade in bestimmtem Format vorliegen.  [^stackexchange]

Beispielsweise wird aus dem Längengrad `50.47` entweder `50 47` oder  `50'47`. 

Folgendes Python-Skript ändert in der csv-Datei die Punkte zu Leerzeichen.

```python
import csv
with open('../data.csv') as csvDataFile:
    with open('../data_new_format.csv', 'w', encoding='UTF8') as f:
        reader = csv.reader(csvDataFile)
        writer = csv.writer(f)
        for row in reader:
            row[3] = " ".join(row[3].split('.'))
            row[4] = " ".join(row[4].split('.'))
            writer.writerow(row)
```

### Erstellen eines Geopackages mithilfe des Data Source Managers

Wie üblich kann der Data Source Manager verwendet werden um ein Geopackage Layer aus csv-Daten zu erstellen. Bisher wurde keine Umrechnung der Daten durchgeführt. Die QGIS-interne Umrechnung wählt man mit der Funktion `DMS-coordinates` aus.

![Einstellungen im Data Source Manager](./3-bomber/DMS.png)

### Ergebnis der Visualisierung

Im Vergleich der alten Koordinaten (grün) und der neuen Koordinaten (rot) ist die Rasterbildung nicht mehr deutlich.

![Alte Koordinaten im Vergleich zu neuen Koordinaten](./3-bomber/old_vs_new.png)


### Vergleich der Lage mit OpenStreetMap

Um die Korrektheit der Lage zu prüfen wurde im letzten Schritt die XYZ Tiles der OpenStreetMap [^osm_tiles]verwendet. 

![FFM1](./3-bomber/FFM1.png)

Auch wenn die Daten zu einem anderen historisch Zeitpunkt erhoben wurden, sieht man eine Abweichung der Lage im Vergleich zur OpenStreetMap. Ein Muster wurde auf den ersten Blick nicht erkennbar. Eine Verschiebung des "Ursprungs" ist ausgeschlossen. Sieht man von einer möglichen Ungenauigkeit der Daten ab (Wahl des Punktes einer Stadt, ...), stellt sich die Frage, ob die korrekte Projektion angewendet wurde.


#  4 - Google Earth Pro Alternativen

Abgabe zum 23. November 2021

Ideen:

- Koordinatensysteme
- Google Earth
- Projektionssysteme
- Ein Container bauen? 

## Alternativen zu Google Earth Pro

### Marble

Die Website der Software [^marble]

- open-source
- Desktop Applikation und Mobile Version (Marble Maps) verfügbar
- am weitesten verbreitete Alternative
- beinhaltet topologische Karte
- beinhaltet Straßenkarte (aus OpenStreetMap)
- beinhaltet Satellitenbilder
- deutlich kleinerer Datensatz

### WorldWind

Die Website der Software [^worldwind]

- open-source
- Projekt der NASA Learning Technology
- beinhaltet topologische Karte
- beinhaltet Straßenkarte (aus OpenStreetMap)
- beinhaltet Satellitenbilder
- deutlich kleinerer Datensatz
- implementiert mit Java + OpenGL 

### Alternativ

Statt einer Installation auf dem eigenen Recher kann Google Earth Pro auch in Virtuellen Boxen wie Turbo.net o.Ä verwendet werden. 


#  5 - Topologie AtlantGIS

Abgabe zum 30. November 2021

## Vorgehensweise

Der Datensatz wurde als GitHub-Repository geforked und ist unter https://github.com/janejulie/AtlantGIS hochgeladen. 
Um in ein bestehendes Git-Repository in ein weiteres Repository einzubinden wird "git submodules" ausprobiert.
Die Shape-Files sind als Layer in QGIS hochgeladen worden und die Visualisierung des Datensatzes nachgestellt. 

## Ergebnis
Mit GitHub Submodules wurde gearbeitet, um die Vorteile eines Git-Repositorys zu verwenden [^git_submodules].
Ohne das Projekt als Submodule einzubinden, kann das geforkede AtlantGIS nicht aktualisiert werden. Operationen wie git pull/commit/push können bei einer Kopie nicht durchgeführt werden. Innerhalb des Projektes wäre dann eine Kopie von AtlantGIS hinterlegt, die Änderungen und insbersondere Verbesserungen nicht einfach aktualisieren kann. Dafür müsste dann eine erneute Kopie des Projektes heruntergeladen werden. Die Versionierung des Projekts geht dabei verloren.

Das Ergebnis der Visualisierung sieht folgendermaßen aus.

![visualization_atlantgis](./5-atlantGIS/visualization.png)

# 6 -  Raum und Zeit in GIS

Abgabe zum 7. Dezember 2021

## Fragestellung

Wie berechnet ORBIS [^orbis] die kürzeste Distanz zwischen zwei Städten?

## Ergebnis

Für die Ermittlung des kürzesten Weges wird der Dijkstra Algorithmus verwendet. Dieser Algorithmus berechnet bei einem gegebenen Startpunkt die kürzeste Distanz zu den anden Knoten. Da die verschiedenen Wege mit unterschiedlichen Transportmitteln überquert werden, muss hier die gewichtete und gerichtete Variante des Algorithmus benutzt werden. Durch die Gewichtung der Pfade steuert ORBIS die verschiedenen Suchprofile (kürzester, billigster, schnellster Pfad).

Der Dijkstra-Algorithmus [^dijk_wiki] markiert zunächst alle Knoten außer dem Startknoten als 'besucht' und weist ihnen den Wert unendlich zu. Dem Startknoten wird der Wert Null zugewiesen. Vom Startknoten aus werden jetzt alle Nachbarn (Knoten, die eine Kante zum Startknoten haben) besucht und der Wert dann überschieben, wenn der Weg nun kürzer ist. Zyklisch wird dieses Prinzip jetzt für alle Nachbarn dieser Knoten angewandt. Sind alle Knoten besucht und die Nachbarn überprüft sind die Werte, die am Ende im Knoten stehen die, die den günstigsten Wert beschreiben. Um zusätzlich zum kleinsten Wert auch den idealen Pfad zu erhalten, wird in den Knoten nicht nur der Wert, sondern auch der Knoten abgespeichert, der zu diesem führt. Dann kann ausgehend vom Zielknoten der Pfad rekonstruiert werden. 

Im Beispiel wird die Route von London nach Rom gesucht. 

![orbis](./6-topologie/orbis.png)


# 7 - Geodatenmodelle

Abgabe zum 14. Dezember 2021

## Fragestellung

Welche Arten gibt es um die Delaunay Triangulation zu erstellen? [^delauney_wiki_en] [^delauney_wiki_de] [^delauney_mit]

## Ergebnis

Der mathematische Hintergrund beruht auf die Detektion eines Punktes in dem Kreisumfang. Dafür wird die Determinante (s. [^delauney_wiki_de]) der Punkte verwendet.

### Flip-Algorithmus

Es wird eine zufällige Belegung der Dreiecke ermittelt. Erst danach wird geprüft ob die Bedingung ("Der Umkreis eines Dreiecks des Netzes darf keine weiteren Punkte der vorgegebenen Punktmenge enthalten") für alle Dreiecke erfüllt ist. Wird die Bedingung verletzt, wird sie lokal behoben indem die Kante "geflipt" wird. Dieser namensgebende Mechanismus verbindet die zuvor nicht verbunden Punkte mit einer Kante und entfernt die bereits Bestehende. Da jedoch dieses Problem anschließend global gelöst werden muss, hat der Algorithmus eine quadratische Worst-Case Laufzeit.

Der Pseudocode für die Implementierung [^delauney_wiki_de]
``` 
 1: Initialisiere die leeren Mengen V, E, T und K = (V, E, T)
 2: Markiere alle Kanten e ∈ E
 3: Füge alle Kanten e ∈ E dem Stack s hinzu
 4: Solange der Stack s nicht leer ist:
 5:     Entferne die Kante ei,j vom Stack s und entmarkiere ei,j
 6:     Falls die Kante ei,j die Umkreisbedingung nicht erfüllt:
 7:         ek,l = Flip der Kante ei,j
 8:         Berechne L(ek,l)
 9:         Für alle Kanten e ∈ {ek,j, ej,l, el,i, ei,j}:
10:             Falls die Kante e nicht markiert ist:
11:                 Markiere die Kante e und lege die Kante e oben auf den Stack s
```

### mit Laufzeit O(n log(n))

Um Laufzeit zu sparen kann die inkrementelle Konstruktion, der Divide-and-Conquer oder der Sweep Algorithmus verwendet werden. Diese benötigen O(n log(n)) Laufzeit und sind somit effizienter. Im Austausch wird in der Regen mehr Speicherplatz benötigt, da die Suche beschleunigt wird, indem die Punkte in einer effizienteren Datenstruktur abgelegt werden.

### dreidimensionaler Raum

Für einen dreidimensionalen Raum wird häufig die Höhe vernachlässigt und stattdessen mit den x,y Koordinaten im zweidimensionalem Raum gerechnet. Erst anschließend werden die Höhen wieder berücksichtigt.

--- 

Ab hier wurde das Gis-Projekt zu Karabalgasun begonnen.

## Fußnoten
[^stackexchange]: https://gis.stackexchange.com/questions/180729/can-qgis-plot-coordinates-in-degrees-minutes-format
[^dhl_bombers]:https://dhlab.hypotheses.org/1820
[^git_data]: https://github.com/ieg-dhr/bombers_baedeker/blob/main/visualisation/coords_dariah_format.csv
[^osm_tiles]:  https://tile.openstreetmap.org/${z}/${x}/${y}.png
[^marble]: https://marble.kde.org
[^worldwind]: https://worldwind.arc.nasa.gov
[^git_submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[^orbis]: https://orbis.stanford.edu/#
[^dijk_wiki]: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
[^delauney_wiki_en]: https://en.wikipedia.org/wiki/Delaunay_triangulation
[^delauney_wiki_de]: https://de.wikipedia.org/wiki/Delaunay_triangulation
[^delauney_mit]: https://web.mit.edu/alexmv/Public/6.850-lectures/lecture09.pdf

