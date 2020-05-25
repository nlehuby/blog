Title: Mais je veux juste la liste des arrêts de bus !?
Date: 2017-08-10 21:17
Author: nlehuby
Tags: #osm, #junglebus
Slug: mais-je-veux-juste-la-liste-des-arrets-de-bus

Il y a quelques années, quand quelqu'un voulait réaliser une extraction OSM des arrêts de bus, il se retrouvait confronté à un problème : 


* pour certains, un arrêt de bus est un lieu sur le bord de la route, où des voyageurs attendent leur bus
* pour d'autres, c'est un endroit sur la voirie, où un bus s'arrête 

La nuance peut sembler légère, mais cela peut jouer sur la volumétrie : lorsqu'on a deux abribus en face, on peut se retrouver avec deux arrêts selon la première définition, mais un unique arrêt avec la seconde...

Pour résoudre ce souci, la communauté OSM a planché [sur une nouvelle modélisation](https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport) des arrêts (entre autres), qui a été adoptée par vote en 2011.

Deux nouveaux attributs viennent compléter le modèle : l'un désigne l'endroit sur la chaussée où le bus s'arrête (public_transport = stop_position), et l'autre désigne l'endroit où les voyageurs attendent (public_transport = platform).<br>
Un problème, une solution, [KISS](https://fr.wikipedia.org/wiki/Principe_KISS) ! 

Vraiment ?

Admettons, pour les besoins de l'exercice, que je sois intéressée par les arrêts de bus, au sens "les endroits où les voyageurs attendent leur bus".<br>
Facile donc, si je veux extraire tous les arrêts de France, je n'ai qu'à filtrer mes données OSM sur le tag public_transport = platform.

Voici les résultats de mon extraction (sur des données du 4 aout 2017) : en France métropolitaine, on a d'après OSM, 45 408 arrêts où attendent des voyageurs.

Là, si le résultat ne vous choque pas, croyez-moi sur parole : ce n'est pas crédible.<br>
Rien qu'en Île-de-France, on a déjà environ 40 000 arrêts de transport en commun, donc, même si la base OSM n'est pas exhaustive, ce n'est pas vraiment le bon ordre de grandeur.

Ok, par curiosité, si j'utilise le tag historique higwhay = bus_stop, qu'est-ce que ça donne ?<br>
123 956 arrêts. Déjà plus crédible.

Mais souvenez-vous, pour certains, un arrêt de bus désigne un endroit sur la route, et moi je veux les abribus et les poteaux où les gens attendent. Essayons de combiner : si je prends les highway = bus_stop qui ne sont *pas* des public_transport = stop_position : 98 173 arrêts.

Bon, si je regarde dans le détail, je trouve que la plupart de ces arrêts n'ont pas le tag public_transport de renseigné du tout. Difficile de savoir quelle proportion de ceux là sont dont des stop_position qui ne m'intéressent pas.

Au final, combien ai-je d'arrêts ? 45 mille, 98 mille ou 124 mille ?<br>
Bref, six ans après l'adoption du nouveau schéma, extraire les arrêts de bus est une opération qui reste hasardeuse...

Exigeons plus ! Et si, en tant que contributeur OSM, on appliquait le schéma et qu'on ajoutait scrupuleusement _stop_position_ ou _platform_ sur tous les higwhay=bus_stop ?<br>
Une analyse Osmose est déjà disponible pour identifier les arrêts à compléter : [c'est par ici que ça se passe](http://osmose.openstreetmap.fr/en/errors/?item=2140&class=21411), et c'est très facile à corriger !


Même si cela ne suffira pas, ce sera déjà la première marche vers plus de réutilisabilité des données OSM \o/


Et en cadeau, si vous être arrivés jusque là dans cet article passionnant, voici des représentations cartographiques de la répartition de ces différentes combinaisons d'attributs.
![corrélation entre la cartographie du tag public_transport = platform et le vote Macron aux législatives. Nan je déconne]({attach}images/20170810_mais_je_veux_juste_la_liste_des_arrets_de_bus/bus_stop_public_transport.gif)


NB : Cet article comprend des approximations et simplifications pédagogiques.<br>
D'ailleurs, si vous les avez remarquées, n'hésitez pas à venir prolonger la discussion sur la liste de diffusion _transport_ de la communauté OSM France,  [par ici](http://listes.openstreetmap.fr/wws/info/transport) ;)
