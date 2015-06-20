# OpenStreetMap data

- Geofabrik.de: http://download.geofabrik.de/south-america-latest.osm.pbf

- OpenStreetMap:

# osmconvert

```
./osmconvert \
    /media/humitos/Seagate\ Expansion\ Drive/osm-data-extract/south-america-latest.osm.pbf \
	-B=paraguay.poly \
	--out-pbf \
	-o=/media/humitos/Seagate\ Expansion\ Drive/osm-data-extract/south-america-paraguay.osm.pbf \
	-t=/media/humitos/Seagate\ Expansion\ Drive/osm-data-extract/osmconvert_tempfile.`date +"%s"`
```

```
./osmconvert \
    /media/humitos/Seagate\ Expansion\ Drive/osm-data-extract/south-america-paraguay.osm.pbf \
	-o=/media/humitos/Seagate\ Expansion\ Drive/osm-data-extract/south-america-paraguay.osm \
	-t=/media/humitos/Seagate\ Expansion\ Drive/osm-data-extract/osmconvert_tempfile.`date +"%s"`
```

# Splitter

http://www.mkgmap.org.uk/download/splitter.html

# Polígono de Paraguay

http://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format

# Crear un polígono

- http://polygons.openstreetmap.fr/
  - Paraguay: http://polygons.openstreetmap.fr/?id=287077

- http://www.naturalearthdata.com/

# Cortar un .osm mediante un .poly

http://wiki.openstreetmap.org/wiki/Osmconvert

# Información útil

- Información técnica sobre geofabrik.de: http://download.geofabrik.de/technical.html
