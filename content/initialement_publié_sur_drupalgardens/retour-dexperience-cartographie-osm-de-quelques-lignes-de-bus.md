Title: Retour d'expérience -  cartographie OSM de quelques lignes de bus
Date: 2014-04-15 10:22
Author: nlehuby
Tags: #osm
Slug: retour-dexperience-cartographie-osm-de-quelques-lignes-de-bus


Bon, maintenant qu’on a indiqué les lignes qui s’arrêtaient à la gare de
Boissy ([ici]({filename}retour-dexperience-cartographie-osm-dune-gare-routiere-1-2.md), puis
[là]({filename}retour-dexperience-cartographie-osm-dune-gare-routiere-2-2.md)), pourquoi ne pas aller
plus loin et cartographier carrément les lignes entières ?!

</p>

Je me suis livrée à cette expérience sur les lignes que j’emprunte
occasionnellement, notamment la ligne J1, du transporteur STRAV, puis
des portions des lignes 12 et 23 de l’opérateur SETRA.

</p>

**Avant-après, ligne J1**

</p>

![image : cet arrêt]({attach}img/media_crop/36/public/201405/zoomlarge-tc-sansj1.png)

</p>
![image : cet arrêt]({attach}img/media_crop/41/public/201405/j1-ok.png)


</p>

**Première étape : le terrain**

</p>

La première étape est similaire à précédemment, ça consiste à monter
dans le bus et à enregistrer une trace GPS.

</p>

La partie difficile à ce niveau est de bien noter les bus\_stop (et
éventuellement leurs caractéristiques : banc, abri), en particulier si
l’arrêt n’est pas demandé par les voyageurs qui sont dans le bus …

</p>

De retour sur son PC, on peut attaquer la saisie :

</p>

-   Vérifier si des relations correspondant aux lignes et aux parcours
    existent déjà

    </p>

    -   Si non, les créer
-   Puis, pas forcément dans cet ordre :

    </p>

    -   Créer les arrêts de bus
    -   Ajouter les arrêts de bus aux relations
    -   Ajouter les chemins empruntés aux relations

**Deuxième étape : la création des relations**

</p>

Avant de créer quoique ce soit, il faut vérifier si ça n’existe pas
déjà !

</p>

