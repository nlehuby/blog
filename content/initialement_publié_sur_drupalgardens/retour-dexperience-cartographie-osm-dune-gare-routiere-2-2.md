Title: Retour d'expérience - cartographie OSM d'une gare routière (2 / 2)
Date: 2014-04-04 16:46
Author: nlehuby
Tags: #osm
Slug: retour-dexperience-cartographie-osm-dune-gare-routiere-2-2


Précédemment, je vous ai traîné derrière moi dans [ma cartographie OSM
de la gare routière de
Boissy-Saint-Léger]({filename}retour-dexperience-cartographie-osm-dune-gare-routiere-1-2.md).

</p>

Pour le moment, nous avons ajouté les arrêts de bus et quelques objets
simples. Le but est maintenant d'indiquer quelles lignes de bus
desservent ces différents arrêts.

</p>

Tout d'abord, un petit rappel théorique (très court, très simple, promis
!) :

**EDIT 2017 : j'ai depuis rédigé [un article détaillé]({filename}../20170528_bien_cartographier_les_bus.md) sur comment bien cartographier des lignes de bus, n'hésitez pas à consulter cet article plutôt**

</p>

Une ligne de bus est composée de différents parcours (notamment le
parcours aller, et le parcours retour, et parfois d’autres).

</p>

On retrouve cette hiérarchie dans OSM.

</p>

 

</p>

La ligne est un objet “relation” dans OSM. Il possède les attributs
suivants :

</p>

-   *type = route\_master*
-   *route = bus*
-   puis des attributs qui la décrivent, comme *from, to, ref,
    operator*, etc

</p>

 

</p>

Les membres de cette relation sont les parcours de la ligne, qui sont
eux même des objets « relations », avec les attributs suivants :

</p>

-   *type = route*
-   *route = bus*
-   et des attributs qui la décrivent

</p>

 

</p>


![image : une relation]({attach}img/carto_gare_22/relation.png)

</p>
</p>

<p>
<address>
exemple avec une ligne que je cartographie plus tard (dans l’article
suivant :p).
</address>
</p>

 

</p>

Cette relation regroupe

</p>

-   les arrêts de bus qui sont desservis
-   les routes (objets de type way) empruntés par le bus

</p>

Et dernière subtilité, que j'ai justement découverte pendant que je
cartographiais les lignes de bus qui passent à Boissy : les relations
sont ordonnées, il faut donc mettre les arrêts de bus dans l'ordre !

</p>

Enfin, en cas de doute, le wiki fait foi :
<https://wiki.openstreetmap.org/wiki/FR:Key:public_transport>

</p>

 

</p>

Donc en bref, on a une relation master, qui contient des relations, qui
elles-mêmes contiennent des arrêts de bus et des routes.

</p>

Passons maintenant à la pratique !

</p>

 

</p>

Je commence par le plus évident avec la ligne de Noctilien : le réseau
RATP est énormément plus avancé en terme de saisie dans OSM que le
“réseau OPTILE”, donc j'imagine que la relation existe déjà.

</p>

Un peu tour sur le wiki et bingo
 : <http://wiki.openstreetmap.org/wiki/WikiProject_France/Noctilien> !

</p>

La relation "master" de la ligne existe, et il y a également une
relation pour le sens Paris-Boissy. Il me faudra créer uniquement le
sens Boissy-Paris.

</p>

Là encore, commençons par le plus simple : ajouter mon arrêt de bus à la
relation existante, c'est-à-dire indiquer que mon arrêt permet
d'emprunter la ligne de Noctilien dans le sens Paris-Boissy.

</p>

J'ouvre l'éditeur iD car je sais qu'on peut ajouter assez facilement une
relation sur un nœud avec. Malheureusement, là, c'est la déconvenue : ma
relation existante ne remonte pas dans la liste des relations
disponibles donc impossible de faire quoique ce soit …

</p>

J'essaye avec JOSM : je re-télécharge ma zone autour de la gare. Je
télécharge ensuite ma relation.

</p>

Puis, je sélectionne l'arrêt à ajouter et je clique sur "modifier la
relation". Là, on me propose d'ajouter l'objet sélectionné (l'arrêt de
bus) à la relation :

</p>
![image : josm]({attach}img/carto_gare_22/josm_0.png)

Au moment d'envoyer ça sur OSM, j'ai plein d'avertissements que je ne
comprends pas :(
</p>
</p>

Je ne pense pas avoir fait d'erreurs, je valide quand même et je vais
regarder dans iD : tout va bien

</p>
![image : id]({attach}img/carto_gare_22/id.png)

</p>
</p>

Bon, ce n'était pas super intuitif, mais j'ai trouvé toute seule, donc
je m'en tire à bon compte...

</p>

 

</p>

J'ai fait le sens aller (l'arrêt est sur la ligne Noctilien N32, dans le
sens  Paris – Boissy), il reste donc le sens retour. Il va donc falloir
que je crée la relation du sens retour, car elle n'existe pas encore !

