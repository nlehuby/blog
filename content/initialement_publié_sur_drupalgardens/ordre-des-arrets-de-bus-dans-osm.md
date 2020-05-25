Title: Ordre des arrêts de bus dans OSM
Date: 2014-05-16 16:35
Author: nlehuby
Tags: #osm
Slug: ordre-des-arrets-de-bus-dans-osm

Oui, encore un article sur les lignes de bus dans OSM ! Promis, après
j'arrête. D'ailleurs, je fais faire très court !

</p>

 

</p>

Toujours dans l'idée d'enrichir et d'améliorer la qualité des données
OSM à l'aide des données opendata disponibles dans
[navitia](http://www.navitia.io/), voici un quick hack, facile et, si
j'ose dire, à la portée de n'importe qui :p

</p>

 

</p>

Prenons, par exemple, la ligne 325 de la RATP : c'est une ligne très
simple, sans fourche ou boucle ou autres joyeusetés.

</p>

Dans OSM, elle est plutôt pas mal cartographiée, on a l'essentiel des
routes et une grande partie des arrêts.

</p>

Mais, en utilisant [sketch-line (l'outil de génération de thermomètre de
ligne à partir des données
OSM)](http://www.overpass-api.de/public_transport.html), le résultat est
... décevant ...

</p>

 

</p>

 

</p>

![image : bus 325 dans le désordre]({attach}img/201405/325-chaos.png)

</p>
</p>

source
: <http://overpass-api.de/api/sketch-line?network=RATP&ref=325&style=paris%C2%A0>

</p>

Déjà, OSM n'arrive même pas clairement à déterminer son origine et sa
destination ... Ensuite, ses parcours ont l'air assez chaotiques.

</p>

C'est un cas typique où les arrêts sont mal ordonnés dans les relations
(car oui, les relations sont ordonnées ! relisez la partie théorique de
mon article sur la carto d'une ligne de bus si vous avez un doute).

</p>

Comment remédier à tout ça et avoir nettoyer la donnée dans OSM ?

</p>

En utilisant navitia.io évidemment :p

</p>

Pas de script cette fois-ci, juste un appel pour récupérer l'ordre des
dessertes :

</p>
![image : bus 325 dans navitia.io]({attach}img/201405/navitia.io-325.png)

</p>
</p>

Puis, il suffit de regarder ce qu'il y a dans OSM et de corriger si
nécessaire dans JOSM (car l'éditeur iD ne permet pas de modifier l'ordre
des éléments dans une relation) :

</p>

![image : bus 325 dans le désordre]({attach}img/201405/josm-325.png)

</p>
</p>

On peut aussi en profiter pour corriger les fautes dans les noms
(Brunesseau ou Bruneseau ? École vétérinaire de Maisons Alfort ou
Maisons Alfort école vétérinaire ? etc)

</p>

C'est un peu long mais pas difficile. 

</p>

Et assez rapidement, on se retrouve avec un thermomètre de ligne tout
beau tout propre, et surtout qui reflète nettement mieux la réalité !

</p>
![image : bus 325 tout bien]({attach}img/201405/325-good.png)


</p>
</p>