Par une petite recherche dans le
[wiki](http://wiki.openstreetmap.org/wiki/WikiProject_France/Transports_en_Île-de-France)
tout d'abord

</p>

Par une petite recherche dans les données OSM :

</p>

Dans [overpass-turbo](http://overpass-turbo.eu/), je demande toutes les
relations, qui ont comme tag network = SITUS (par exemple)

</p>

![image : overpass]({attach}img/201404_carto_ligne_bus/overpass.png)

</p>

 

</p>

 En l’occurrence, je les ai déjà créés précédemment donc on peut sauter
cette étape ;)

</p>

Mais j’ai été étonnée de trouver des lignes du réseau SITUS déjà
cartographiée !

</p>

 

</p>

**Troisième étape : la saisie des arrêts et l’ajout à la relation**

</p>

Je commence par saisir les arrêts. Certains existent déjà, d’autres non.

</p>

Puis comme précédemment, je les ajoute à mes relations.

</p>

Là, il y a des petites choses amusantes : parfois il y a déjà un arrêt
qui existe, mais pas exactement au même endroit : comment savoir si
c’est le même déjà existant (et dans ce cas, s’il est bien positionné)
ou s’il y en a plusieurs assez proches ? Dans ce cas, un second passage
sur le terrain s’impose !

</p>

Certains arrêts ont déjà un tag local\_ref = J1, ce qui donne le rendu
suivant sur OSM avec la couche de calque Transports :

</p>

![image : calque Transports]({attach}img/201404_carto_ligne_bus/couche_tc.png)

</p>

Sur la ligne 23, j’ai également rencontré la problématique suivante :

</p>

Les arrêts de bus n’étaient pas marqués comme des arrêts de bus mais
comme des terminaux permettant d’acheter des tickets*amenity =
vending\_machine* (ce qui est effectivement le cas, ce sont des arrêts
de bus à haut niveau de service :p).

</p>

J’ai voulu ajouter juste le tag précisant que c’est un arrêt de bus
(*highway = bus\_stop*).

</p>

Mais [Osmose](http://osmose.openstreetmap.fr/) (un outil de détection
d'erreurs et d'incohérences dans les données OSM), remonte ceci comme
une erreur :

</p>

![image : osmose]({attach}img/201404_carto_ligne_bus/osmose.png)

</p>

 

</p>

J’ai donc fait dû faire deux points très proches, l’un portant la vente
de ticket et l’autre l’arrêt de bus.

</p>

 

</p>

À part ces quelques cas particuliers très locaux, c’est une manipulation
assez rébarbative, mais assez simple.

</p>

Quoique la ligne J1 m’a donné un peu de fil à retordre, car elle est un
peu spéciale :

</p>

-   C’est une ligne circulaire (Villeneuve-Saint-Georges vers
    Villeneuve-Saint-Georges en passant par Boissy-Saint-Léger)
-   Et en forme de 8 (un arrêt est desservi plusieurs fois !)
-   Avec un unique sens (le sens retour existe, mais c’est en fait la
    ligne J2)
-   Mais avec quand même des parcours spéciaux, car il y a des arrêts
    scolaires qui ne sont desservis qu’une à deux fois par jour !

Si j’avais su, j’aurais commencé par une plus « normale » !

</p>

![image : J1]({attach}img/media_crop/J1-complet.png)


</p>

Ça m’a au moins permis de résoudre un mystère : habituellement, je ne le
prenais que pour quelques arrêts, mais effectivement, je m’étais souvent
étonnée du fait que la girouette du bus indiquait parfois
Boissy-Saint-Léger, et parfois Villeneuve Saint-Georges, mais que les
annonces sonores dans le bus disaient toujours « Ligne J1 en direction
de gare de Villeneuve Saint-Georges »…

</p>

 

</p>

**Quatrième étape : l’ajout des routes dans la relation**

</p>

Ceci fait, il ne reste plus qu’à ajouter les routes empruntées par le
bus dans les relations.

</p>

 

</p>

Là, il n’y a qu’une petite subtilité (qu’on ne peut apprécier qu’au
moment de l’étape 5) :

</p>

Dans le cas où le bus tourne avant la fin de la route telle qu’elle est
tracée sur OSM, ça donne des choses inexactes et plutôt moches en terme
de rendu :

</p>

![image : rendu tout moche]({attach}img/201404_carto_ligne_bus/avec-j1-moche.png)


</p>

La solution est ici de couper le chemin (là, j’avoue, je n’ai pas trouvé
toute seule, j’ai demandé un peu d’aide à la communauté OSM) :

</p>

 

</p>

Dans JOSM, quand je survole la relation, les éléments se mettent en
surbrillance :

</p>
![image : capture d'écran de JOSM]({attach}img/201404_carto_ligne_bus/josm3.png)

</p>

Ensuite, il suffit de cliquer à l’endroit où on veut tronçonner le
chemin, donc sur le point de séparation, puis de taper P (ou
sélectionner Données \>  Couper le chemin)

</p>

![image : capture d'écran de JOSM]({attach}img/201404_carto_ligne_bus/josm4.png)

</p>

J’ai maintenant deux chemins (sur la capture, j’en ai sélectionné juste
un, ce qui n’était pas possible avant) :

</p>
![image : capture d'écran de JOSM]({attach}img/201404_carto_ligne_bus/josm2.png)


</p>

Puis, il ne reste plus qu’à modifier la relation pour supprimer le bout
de chemin qui ne devrait pas y être :

</p>


![image : capture d'écran de JOSM]({attach}img/201404_carto_ligne_bus/josm1.png)


</p>

 

</p>

Vous remarquerez au passage dans JOSM que le fait de cliquer sur un
membre le met en surbrillance sur la carte, ce qui permet de ne pas
supprimer le mauvais ;)

</p>

Ne pas oublier d’enregistrer, sinon, il faudra le refaire trois fois …

</p>

 

</p>

Voilà le résultat final :

</p>

![image : résultat final]({attach}img/201404_carto_ligne_bus/avecj1-mieux.png)



</p>

 

</p>

**Cinquième étape : ~~admirer~~ vérifier son travail !**

</p>

Sur le wiki, les liens du modèle (que j'ai déjà évoqué dans [le premier
article]({filename}retour-dexperience-cartographie-osm-dune-gare-routiere-1-2.md)) peuvent être utiles
pour vérifier son travail :

</p>

![image : wiki]({attach}img/201404_carto_ligne_bus/wiki.png)

</p>

La première vérification, la plus immédiate, est l’affichage de la
relation dans OSM (c’est le premier lien du modèle inséré dans le
wiki**) :**

</p>
![image : wiki]({attach}img/201404_carto_ligne_bus/relation_wiki.png)


</p>
<p>
<address>
Exemple avec la ligne 12 (je n’ai cartographié que la moitié, le reste
était déjà présent)
</address>
</p>

 

</p>

Le dernier lien du modèle est également très intéressant, il
reconstruit, à partir des données OSM, le thermomètre de la ligne :

</p>

![image : thermo overpass]({attach}img/201404_carto_ligne_bus/overpass-thermo.png)

</p>
<p>
<address>
Exemple sur la ligne 12
</address>
</p>

 

</p>

Et enfin, il y a [le rendu de la couche
transport](http://www.thunderforest.com/transport/), mais c’est moins
immédiat, car il est mis à jour sur une base régulière plus espacée.

</p>

 

</p>

Voilà pour ce petit retour d’expérience sur la cartographie d’une ligne
de bus, qui j’espère suscitera des vocations ;)

</p>
<p>
