Title: Du GTFS à OpenStreetMap
Date: 2020-09-01 19:08
Author: nlehuby
Tags: #osm, #junglebus
Slug: de-gtfs-a-osm


Votre réseau de bus préféré a publié ses données en open data en GTFS et vous voulez les utiliser pour vérifier la complétude d'OpenStreetMap et voir ce qui peut être amélioré ? Voici quelques conseils pour se lancer !

## GTFS WTF ?

Le GTFS est un format fréquemment utilisé pour décrire des données de transport. Il permet de définir les caractéristiques et la géographie du réseau, ainsi que ses horaires. Ce format est largement utilisé pour alimenter les logiciels et services de calcul d'itinéraire et d'information voyageur, mais aussi les outils de planification et d'amélioration du réseau. C'est donc tout naturellement sous cette forme que vous pourrez trouver les données des lignes et arrêts de bus publiées par votre opérateur ou collectivité.

![Qu'est-ce que le GTFS ? Image CC-BY-SA Jungle Bus, issue de l'infographie https://junglebus.io/osm-puis-gtfs-ou-gtfs-puis-osm/]({attach}images/20200901_gtfs/GTFS_wtf.png)


Un fichier GTFS se présente sous la forme d'un fichier zip contenant tout un tas de fichiers texte. Malgré leur extension, il s'agit en réalité de fichiers csv qui peuvent être ouverts dans votre logiciel de tableur favori (LibreOffice Calc, Excel, etc).<br>
La [documentation](https://github.com/google/transit) décrivant le contenu des fichiers, le détail des colonnes et comment les lier entre elles est disponible en ligne.

Afin de se faciliter la tâche, j'utiliserai ici non pas le fichier GTFS directement, mais un export réalisé avec l'outil [GTFS geo](https://gtfs-geo.herokuapp.com/). Il permet en effet de transformer un fichier GTFS en un ensemble de fichiers géographiques, plus adaptés pour notre mission du jour et qui s'importeront aisément dans la plupart des outils d'éditions d'OpenStreetMap.

![capture d'écran de l'interface de GTFS geo]({attach}images/20200901_gtfs/gtfs_geo.png)

NB : Comme je le dis souvent, open data ne veut pas dire open bar, donc avant de commencer à modifier quoique ce soit, vérifiez que vous pouvez utiliser ces données pour enrichir OpenStreetMap.

## étape 1 : les arrêts

L'étape la plus simple à réaliser est une comparaison des arrêts.

Ils sont dans le fichier `stops.csv`.
*Pour obtenir un résultat similaire à partir du GTFS, il faut changer l'extension du fichier en csv, renommer les colonnes `stop_lat` et `stop_lon` en latitude et longitude, et filtrer le contenu pour ne conserver que ceux qui ont un `location_type = 0`.*

Je vous conseille de l'ouvrir tout d'abord dans un tableur pour estimer la qualité du nommage des arrêts (TOUT EN MAJUSCULE ? avec des abréviations ? etc). Regardez aussi si le `stop_code` ou le `stop_id` correspondent à un numéro visible sur les arrêts (par exemple un code pour obtenir aux prochains passages en temps réel à cet arrêt ?) : si c'est le cas, cela correspond à des données utiles à ajouter à OpenStreetMap.

![aperçu des arrêts d'un GTFS exporté avec GTFS geo]({attach}images/20200901_gtfs/apercu_stops.png)

Ensuite, il peut être intéressant de les afficher sur une carte pour un premier état des lieux (umap, QGIS ou tout simplement JOSM avec un fond OSM ou d'imagerie aérienne de qualité). Cela donne déjà un premier aperçu et peut permettre de détecter des erreurs grossières (des arrêts situés hors de la zone du réseau, voire en plein milieu de la mer).

![aperçu des arrêts dans JOSM]({attach}images/20200901_gtfs/stops_josm_1.png)

Ce qui nous intéresse vraiment à ce stade est la précision du positionnement des arrêts sur la carte : les arrêts sont-ils situés plutôt sur la route, à coté de la route ou dans des bâtiments ?

![aperçu des arrêts dans JOSM]({attach}images/20200901_gtfs/stops_josm_2.png)
![aperçu des arrêts dans JOSM]({attach}images/20200901_gtfs/stops_josm_3.png)

Il faut aussi vérifier la manière dont les arrêts sont modélisés :  en effet, les arrêts du GTFS ne correspondent pas forcément à des arrêts tels qu'on peut les observer sur le terrain. On peut tout à fait avoir un unique arrêt GTFS pour les deux sens de circulation d'une ligne, même s'il correspond à deux abribus sur le terrain, ou à l'inverse plusieurs arrêts (un pour chaque ligne) pour représenter un arrêt de bus desservi par plusieurs lignes.

![aperçu des arrêts dans JOSM]({attach}images/20200901_gtfs/stops_mapcontrib_1.png)

Bref, il faut passer un peu de temps à explorer les données pour identifier les petites surprises qui risqueraient de nous complexifier la tâche.

Une fois que nous sommes familiarisés avec les arrêts du GTFS, nous pouvons attaquer la comparaison avec OpenStreetMap. Pour cela, on peut par exemple charger le fichier des arrêts dans [ce thème MapContrib](https://www.cartes.xyz/t/e7200d-Arrets_de_bus#). JOSM est également un très bon choix pour cette tâche.

![aperçu des arrêts dans JOSM]({attach}images/20200901_gtfs/stops_mapcontrib_2.png)

Si ce n'est pas encore fait, je vous conseille au préalable de passer un peu de temps à uniformiser les arrêts déjà présents dans OpenStreetMap pour la zone. Sans cela, il vous sera peut-être difficile de [répondre à des questions très simples](https://nlehuby.5apps.com/mais-je-veux-juste-la-liste-des-arrets-de-bus.html) comme "combien y a t-il d'arrêts de bus dans cette ville ?" en utilisant OpenStreetMap. <br>
En effet, comme pour le GTFS, [plusieurs modélisations](https://nlehuby.5apps.com/bien-cartographier-les-bus.html) sont possibles, autant sur le positionnement de l'arrêt (sur la route, ou à côté) que sur les tags : respectez donc les pratiques locales lorsqu'elles existent. Sinon, je recommande la modélisation suivante, qui est compatible avec la plupart des rendus et outils qui tirent partie des données transport d'OpenStreetMap : un arrêt est représenté par un unique objet, placé à côté de la route, avec les tags `highway = bus_stop` et `public_transport = platform`.

![aperçu des arrêts dans JOSM]({attach}images/20200901_gtfs/model_arret.png)

Après ce petit intermède de jardinage des données existantes, on peut s'attaquer à la comparaison et à l'enrichissement des arrêts d'OpenStreetMap à partir du GTFS. <br>
Pensez à croiser les sources et à vous appuyer sur l'imagerie aérienne ou les photos de rue sous licence compatible ;)

Repérez aussi s'il y a des arrêts existants dans OpenStreetMap qui ne sont pas représentés dans les données open data (la navette gratuite mise en place par la mairie ou un autre réseau de transport que celui sur lequel vous travaillez).

Dans JOSM, vous pouvez utiliser le [plugin todo](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/TODO_list) pour constituer une liste d'arrêts et les vérifier dans l'ordre très rapidement.

![Le plugin TODO de JOSM]({attach}images/20200901_gtfs/josm_todo_plugin.png)

Si les résultats des étapes précédentes sont plutôt bons (les données GTFS sont de bonne qualité, avec des noms propres et des positions précises et proches de la modélisation adoptée par OpenStreetMap), vous pouvez par exemple utiliser le [plugin Conflation](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Conflation) de JOSM pour passer rapidement en revue les différences.

![Le plugin conflation de JOSM]({attach}images/20200901_gtfs/josm_conflation_plugin.png)

Vous pouvez également créer une analyse Osmose : c'est un excellent outil pour réaliser des intégrations de données dans OpenStreetMap à partir d'une source open data. De plus, Osmose permet de travailler plus facilement à plusieurs et plus tard de suivre les évolutions apportées dans les données (autant GTFS qu'OpenStreetMap).

![une analyse Osmose]({attach}images/20200901_gtfs/stops_osmose.png)

Bref, à l'issue de cette étape, vous avez mis en qualité les arrêts de votre réseau : c'est déjà un bel accomplissement, félicitations ! Nous pouvons donc passer aux lignes !


## étape 2 : état des lieux des lignes et parcours

L'édition des lignes de transport dans OpenStreetMap est réputée difficile, mais pas de panique : avec un peu de pratique et de méthode, ce n'est pas si dur !

Chaque ligne est constituée d'un ou plusieurs parcours, qui représentent les trajets effectivement suivis par les véhicules et les arrêts qui sont desservis dans l'ordre. Dans le cas général, on aura deux parcours pour chaque ligne (un pour l'aller et un pour le retour), mais de nombreuses exceptions existent : la ligne circulaire avec un unique trajet, la ligne en fourche avec 3 ou 4 trajets différents et réguliers, le détour du mercredi matin pour éviter la place du marché ou le détour tous les matins et tous les soirs pour passer devant le lycée, etc

Dans OpenStreetMap, chaque parcours sera représenté une relation de `type = route`. Cette relation contiendra les arrêts dans l'ordre et les rues et routes empruntées par le bus. Puis on regroupera tous les trajets d'une même ligne dans une relation de `type = route_master`.

Avant d'aller plus loin et de se pencher sur les données GTFS, je vous conseille, comme pour les arrêts, de passer un peu de temps à mettre en qualité les données déjà dans OpenStreetMap. En particulier, on ajoutera si nécessaire des tags sur les parcours et lignes pour indiquer le transporteur (`operator`) et le réseau (`network`) afin qu'on puisse différencier facilement les lignes de notre réseau et celles du réseau national de car ou des navettes de la mairie. On vérifiera également que chaque parcours est bien rattaché à une ligne (les relations `route` sont membres de relation `route_master`) sans quoi répondre à la question du nombre de lignes dans la ville risque d'être une opération difficile.

Pour cette étape, pensez à activer les [validateurs JOSM Jungle Bus](https://github.com/Jungle-Bus/transport_mapcss), qui vous indiqueront les choses à corriger dans les données existantes.

![Activer les validateurs Jungle Bus de JOSM]({attach}images/20200901_gtfs/josm_junglebus_rules.png)

Vous pouvez également retrouver la plupart de ces contrôles qualité dans [Osmose](https://osmose.openstreetmap.fr/fr/map/#item=1260%2C2140%2C8040%2C9014). Jetez aussi un œil à la version bêta de [Bifidus](https://jungle-bus.github.io/bifidus/index.html), qui vous permet de les mettre en valeur sur une carte sur une zone donnée.

![Jettez un oeil à la version bêta de Bifidus]({attach}images/20200901_gtfs/bifidus_beta.png)

Regardons à présent les lignes et les parcours du GTFS.

GTFS geo vous propose un fichier csv contenant les parcours. Une colonne indique la ligne d'appartenance et le nombre d'arrêts.

![Aperçu des lignes et parcours]({attach}images/20200901_gtfs/apercu_trips.png)

*Dans le GTFS, vous obtiendrez la liste des lignes dans le fichier `routes.txt`. Pour trouver les parcours de chaque ligne, il faut utiliser le fichier `trips.txt`, filtré par `route_id`, et en ne conservant que ceux qui ont la même séquence d'arrêts (qu'on retrouve dans le fichier `stop_times.txt`).*

En fonction de la complexité des lignes, il vous faudra peut-être faire des choix dans ces parcours : on peut toujours dans un premier temps se concentrer sur les parcours les plus réguliers (le trajet le plus fréquent est plus pertinent à cartographier que la variante qui ne passe que le mercredi à 10h30). 

La grille horaire de la ligne, lorsqu'elle est disponible, offre une visualisation des différents trajets assez efficace et peut-être utile pour identifier ceux que l'on souhaite cartographier et ceux qu'on se garde pour plus tard.

![Aperçu des lignes et parcours]({attach}images/20200901_gtfs/exemple_grille_horaire.png)

À partir de tout cela, vous devez avoir une première vision du nombre de parcours et de lignes déjà existants dans OpenStreetMap et à compléter, ainsi que de ceux à créer entièrement.

Pour suivre votre avancement, je conseille d'initier une page de wiki, pour avoir une liste cible des lignes et parcours et mesurer l'avancement. [La page suivante](https://wiki.openstreetmap.org/wiki/France/Bus_Pep%27s) peut vous servir de modèle si vous n'êtes pas familiarisé avec la syntaxe du wiki.

![Un tableau d'avancement dans le wiki]({attach}images/20200901_gtfs/apercu_wiki.png)

Cette page de wiki est également le bon endroit pour rappeler les bons tags à mettre sur les lignes (pour uniformiser les tags `operator` et `network` par exemple) et la manière de cartographier les arrêts.

Bref, à l'issue de cette étape, vous avez une vision d'ensemble sur votre réseau : les lignes et parcours existants et ceux qui sont à créer. Nous allons à présent regarder en détail chaque parcours un par un et le compléter.

## étape 3 : les parcours et leurs arrêts

Prenons donc un parcours : dans GTFS Geo, chaque parcours est associé à un fichier geojson, qui comprend les métadonnées, les arrêts et le tracé du trajet.

*Dans le GTFS, vous obtiendrez les métadonnées des trajets en fusionnant les informations des fichiers `routes.txt` et `trips.txt` en utilisant la colonne `route_id` pour raccrocher chaque trajet à sa ligne. Les trajets présents dans `trips.txt` ont une notion d'horaire et de calendrier associés, donc il vous faudra sans doute au préalable choisir un trajet représentatif unique. La liste des arrêts du trajet est disponible dans le fichier `stop_times.txt` en utilisant le `trip_id` pour filtrer. Enfin, il vous faudra également utiliser le `stop_id` pour retrouver dans le fichier `stops.txt` le nom et les coordonnées de ces arrêts.*

Vous pouvez donc ouvrir le fichier geojson dans JOSM pour visualiser un parcours.

![Un parcours dans JOSM]({attach}images/20200901_gtfs/josm_trip_1.png)

Il vous faut alors reprendre la relation du parcours associé ou à la créer si nécessaire à partir des infos fournies par le GTFS. N'oubliez pas de mettre cette relation de parcours (`type=route`) dans la relation de ligne (`type=route_master`) associée.

Puis, en suivant le geojson, il n'y a plus qu'à retrouver les arrêts (déjà créés dans OpenStreetMap à l'étape 2) et à les ajouter, dans l'ordre où ils sont desservis dans la relation.

![Ajouter les arrêts dans la relation avec JOSM]({attach}images/20200901_gtfs/add_stop_in_josm.gif)

Enfin, avant de passer au parcours suivant ou à l'étape suivante, n'oubliez pas de mettre à jour le wiki avec votre avancement.

![Avancement des arrêts sur le wiki]({attach}images/20200901_gtfs/wiki_stop_progress.gif)

## étape 4 : les tracés des parcours

En complément des arrêts de chaque parcours, on souhaitera également ajouter le tracé, qui se matérialise dans OpenStreetMap par la suite des rues empruntées par le bus.

Dans GTFS Geo, ce tracé est présent dans le fichier geojson de chaque parcours. Le tracé est une information facultative dans le GTFS : lorsqu'elle n'est pas fourni, le geojson contiendra uniquement des lignes droites reliant les arrêts dans l'ordre.

![Un parcours dans JOSM]({attach}images/20200901_gtfs/josm_trip_2.png)

*Dans le GTFS, vous obtiendrez les éventuels tracés des trajets dans le fichier `shapes.txt`. Il s'agit d'une suite de points qu'il vous faudra relier. Vous pouvez faire le lien entre le tracé et le trajet GTFS en utilisant la colonne `shape_id` des fichiers `shapes.txt` et `trips.txt`. Le fichier `shapes.txt` est facultatif. S'il n'est pas fourni, à vous de retrouver le chemin emprunté par le véhicule entre les arrêts !*

Pour ajouter ce tracé dans OpenStreetMap, ouvrez la relation du parcours, puis sélectionner une à une les rues et les ajouter à la relation.

Si vous avez beaucoup de parcours ou des lignes particulièrement longues, je vous invite à tester quelques plugins JOSM : 

- [PT Assistant](https://wiki.openstreetmap.org/wiki/FR:JOSM/Greffons/PT_Assistant) et son assistant de routing. Ce plugin est par ailleurs indispensable pour cartographier des lignes de transport dans JOSM : il ajoute de nombreux tests de qualité et facilite la visualisation des objets importants. L'essayer, c'est l'adopter !
- [Relation Toolbox](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Relation_Toolbox), qui permet d'accélérer l'ajout de plusieurs objets dans une relation

![Le plugin PT Assistant]({attach}images/20200901_gtfs/josm_ptassistant_plugin.png)
> PT Assistant permet (entre autres) de visualiser beaucoup plus facilement le parcours de bus sélectionné, ses arrêts, leur ordre ainsi que le tracé.

Et enfin, lorsque c'est fait, le wiki est à mettre à jour en conséquence comme pour les arrêts.

![Avancement des tracés sur le wiki]({attach}images/20200901_gtfs/wiki_shape_progress.gif)


## étape 5 : profitez !

Vous avez créer tous les arrêts puis toutes les lignes et tous les parcours, et enfin ajouté les arrêts et rues dans tous ces parcours ? Félicitations ! 

Vous pouvez maintenant à présent retrouver ces données sur les rendus transport d'openstreetmap.org (il y a parfois plusieurs jours de décalage, soyez patients).

![Avancement sur fond transport]({attach}images/20200901_gtfs/seine_et_marne_bus.gif)

Le détail des informations de chaque ligne est également explorable depuis [Unroll](https://jungle-bus.github.io/unroll/) :

![Unroll, pour visualiser le détail d'une ligne]({attach}images/20200901_gtfs/unroll.png)

Jetez aussi un œil à l'application mobile OSMAnd, qui permet également de [naviguer dans ces données de transport](https://nlehuby.5apps.com/plus_de_bus_osmand.html) et même de calculer des itinéraires en bus !

Et ce n'est pas tout, les sites ou applications qui utilisent les données de transport d'OpenStreetMap sont de plus en plus nombreux : jetez un oeil à la [page de wiki qui les référence](https://wiki.openstreetmap.org/wiki/FR:Public_transport/Tools#Visualisation) pour trouver encore plus de choses cools à faire avec ces nouvelles données !