</p>

 

</p>

Créer une relation est étonnamment facile dans iD, c'est fait en
l'espace de quelques secondes.

</p>

En revanche, pas moyen de trouver comment assigner une relation parente
(pour dire que ma nouvelle relation N32 Boissy - Paris appartient à la
relation "master" ligne N32).

</p>

Retour dans JOSM donc !

</p>

Je mets à jour les données OSM (pour ne pas avoir de conflit au moment
où je vais pousser mes modifications), je sélectionne ma relation fille
et je clique sur modifier ma relation parente, j'ajoute et j'envoie à
OSM.

</p>

Petit tour dans ID sur ma relation parente pour vérifier :

</p>
![image : id]({attach}img/carto_gare_22/encore_id.png)


J'en profite pour faire un tour sur le wiki et indiquer que j'ai créé la
relation sens retour.
</p>
</p>

 

</p>

J'ai galéré plus que je ne l'imaginais, mais maintenant que j'ai la
méthode, l'affaire est dans le sac, il ne reste plus qu'à dupliquer !

</p>

 

</p>

Un peu de méthode, tant que je suis sur le wiki, je vais commencer par
là.

</p>

Je créée donc la page de wiki du réseau SETRA :
<https://wiki.openstreetmap.org/wiki/WikiProject_France/Bus_SETRA>

</p>

Je duplique le contenu depuis une autre page décrivant un réseau de bus
de banlieue et je modifie uniquement ce qui m'intéresse, à savoir :

</p>

-   le paragraphe descriptif sur les attributs : il faut indiquer le bon
    réseau (*network*) et le bon transporteur*(operator*)
-   le gros tableau qui contient les relations des différentes lignes.

</p>

 

</p>

Je n'ai que trois lignes, c'est donc assez rapide.

</p>

J'avoue que je suis bluffée par ce que je vois dans le tableau décrivant
les lignes (et je ne suis pas mécontente d'avoir déjà quelques bases sur
la syntaxe MediaWiki, car sinon, comprendre et éditer le tableau
pourrait représenter une difficulté supplémentaire ...)

</p>

![image : wiki]({attach}img/carto_gare_22/wiki.png)

</p>
</p>

Il y a des outils de saisie assez malins :

</p>

Si j'écris *{{Relation|3315207|Brie-comte-Robert Piscine → Créteil
Préfécture|tools=no}}*, cela va afficher un lien vers la relation
correspondante.

</p>

Le modèle *BrowseLine* permet d'afficher en plus quelques liens vers des
outils de contrôles des relations. Je vous en présenterai quelques-uns
plus en détail dans l’[article
suivant.]({filename}retour-dexperience-cartographie-osm-de-quelques-lignes-de-bus.md)

</p>

Bref, le wiki est donc particulièrement adapté pour consigner mon
avancement.

</p>

 

</p>

Une fois ma page initialisée, je peux créer mes relations.

</p>

Je lance iD, je sélectionne un arrêt, je l'ajoute à une nouvelle
relation. Je crée ma nouvelle relation bus X, sens 1. En revanche, je
n'ai pas trouvé comment ordonner les membres d'une relation dans iD,
donc un passage par JOSM s'impose derrière ...

</p>

J'envoie sur OSM et je rajoute l'identifiant de cette nouvelle relation
dans le wiki :

</p>
![image : wiki]({attach}img/carto_gare_22/encore_wiki.png)

</p>
</p>

Magnifique !

</p>

 

</p>

Bon, je laisse tomber iD et  je passe sur JOSM pour aller un peu plus
vite dans la création de mes différentes relations (route master, puis
sens 1 et sens 2).

</p>

 

</p>

Ultime étape :

</p>

Ajouter la voie de bus de la gare routière à mes différentes relations
(pour indiquer les bus de toutes ces lignes empruntent cette voie).

</p>

C’est assez simple, il suffit de sélectionner ma route et de l’ajouter à
ma relation, exactement comme pour les arrêts de bus.

</p>

 

</p>

Et voilà, OSM sait tout sur la gare routière de Boissy :)

</p>

 

</p>

Mais il serait frustrant de s'arrêter là, j'ai maintenant tout ce qu'il
faut pour cartographier entièrement ces lignes de bus que je viens de
créer : ce sera l'objet de [l'article suivant
!]({filename}retour-dexperience-cartographie-osm-de-quelques-lignes-de-bus.md)
