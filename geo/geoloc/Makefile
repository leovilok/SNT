INTRO_FILES = intro.html GPS24goldenSML-CCBYSA-Paulsava.gif

COORDS_FILES = coordonnees/coordonnees.html \
               coordonnees/equirect-map-latitude.png \
               coordonnees/equirect-map-longitude.png \
               coordonnees/equirect-map-coordonnees.png

TRILAT_FILES = trilateration/trilateration.html trilateration/equirect-map-bg.png trilateration/gps-sat.png trilateration/temps.png trilateration/trilat-1.png trilateration/trilat-2.png trilateration/trilat-3.png

geoloc.zip: imsmanifest.xml $(COORDS_FILES) $(INTRO_FILES) $(TRILAT_FILES)
	apack $@ $^

%.html: %.md
	pandoc $< -o $@

intro.html: intro.md

coordonnees/coordonnees.html: coordonnees/coordonnees.md

trilateration/trilateration.html: trilateration/trilateration.md

