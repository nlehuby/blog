Title: Bien cartographier les bus dans OSM
Date: 2023-02-24 08:34
Author: nlehuby
Tags: #osm, #junglebus
Slug: bien-cartographier-les-bus

Il est fréquent d'être un peu perdu(e) lorsqu'on souhaite cartographier les lignes de bus dans OSM. Cet article propose quelques rappels théoriques pour bien se lancer !

Pour commencer, on a l'arrêt de bus.<br>
![image d'arrêt de bus]({attach}images/20170528_bien_cartographier_les_bus/bus_stop.png)

Pour cartographier cet arrêt de bus, on crée un nœud, avec le tag *public_transport = platform*. Ce tag désigne l'endroit où le voyageur attend le bus donc il faut le positionner au niveau du trottoir, là où se situe l'abribus ou le poteau d'arrêt.<br>
Pour bien préciser le mode de transport (car ce tag s'utilise aussi pour les arrêts de tram ou de train), on ajoute également *highway = bus_stop*.

On peut ensuite ajouter les informations contextuelles propres à cet arrêt, comme son nom (*name = ...*), s'il y a un abri (*shelter = yes/no*), un banc (*bench = yes/no*), une bande podotactile pour aider les malvoyants à se repérer, etc<br>

En complément du lieu où les voyageurs attendent, il est possible d'indiquer l'emplacement sur la route où le véhicule s'arrête. Cette information est particulièrement importante dans la cartographie des trains ou des tramways, mais est largement moins utile pour les bus, donc je recommande de l'ignorer complètement car elle ajoute beaucoup de complexité notamment pour la maintenance. Mais puisqu'elle existe dans OSM, décrivons-là tout de même par acquis de conscience.<br>
Pour représenter l'endroit sur la chaussée où le bus s'arrête, on peut donc créer un deuxième nœud. À noter que le nœud doit faire partie du chemin décrivant la route et non pas être posé dessus.<br>
Sur ce nœud, on ajoute les tags *public_transport = stop_position* et *bus=yes*. Il est courant d'y indiquer à nouveau le nom de l'arrêt, mais on évitera d'y ajouter les informations sur l'équipement (abribus, banc, etc) afin de ne pas créer trop de redondance.

![image d'arrêt de bus avec les tags qui vont bien]({attach}images/20170528_bien_cartographier_les_bus/bus_stop_annote.png)

Une fois qu'on a bien cartographié notre arrêt, il nous faut indiquer quels bus s'y arrêtent.<br>
Les lignes de bus sont représentées dans OSM par des relations, c'est-à-dire des objets qui sont des regroupements d'autres objets.

Une ligne de bus dans OSM sera une relation de *type = route_master*.<br>
On lui ajoutera les autres tags suivants :

* *route_master = bus* pour indiquer son mode de transport
* *ref = un nombre*, pour indiquer le numéro de la ligne
* *operator = ...*, pour renseigner l'entreprise qui fait rouler ces bus
* *network = ...*, pour indiquer le nom du réseau
* *name = ...*, pour indiquer le nom de la ligne

Dans cette relation ligne de bus, on mettra les objets OSM qui représentent les variantes de trajets de la ligne, ses parcours.<br>
En général, on aura au moins le parcours de la ligne en sens aller et le parcours de la ligne en sens retour. On trouvera aussi parfois le parcours spécial du matin qui s'arrête devant l'école, ou le parcours spécial du jeudi qui passe dans une autre rue à cause du marché.

Les trajets sont aussi des relations, de *type = route*.<br>
On leur ajoute les tags suivants :

* *route = bus* pour indiquer le mode de transport
* *ref = un nombre*, pour rappeler le numéro de la ligne
* *operator = ...*, pour rappeler l'entreprise qui fait rouler ces bus
* *network = ...*, pour rappeler le nom du réseau
* *name = ...*, pour indiquer le nom du parcours
* *from = ...*, pour indiquer le point de départ du parcours
* *to = ...*, pour indiquer la destination du parcours
* *public_transport:version = 2*. Ce tag technique sert à indiquer qu'on utilise le "nouveau" modèle de cartographie des transports en commun, qui a été approuvé par un vote de la communauté en 2010, et non le modèle historique, où les rôles dans la relation peuvent avoir un sens un peu différent.

Et dans cette relation trajet, on ajoute :

* tous les arrêts, dans l'ordre où ils sont desservis
* les routes empruntées par le bus, dans l'ordre, afin de reconstituer son itinéraire

Les arrêts *platform*, situés sur le trottoir, s'ajoutent dans la relation trajet avec le rôle *platform*.<br>
Si vous avez créé également les arrêts *stop_position*, situés sur la route, vous pouvez les ajouter dans la relation trajet avec le rôle *stop*.

Ceci est bien sûr à faire pour toutes les lignes (ou plus précisément trajets de lignes) qui s'arrêtent à cet arrêt. Afin de trouver ces lignes dans OSM (et déterminer si elles existent déjà ou s'il faut les créer), il peut être utile de faire une petite recherche, par exemple avec [Unroll](https://jungle-bus.github.io/unroll/).

À ce stade, on a donc des nœuds (*platform*, et éventuellement *stop_position*), qu'on met dans les relations (*type = route*), qu'on met elles-mêmes dans des relations (*type = route_master*)<br>
![schéma avec route et route_master]({attach}images/20170528_bien_cartographier_les_bus/bus_dans_relation.png)

On peut également retrouver un autre type de relation, qui sert à modéliser les correspondances au niveau des arrêts.<br>
Elle a alors les tags *type = public_transport* et *public_transport = stop_area*, et contient également comme membres les arrêts *platform* avec le rôle *platform*, et éventuellement les arrêts *stop_position* avec le rôle *stop*.<br>
Ces relations sont surtout pertinentes pour modéliser les stations de métro ou les gares, afin que les utilisateurs de la donnée (tels que les calculateurs d'itinéraire) puissent savoir qu'une bouche de métro permet de rejoindre tel quai, ou que tel quai est bien en correspondance avec tel autre quai.<br>
Elles sont cependant moins utiles pour les bus car les correspondances peuvent se déterminer par simple proximité géographique, donc je conseille de ne pas les créer. Mais on en retrouvera parfois dans les grandes gares routières ou lorsqu'un arrêt de bus est en correspondance avec une gare.

![schéma avec tout les relations possibles. Vous reprendrez bien une petite relation avec votre relation de relations ?]({attach}images/20170528_bien_cartographier_les_bus/bus_dans_plein_relations.png)

En résumé, créez votre arrêt à côté de la route, ajoutez-le dans tous les trajets de bus qui passent là (*type = route* et *route = bus*), en vérifiant que ces trajets sont eux-mêmes dans une ligne de bus (*type = route_master* et *route_master = bus*), et vous avez fini ! Il ne vous reste plus qu'à faire la même chose avec l'arrêt de bus qui est de l'autre côté de la rue ;)

Félicitations, vous connaissez à présent les bases : vous pouvez comprendre les données déjà renseignées dans OSM et vous lancer sereinement dans la cartographie des bus autour de chez vous !

Vous rencontrerez encore quelques nouveautés au gré de votre cartographie : il vous faudra parfois couper les chemins pour bien représenter les tracés des lignes, vous devrez apprendre des nouveaux tags pour représenter les lignes spéciales comme les bus à la demande ou les bus scolaires, etc<br>
Autant de sujets pour des nouveaux articles de blog qui restent à écrire ! En attendant, pour aller plus loin, je vous invite à vous plonger dans [le wiki](https://wiki.openstreetmap.org/wiki/FR:Bus) et à venir poser vos questions sur la [liste de diffusion transport](https://listes.openstreetmap.fr/wws/info/transport) ou sur [le forum](https://forum.openstreetmap.fr/tag/transport-en-commun) !

Remarque : cet article est une petite réécriture d'un article de 2017 souvent repartagé. L'article initial mettait plus en avant les différences entre le modèle actuel (qu'on appelle "ptv2" dans le jargon) et le modèle historique ; ces distinctions n'ont plus grand sens aujourd'hui. Pour les nostalgiques, [l'article initial]({filename}20170528_bien_cartographier_les_bus_initial.md) reste bien sûr disponible. 
