Title: osm-transit-extractor, le couteau suisse pour les transports dans OSM
Date: 2018-05-01 19:31
Author: nlehuby
Tags: #osm, #junglebus
Slug: osm-transit-extractor-couteau-suisse


Si vous êtes utilisateur de données OpenStreetMap, que ce soit pour faire des cartes, des applicatifs géographiques, ou juste des analyses, vous connaissez sûrement les outils en ligne de commande de la communauté : [osmosis](https://wiki.openstreetmap.org/wiki/FR:Osmosis), [osmium](https://wiki.openstreetmap.org/wiki/Osmium) ou encore [osmconvert](https://wiki.openstreetmap.org/wiki/Osmconvert).<br>
J'ai moi-même déjà évoqué certains de ces outils dans [un précédent article](https://nlehuby.5apps.com/tuto-extraire-infos-osm.html).

Mais lorsqu'on est intéressé(e) par les lignes de transports, ces outils ne sont pas des plus pratiques, car il est nécessaire de manipuler des relations OSM, c'est-à-dire des objets un brin complexes constitués eux-mêmes d'autres objets.

Bien sûr, la bonne vieille solution Overpass reste envisageable si la zone n'est pas trop grosse. Jetez un œil à [cet autre article](https://nlehuby.5apps.com/overpass-bus.html) pour trouver la requête qu'il vous faut ;)

Mais dans tous les cas, il nous faudra jongler dans nos filtres pour récupérer les relations de type route ou route_master avec certains tags uniquement car [les circuits de marche nordique](https://wiki.openstreetmap.org/wiki/Tag:route%3Dnordic_walking) ou encore les [pipelines vraiment très longs](https://wiki.openstreetmap.org/wiki/Tag:route%3Dpipeline) sont cartographiés d'une manière très similaire...

C'est pourquoi je suis ravie de vous présenter [osm-transit-extractor](https://github.com/CanalTP/osm-transit-extractor), une alternative qui apporte enfin aux transports en commun toute l'attention qu'ils méritent ;)

Pour un cas pratique, imaginons donc que vous voulez vous faire une idée des lignes de transports de Bretagne.

osm-transit-extractor se présente sous la forme d'un exécutable (Linux uniquement pour le moment) : il suffit donc de le télécharger [depuis Github](https://github.com/CanalTP/osm-transit-extractor/releases) puis de le dézipper pour l'utiliser.

Ensuite, on récupère les données de la zone qui nous intéresse, ici [la région Bretagne](http://download.geofabrik.de/europe/france/bretagne.html), au format PBF.

Et c'est parti :

`./osm_transit_extractor -i bretagne-latest.osm.pbf`

Oui, c'est tout !

On obtient alors un petit ensemble de fichiers csv avec les données qui nous intéressent.

Les 3 fichiers les plus intéressants sont

- les arrêts : `osm-transit-extractor_stop_points.csv`
- les parcours : `osm-transit-extractor_routes.csv`
- les lignes : `osm-transit-extractor_lines.csv` (relations route_master dans OSM)


Ces fichiers contiennent à la fois les informations utiles sur ces objets ainsi que tous les tags OSM, mais aussi les géométries de ces objets.<br>
Ces fichiers csv peuvent donc s'utiliser aussi bien dans un tableur (ou autre) pour une analyse des métadonnées, ou dans QGIS (ou autre) pour une représentation cartographique.

Voici par exemple un extrait des infos de quelques lignes :
![capture d'écran des infos de lignes]({attach}images/20190501_osm_transit_extractor/lines_metadata.png)

Et voici une petite représentation de ces lignes, réseau par réseau :
![capture d'écran des lignes de Bretagne dans QGIS, et en couleurs aléatoires]({attach}images/20190501_osm_transit_extractor/lines_wkt.png)

Notre extraction comprend également des fichiers pour faire le lien entre les différents objets, par exemple entre une ligne et ses différents parcours, ou entre un parcours et ses arrêts.

Voici par exemple la liste des parcours de la ligne de Ferry Brest Ouessant :
![capture d'écran de line_route]({attach}images/20190501_osm_transit_extractor/line_route.png)

Voici encore un extrait des arrêts de la ligne 9 de Kicéo en direction de Meucon :
![capture d'écran de route_stop]({attach}images/20190501_osm_transit_extractor/route_stop.png)

Et ce n'est qu'un aperçu : osm-transit-extractor est un vrai petit couteau suisse, rapide et efficace dès qu'on veut des infos sur les lignes de transports dans OSM.

Bien sûr, c'est opensource, donc n'hésitez pas à passer sur [github](https://github.com/CanalTP/osm-transit-extractor/issues) si vous rencontrez des soucis ou avez des idées d'évolutions. Et si vous êtes un rustacéen, vos contributions sont les bienvenues ;)
