Title: Script d’intégration des arrêts de bus dans OSM à partir de navitia.io
Date: 2014-04-29 16:54
Author: nlehuby
Tags: #osm, #hack, #opendata
Slug: script-dintegration-des-arrets-de-bus-dans-osm-a-partir-de-navitiaio


Vous l'aurez compris, mon TOC (trouble obsessionnel cartographique) du
moment, c'est les arrêts de bus !

Et en travaillant sur le projet [KartoKartier](http://kartokartier.com),
avec mes collègues, dans le cadre du concours
[Cartoviz](http://cartoviz.lafonderie-idf.fr), je me suis rendue compte
qu'il y avait une belle marge de manoeuvre pour améliorer la qualité des
données OSM pour les arrêts de bus : [j'en parlais
ici](http://www.kisiodigital.com/Blog/Entry/id/89).

</p>

C'est ainsi que je me suis mise en tête de faire un script qui se
nourrit de l'opendata RATP  via l'API [navitia.io](http://navitia.io),
pour enrichir les données OSM en ajoutant, pour commencer, les noms des
arrêts manquants.

</p>

Ce script est disponible sur
[github](https://github.com/nlehuby/OSM_snippets/tree/master/navitia-to-OSM%20(bus%20stop%20names)),
et librement réutilisable.

</p>

 

</p>

<u>Que fait ce script ?</u>

</p>

Tout d’abord, il récupère la liste de tous les arrêts de bus, situé dans
la ville de Paris (par exemple), qui n’ont pas de nom renseigné.

</p>

J'ai commencé par l'utiliser sur des villes plus proches de la mienne,
voici quelques métriques :

</p>

-   nombre d’arrêts sans nom à Paris : 267
-   nombre d’arrêts sans nom à Boissy-Saint-Léger : 21
-   nombre d’arrêts sans nom à Sucy-en-Brie : 38
-   nombre d’arrêts sans nom à Créteil : 25
-   nombre d’arrêts sans nom à Bonneuil-sur-Marne : 3

</p>

Ensuite, pour chacun de ces arrêts, j’appelle navitia.io (une API pour
les transports en commun, développée par [Kisio Digital](http://canaltp.fr) (anciennement Canal TP),
et qui s'alimente, entre autres, des données opendata RATP) et je lui
demande de me retourner les points d’arrêts à proximité des coordonnées
du point OSM.

</p>

Les données opendata de la RATP, qui sont utilisées dans navitia.io ont
une géolocalisation peu précise, donc en faisant varier la distance
d’accroche, on obtient des résultats plus ou moins pertinents :

</p>

Métriques sur Paris :

</p>

-   Nombre d’arrêts OSM ayant un arrêt RATP à moins de 100 mètres : 249
-   Nombre d’arrêts OSM ayant un arrêt RATP à moins de 50 mètres : 221
-   Nombre d’arrêts OSM ayant un arrêt RATP à moins de 20 mètres : 145
-   Nombre d’arrêts OSM ayant un arrêt RATP à moins de 10 mètres : 74

</p>

 

</p>

Sur ces arrêts, j’ai choisi, dans un premier temps, de ne conserver que
ceux qui ont un unique arrêt RATP (ou plusieurs arrêts avec le même nom)
: ce sont les plus faciles à intégrer.

</p>

Pour ceux-là, je crée un fichier JOSM avec le nom pré-rempli.

</p>

Il n’y a plus alors qu’à ouvrir le fichier dans JOSM, à charger les
données existantes autour du point, à vérifier que les infos sont
cohérentes, puis à envoyer la modification dans OSM.

</p>
![image : retour]({attach}img/201405/poteau-arret.png)

</p>
</p>

<p>
<address>
exemple de retour du script
</address>
</p>
![image : retour du script sur Boissy]({attach}img/201405/poteau-arret-boissy.png)



</p>
</p>



Ci-dessus, le retour du script sur Boissy-St-Léger : il n'y a un seul
arrêt RATP (l'arrêt noctilien que j'ai cartographié [dans un article précédent]({filename}retour-dexperience-cartographie-osm-de-quelques-lignes-de-bus.md)), et il a déjà un
nom !





<u>Dans la pratique, l’intégration :</u>

</p>

J’ai choisi d’y aller itérativement, et de commencer par les moins
ambigus, donc ceux ayant un arrêt RATP très proche. J'ai aussi choisi de
commencer par ceux proches de chez moi, pour pouvoir faire une
vérification sur le terrain en cas de doute.

</p>

Les premiers arrêts que j'ai intégrés étaient parfaits : c'est le cas
typique

</p>

-   où navitia a trouvé une correspondance entre mon arrêt sans nom et
    les données opendata
-   où il n'y a que deux arrêts de bus dans tout le quartier, placé
    chacun d'un côté de la route (le sens aller et le sens retour)
-   le second arrêt a déjà un nom, et c'est le même que celui trouvé par
    navitia
-   éventuellement, mon arrêt a un tag name:RATP rempli, et concordant
    (mais il a peut-être été aussi généré par un script, je ne sais pas
    si c'est vraiment une mesure de fiabilité)

</p>

Là, on peut intégrer les yeux fermés :)

</p>

Malheureusement, c'est loin de représenter la majorité des cas ...

</p>

À vrai dire, j'ai même trouvé une bonne poignée d'exemples carrément
invalides (c'est le cas de le dire) : par exemple, cet arrêt

</p>
![image : cet arrêt]({attach}img/media_crop/6/public/201404/1.png)

</p>
</p>

Il est situé à 16 mètres d’un arrêt de bus que l’opendata RATP appelle
Invalides.

</p>

Mais, dans les données déjà présentes sur OSM, il est indiqué que c’est
un arrêt desservi par les cars Air France.

</p>

En conséquence, navitia, alimenté par des données opendata RATP et SNCF
(et pas Air France) n’est pas une source fiable pour me fournir le nom
de l’arret.

</p>

Ça ne veut pas dire que l'arrêt ne s'appelle pas Invalides, mais à moins
d'aller voir sur place, je ne peux pas en être certaine ...

</p>

On l'oublie souvent, mais il n'y a pas que la RATP comme opérateur de
transport, même à Paris !

</p>

J’ai même découvert des opérateurs de transport que je ne connaissais
pas :

</p>
![image : opérateur]({attach}img/media_crop/11/public/201404/2.png)

</p>
</p>

 

</p>

Enfin, il ya aussi des exceptions géographiques étranges : je pense par
exemple aux arrêts de bus autour de Porte Dorée : on trouve deux arrêts,
chacun d'un côté de la route, et il y en a un des deux qui ne s'appelle
pas Porte Dorée !

</p>

 ![image : cet arrêt]({attach}img/media_crop/21/public/201404/portedoree.png)

</p>
</p>

 

</p>

Bref, on aurait pu croire qu’on pouvait tout importer automatiquement,
mais en creusant un peu, on se rend compte que souvent, il y a des
petites subtilités et qu’une vérification humaine est effectivement
nécessaire. On comprend ainsi beaucoup mieux les réticences de la
communauté OSM face aux imports massif de données d’autres sources
(c'est d'ailleurs pour ça qu'on parle ici d'intégration, et non
d'import).

</p>

 

</p>

<u>État des lieux :</u>

</p>

En bref ... aujourd'hui, j'ai intégré tous les arrêts RATP des villes
proches de chez moi (Boissy, Sucy, Bonneil, Créteil). Mais
malheureusement, ils ne représentent pas la majorité des arrêts de bus
de ces villes, qui sont massivement desservies par d'autres compagnies,
dont les données de transport ne sont pas en opendata, et donc pas dans
navitia.io !

</p>

Sur Paris, il m'en reste aujourd'hui moins de 100 !

</p>

 

</p>

<u>Et après ?</u>

</p>

Les possibilités sont multiples : par exemple, l'intégration dans Osmose
pourrait permettre à d'autres contributeurs de vérifier avant d'envoyer
les modifications dans OSM (comme ce qui est fait pour les données
opendata des écoles par exemple).

</p>

Il serait intéressant également de regarder les rejets de mon script,
comme les arrêts OSM ayant plusieurs arrêts opendata (avec un nom
différent) à proximité : sur ceux-là, une vérification sur le terrain
s'impose pour choisir entre les possibilités.

</p>

Ensuite, pourquoi pas réfléchir à l'intégration des lignes de bus RATP à
partir de navitia.io !

</p>

 

</p>

De plus, OSM est un projet international, et navitia aussi, donc le
modèle pourrait s'exporter sans soucis ...

</p>

Mais j'attends surtout l’opendata des données transports sur toute
l’Île-de-France, pour compléter les villes près de chez moi !

**EDIT 2015 : c'est fait, [les données de toute l'Île-de-France sont librement accessibles]({filename}les-donnees-horaires-du-stif-en-opendata.md)**

**EDIT 2017 : mise à jour de quelques liens cassés**

