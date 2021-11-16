# Atlantis Rekonstruktion (2/11/21)

## Problemstellung



## Vorgehensweise

# Erstellung eines eigenen Geopackages (9/11/21)

## Problemstellung



## Vorgehensweise



# Raumkonzeptionen (16/11/21)

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

![Einstellungen im Data Source Manager](/Users/jenekabro/Library/Mobile Documents/com~apple~CloudDocs/Campus/RaDiK/4-bomber/DMS.png)

### Ergebnis der Visualisierung

Im Vergleich der alten Koordinaten (grün) und der neuen Koordinaten (rot) ist die Rasterbildung nicht mehr deutlich.

![Alte Koordinaten im Vergleich zu neuen Koordinaten](/Users/jenekabro/Library/Mobile Documents/com~apple~CloudDocs/Campus/RaDiK/4-bomber/old_vs_new.png)



### Vergleich der Lage mit OpenStreetMap

Um die Korrektheit der Lage zu prüfen wurde im letzten Schritt die XYZ Tiles der OpenStreetMap [^osm_tiles]verwendet. 

![FFM1](/Users/jenekabro/Library/Mobile Documents/com~apple~CloudDocs/Campus/RaDiK/4-bomber/FFM1.png)

Auch wenn die Daten zu einem anderen historisch Zeitpunkt erhoben wurden, sieht man eine Abweichung der Lage im Vergleich zur OpenStreetMap. Ein Muster wurde auf den ersten Blick nicht erkennbar. Eine Verschiebung des "Ursprungs" ist ausgeschlossen. Sieht man von einer möglichen Ungenauigkeit der Daten ab (Wahl des Punktes einer Stadt, ...), stellt sich die Frage, ob die korrekte Projektion angewendet wurde.

## Fußnoten

[^stackexchange]: https://gis.stackexchange.com/questions/180729/can-qgis-plot-coordinates-in-degrees-minutes-format
[^dhl_bombers]:https://dhlab.hypotheses.org/1820
[^git_data]: https://github.com/ieg-dhr/bombers_baedeker/blob/main/visualisation/coords_dariah_format.csv
[^osm_tiles]:  https://tile.openstreetmap.org/${z}/${x}/${y}.png

