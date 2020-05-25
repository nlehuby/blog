Title: Analyse des arrêts d'un parcours de bus
Date: 2017-01-21 22:07
Author: nlehuby
Tags: #osm
Slug: analyse-arrets-bus


Quand je parle de mon trouble obsessionnel cartographique favori, les lignes de bus, les gens me demandent parfois si je trouve encore des choses à cartographier sur cette thématique, surtout en Île-de-France, où OSM est déjà très riche et densément mappé.<br>
Mais c'est une fausse impression de complétude : il y a encore beaucoup à faire et bien que j'ai commencé en 2014 (souvenez-vous, je vous ai fait découvrir mes expériences [sur ce blog]({filename}initialement_publié_sur_drupalgardens/retour-dexperience-cartographie-osm-de-quelques-lignes-de-bus.md)), je continue de contribuer régulièrement sur cette thématique.

D'après le référentiel opendata du STIF, il y a plus de 1800 lignes (tous modes confondus) alors qu'à date dans OSM, on en a moins de 500.<br>
Pourtant, il suffit de jetter un coup d'oeil au fond transport pour constater que les contributeurs sont très actifs sur cette thématique.<br>
En effet, la donnée brute existe déjà en grande partie dans OSM, mais il reste pas mal de travail d'uniformisation sur les tags établis.<br>
Car, cartographier une ligne de bus, ce n'est pas si facile ! Mais ça sera surement l'object d'un prochain article tutoriel ;)<br>
Concentrons nous donc plutôt sur les arrêts.

Voici quelques captures des arrêts du parcours de la ligne 306 du réseau RATP en direction de Saint-Maur, dans l'opendata (le petit point en bout de flèche) et dans OSM (le picto à la base de la flèche)
![un arrêt OSM et son arrêt opendata associé]({attach}images/20170121_analyse_stif/marroniers.png)

La distance entre les deux sources est très variable.<br>
Pour certains, l'arrêt opendata est à moins de 10 mètres de l'arrêt OSM :
![un pas bien loin]({attach}images/20170121_analyse_stif/distance_petite.png)
Mais dans d'autres, il faut rechercher à 150 mètres pour le retrouver :
![et un bien plus loin]({attach}images/20170121_analyse_stif/distance_longue.png)

Cette grande distance semble souvent imputable à la précision de géoloc des données opendata, mais il s'agit aussi parfois d'arrêt OSM positionnés approximativement (souvent signalés avec un tag FIXME : position à corriger).<br>
Sans vouloir faire des généralisations hâtives, il semblerait qu'on constate assez systématiquement des grands écarts de distance sur les gares routières, où l'opendata se contente du centre de la gare.
![une gare routière]({attach}images/20170121_analyse_stif/noisy.png)

Mais malgré ça, on arrive quand même à trouver un arrêt opendata pour chaque arrêt OSM \o/<br>
Deux exceptions :<br>

* Un arrêt manque à l'appel dans OSM : l'arrêt Rue du Monument. ![need survey]({attach}images/20170121_analyse_stif/rue_du_monument.png)
* Des arrêts semblent être en trop dans OSM : il y a en effet trois arrêts Villiers-sur-Marne–Le Plessis-Trévise RER rattachés à ce parcours de bus.![also need survey]({attach}images/20170121_analyse_stif/villiers.png) L'un est indiqué comme étant un arrêt de descente pour tous les bus, ce qui est en effet une pratique répendue dans les gares routières, mais l'un des deux autres est clairement en trop. Fausse manip d'un contributeur ou défaut de mise à jour ?

Bref, même sur cette ligne qui semble plutôt complète, il reste des imprécisions.

À noter qu'on trouve aussi de belles imprécisions dans l'opendata, avec :

* des arrêts à l'intérieur de bâtiments ![c'est pratique ceci dit, d'attendre son bus au chaud]({attach}images/20170121_analyse_stif/st_maur.png)
* des arrêts pas situés dans la bonne rue ![bon courage pour choper ce bus si tu l'attends dans cette rue]({attach}images/20170121_analyse_stif/plateau.png)

Si vous souhaitez vous faire votre propre idée sur les lignes qui passent près de chez vous, voici quelques éléments pour reproduire mon analyse :<br>
Pour les arrêt OSM, j'ai utilisé une extraction via l'API Overpass de type

    :::shell
    relation({id de la relation});node(r:"{platform ou stop selon la version du schéma}");out meta;


Il vous faudra renseigner

* l'id de la relation du parcours
* "stop" s'il s'agit d'un parcours encore en public_transport:version = 1 ou "platform" s'il s'agit d'un public_transport:version = 2.

Pour les arrêts opendata, j'ai réalisé une extraction par parcours à l'aide de l'API [navitia.io](http://navitia.io) car filtrer les données opendata par parcours est un peu fastidieux. Cela me permet également de récupérer l'identifiant de l'arrêt dans le référentiel STIF dans la foulée.<br>
Le script python est sur [github](https://github.com/nlehuby/OSM_snippets/blob/master/analyse_ref_STIF/extract_stops_of_a_route.py).<br>
On peut ensuite visualiser ça dans JOSM à l'aide du plugin opendata.

Pour faire le rapprochement entre l'opendata et OSM, j'ai utilisé le plugin conflation de JOSM.

Cette analyse est très orienté parcours, mais on peut imaginer qu'une fois que le référentiel des arrêts du STIF aura été proprement intégré dans OSM on pourra réaliser cela par quartier, ou tout autre découpage, géographique ou non.<br>
Mais c'est un peu prématuré ... Sur le parcours en question, seuls 11 arrêts disposaient de leur identifiant STIF, et 4 étaient erronés.<br>
![argh, des ref:FR:STIF fausses]({attach}images/20170121_analyse_stif/ref_pas_bonnes.png)
La cause est difficile à déterminer à ce stade : il s'agit parfois de la référence d'un arrêt desservi par la ligne 306 dans l'autre sens, et parfois d'une référence qui n'existe pas ou plus dans le référentiel du STIF.

Bref, même en Île-de-France, il reste du boulot sur les arrêts de bus :)
