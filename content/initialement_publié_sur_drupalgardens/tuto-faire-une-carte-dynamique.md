Title: [tuto] Faire une carte dynamique
Date: 2015-02-23 21:26
Author: nlehuby
Tags: #osm, #hack, #tuto
Slug: tuto-faire-une-carte-dynamique


Ce que j’apprécie particulièrement avec OpenStreetMap, c’est que c’est
un écosystème très riche et qu’on peut découvrir chaque jour un nouveau
truc génial à faire avec.

</p>

Voici un petit exemple d’une fonctionnalité que j’ai découverte
récemment, et utilisée dans [mon précédent article sur les points de
collecte de recyclage de
verre]({filename}ou-recycler-son-verre.md).

</p>

EDIT 2019 - cet article est un peu daté. Voir aussi le tutoriel de fgouget sur le même thème : [Comment j'ai créé une carte mondiale des boîtes à livres en quelques minutes](http://fgouget.free.fr/osm/boitesalivres.shtml)
 

</p>

OpenStreetMap, c’est avant tout une grosse base de données. Mais pour
mettre en évidence ces données, il faut avoir un certain niveau de
connaissance d’OpenStreetMap.

</p>

Voici un solution simple pour afficher des données issues de la base OSM
sur un fond de carte (OSM, évidemment), avec mise à jour automatique des
données en fonction des modifications apportées sur la base par les
contributeurs.

</p>

<iframe frameborder="0" height="300px" src="https://umap.openstreetmap.fr/fr/map/boulangeries_26977?scaleControl=false&amp;miniMap=false&amp;scrollWheelZoom=false&amp;zoomControl=true&amp;allowEdit=false&amp;moreControl=true&amp;datalayersControl=true&amp;onLoadPanel=undefined" width="100%"></iframe>

[Voir en plein
écran](http://umap.openstreetmap.fr/fr/map/boulangeries_26977)

</p>

Ici, une carte des boulangeries de Paris présentes dans OSM.

</p>

 

</p>

Pour récupérer les données, on utilisera par exemple l’API Overpass.

</p>

Et comme faire une requête Overpass qui fonctionne du premier coup est
une opération un peu hasardeuse, on utilisera bien sûr [Overpass
Turbo](http://overpass-turbo.eu/).

</p>

Le tag pour une boulangerie est le suivant : [shop =
bakery](http://wiki.openstreetmap.org/wiki/FR:Tag:shop=bakery?uselang=fr)

</p>

En utilisant le wizard d'Overpass Turbo, on obtient le résultat
suivant :

</p>

![image : export Overpass ]({attach}img/201501/export.png)

</p>

Le résultat est ok, mais un peu moche.

</p>

Pour aller plus loin, on va afficher ces données dans
[uMap](http://umap.openstreetmap.fr/fr/), un service opensource de
création de carte personnalisable simple d’accès.

</p>

 

</p>

uMap permet en effet de choisir un fond de carte OSM et d’y ajouter des
données de la provenance de son choix, de personnaliser un peu le design
général, puis de partager sa carte.

</p>

 

</p>

Il nous faut donc indiquer à uMap où trouver les données à afficher.

</p>

Pour cela, dans Overpass Turbo : Exporter \> Requête \> format compact

</p>

![image : overpass turbo]({attach}img/201501/export1.png)

</p>

On obtient alors les paramètres, sous un format compact, à passer à
l’API Overpass pour avoir un résultat.

</p>

Pour obtenir ce résultat, il faut passer ces paramètres à une instance
Overpass (par exemple, [l’instance mondiale
« principale »](http://api.openstreetmap.fr/oapi/interpreter?data=) ou
[l’instance française](http://overpass-api.de/api/interpreter?data=)).

</p>

En concaténant les deux bouts de mon url, j’ai une requête que me
retourne les données OSM au format json :

</p>

[http://api.openstreetmap.fr/oapi/interpreter?data=[out:json][timeout:25]...](http://api.openstreetmap.fr/oapi/interpreter?data=[out:json][timeout:25];%28node[%22shop%22=%22bakery%22]%2848.84726471793433,2.370729446411133,48.86273852508843,2.385792732238769%29;way[%22shop%22=%22bakery%22]%2848.84726471793433,2.370729446411133,48.86273852508843,2.385792732238769%29;relation[%22shop%22=%22bakery%22]%2848.84726471793433,2.370729446411133,48.86273852508843,2.385792732238769%29;%29;out%20body;%3E;out%20skel%20qt;)

</p>

Muni de cette précieuse requête, allons sur uMap créer notre jolie
carte !

</p>

Sur une carte, les données sont regroupées par « calque ».

</p>

Créons une carte.

</p>

Par défaut, elle contient un seul calque, vide, appelé calque 1.

</p>

Nous allons éditer ce calque pour y ajouter nos données récupérées via
Overpass

</p>

![image : édition du calque]({attach}img/201501/export2.png)

</p>

Cliquons sur Données distantes

</p>

Dans le champ url, renseigner la requête Overpass, et sélectionner le
format de données « osm »

</p>

Enfin, cocher la case « Dynamique »

</p>

![image : dynamique]({attach}img/201501/export3.png)

</p>

Vous devriez voir vos données s’afficher sur la carte.

</p>

C’est bien, mais … on peut mieux faire !

</p>

En effet, on aimerait bien pouvoir se déplacer sur la carte pour voir
les boulangeries ailleurs que sur le petit coin que j’ai choisi.

</p>

Il faut donc indiquer à uMap de modifier la requête Overpass en fonction
de l’endroit où se situe l’utilisateur sur la carte.

</p>

Cela se fait très simplement en remplacer toutes les occurrences des
coordonnées dans la requête par les mots-clefs suivants
`{south},{west},{north},{east}` qui sont interprétés par uMap.

</p>

La requête Overpass devient alors :

</p>
```
[http://api.openstreetmap.fr/oapi/interpreter?data=[out:json][timeout:25];](http://api.openstreetmap.fr/oapi/interpreter?data=[out:json][timeout:25];)(node["shop"="bakery"]({south},{west},{north},{east});way["shop"="bakery"]({south},{west},{north},{east});relation["shop"="bakery"]({south},{west},{north},{east}););out
body;\>;out skel qt;
```
</p>

 

Cela se fait très simplement en remplacer toutes les occurrences des
coordonnées dans la requête par les mots-clefs suivants
`{south},{west},{north},{east}` qui sont interprétés par uMap.

</p>

La requête Overpass devient alors :

</p>
```
[http://api.openstreetmap.fr/oapi/interpreter?data=[out:json][timeout:25];](http://api.openstreetmap.fr/oapi/interpreter?data=[out:json][timeout:25];)(node["shop"="bakery"]({south},{west},{north},{east});way["shop"="bakery"]({south},{west},{north},{east});relation["shop"="bakery"]({south},{west},{north},{east}););out
body;\>;out skel qt;
```
</p>

Il ne reste plus qu’à personnaliser la carte selon nos goûts, nos envies
et nos besoins : on peut changer le fond de carte, choisir des marqueurs
plus jolis, etc

</p>

Ne pas oublier également de préciser la licence (ODbL, car utilisation
de données OSM).

</p>

 

</p>

Puis, il ne reste plus qu’à partager sa carte avec le monde entier.

</p>

Pour cela, on peut soit [fournir un
lien](http://umap.openstreetmap.fr/fr/map/boulangeries_26977#16/48.8116/2.3665),
soit l’embarquer directement dans la page comme je l’ai fait ici

</p>


![image : umap]({attach}img/201501/export4.png)

</p>

Et voilà. C’est simple et efficace :)

</p>

Si vous avez des besoins plus sophistiqués, il faudra coder un peu et
partir sur des solutions à bases de modules de Leaflet, telles que
celles que j’ai mises en place pour
[OpenBeerMap](http://openbeermap.github.io/).

</p>
<p>
