Title: Extraire des infos thématiques d'OSM
Date: 2016-07-24 19:07
Author: nlehuby
Tags: #osm, #hack, #tuto
Slug: tuto-extraire-infos-osm


Quand on souhaite réaliser une analyse thématique à partir des données OSM, on passe forcément par l'étape de récupération des données.
Pour cela, on a plusieurs solutions.

La plus simple pour se lancer, c'est d'utiliser [Overpass](http://wiki.openstreetmap.org/wiki/Overpass_API), via [Overpass Turbo](http://overpass-turbo.eu/).<br>
J'en ai déjà parlé [dans un précédent article]({filename}initialement_publié_sur_drupalgardens/tuto-faire-une-carte-dynamique.md) : on donne nos contraintes et en un rien de temps, on a un résultat visuel et les objets qui nous intéressent ressortent sur la carte.<br>
On peut alors récupérer directement ces objets ou bien la requête Overpass pour la faire exécuter par un autre applicatif (comme uMap par exemple, cf [mon tutoriel sur le sujet]({filename}initialement_publié_sur_drupalgardens/tuto-faire-une-carte-dynamique.md))

À noter que l'API Overpass permet également de récupérer des objets au format csv, ce qui peut s'avérer pratique s'il s'agit d'une extraction pour analyse (et pas juste pour un affichage). Voici par exemple le nécessaire pour récupérer dans Overpass-Turbo les distributeurs de billets alentours, en csv :

    :::shell
    [out:csv(::"id", ::lat, ::lon, operator)][timeout:25];
    (
        node["amenity"="atm"]({{bbox}});
    );
    out ;

Bref, malgré une courbe d'apprentissage de la syntaxe un peu rude ([Overpass Turbo](http://overpass-turbo.eu/) et le [wiki](http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) sont là pour aider), Overpass, c'est génial !

Cependant, dès qu'on souhaite requêter une trop grande quantité de données, une trop grande surface ou à une fréquence trop élevée, on se retrouve confrontés aux limites de l'API.

Dans ce cas de figure, la solution royale, c'est de récupérer directement toutes les données brutes d'OSM et de faire sa propre extraction à la main.

En général, on télécharge les données, au format [pbf](http://wiki.openstreetmap.org/wiki/PBF_Format), sur [Geofabrik](http://download.geofabrik.de/europe/france.html) par exemple.

Puis, une solution courante est d'insérer ces données en base (avec [imposm](https://imposm.org/) ou [osm2pgsql](http://wiki.openstreetmap.org/wiki/Osm2pgsql)), puis de faire des requêtes SQL pour extraire les infos souhaitées.

Mais, lorsque l'extraction est assez simple, sachez qu'il existe une alternative en ligne de commande, basée sur [Osmosis](http://wiki.openstreetmap.org/wiki/FR:Osmosis) et [Osmconvert](http://wiki.openstreetmap.org/wiki/Osmconvert).

On utilisera osmosis pour ne conserver dans les données que les objets qui nous intéressent.<br>
Puis on utilisera osmconvert pour extraire ces objets au format csv.

Par exemple, si je souhaite extraire tous les distributeurs de billets ([amenity = atm](http://wiki.openstreetmap.org/wiki/FR:Tag:amenity%3Datm)) des données OSM que j'ai téléchargées, je peux procéder ainsi :

    :::shell
    osmosis --read-pbf file="data.osm.pbf" --nkv keyValueList="amenity.atm" --write-pbf atm.osm.pbf

À ce stade, j'ai obtenu un fichier pbf ne contenant que les noeuds taggés avec amenity = atm. Puis, pour avoir tout ça dans un format plus habituel et extraire uniquement les tags qui m'intéressent :

    :::shell
    osmconvert atm.osm.pbf --csv="@id @lat @lon name operator network fee" --csv-headline --csv-separator=";" -o=osm_atm.csv

Et je peux aussi réaliser des unions : par exemple, admettons que je souhaite également récupérer les horloges publiques ([amenity = clock](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dclock)) pour réaliser une analyse particulièrement innovante sur les distributeurs et les horloges ... <br>
Je commence par procéder de même :

    :::shell
    osmosis --read-pbf file="data.osm.pbf" --nkv keyValueList="amenity.clock" --write-pbf clock.osm.pbf

Puis, je fusionne mes deux fichiers précédemment obtenus en un seul :

    :::shell
    osmosis --read-pbf atm.osm.pbf --read-pbf clock.osm.pbf --merge --write-pbf clock_and_atm.osm.pbf

Puis, je peux, comme précédemment utiliser osmconvert pour récupérer les objets et les tags utiles.


À noter que si on souhaite extraire autre chose que des noeuds, il reste possible d'utiliser osmosis, mais c'est un peu plus complexe.<br>
La requête suivante permet par exemple de récupérer les parcours de bus (qui sont des relations taggées avec [route=bus](http://wiki.openstreetmap.org/wiki/Tag:route%3Dbus)) :

    :::shell
    osmosis --read-pbf data.osm.pbf --tf accept-relations route=bus --used-way --used-node --write-pbf route_bus.osm.pbf

On a alors un pbf contenant les relations parcours de bus, ainsi que tous les objets (chemins et noeuds) qui constituent ces relations.
