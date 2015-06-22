# OpenStreetMap Paraguay Data

We realized that one of the most used mirror of OpenStreetMap (Geofabrik) doesn't
have the Paraguay map, so we created ourselves.

The idea is to show them we exists and try to make/help them to
include this map. It's the only one from South America that it's not
included in their mirror and we don't know why.


# Steps to create Paraguay map

1. Download south-america.osm.pbf
```
wget -c http://download.geofabrik.de/south-america-latest.osm.pbf
```

1. Crop the map using the `paraguay.poly` file

```
./osmconvert \
    south-america-latest.osm.pbf \
	-B=paraguay.poly \
	--out-pbf \
	-o=south-america-paraguay.osm.pbf
```

# How to get the `paraguay.poly` file

We use this website to get the `paraguay.poly` file:

- http://polygons.openstreetmap.fr/
  - Paraguay: http://polygons.openstreetmap.fr/?id=287077

