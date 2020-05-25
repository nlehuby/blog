Title: Bien cartographier les bus
Date: 2017-05-28 15:24
Author: nlehuby
Tags: #osm, #junglebus
Slug: bien-cartographier-les-bus

Aujourd'hui, je vous propose quelques rappels théoriques sur comment bien cartographier les bus dans OSM.

NB : Je prends pour référence [le modèle dit "Public Transport v2"](https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport), approuvé par la communauté OSM en 2010. À noter qu'il n'y a pas eu de mise à niveau globale vers ce modèle et donc que le modèle historique, plus simple mais moins précis, continue d'exister et est souvent le seul reconnu par les outils utilisant les données OSM.

Pour commencer, on a l'arrêt de bus.<br>
![image d'arrêt de bus]({attach}images/20170528_bien_cartographier_les_bus/bus_stop.png)

Dans le modèle historique, pour cartographier cet arrêt de bus, on se contentait de mettre un tag *highway = bus_stop*, en général au niveau du trottoir.<br>
Mais ça, c'était avant ! Maintenant, on crée deux objets dans OSM :<br>
Tout d'abord, pour désigner l'endroit où le voyageur attend le bus (ici, l'abribus), on crée un noeud, avec les tags *public_transport = platform*.<br>
Pour bien préciser le mode (car ce tag s'applique aussi pour les arrêts de tram ou de train), et pour la rétro-compatibilité avec l'ancien modèle (notamment sur les outils de rendu), on ajoute également *highway = bus_stop*.

Puis, on crée un deuxième noeud, qui représente l'endroit sur la chaussée où le bus s'arrête. À noter que le noeud doit faire partie du chemin décrivant la route et non pas être posé dessus.<br>
Sur ce noeud, on ajoute les tags *public_transport = stop_position* et *bus=yes*

Une fois qu'on a fait ça, on peut ajouter les infos contextuelles propres à cet arrêt, comme son nom (*name = ...*), s'il y a un abri (*shelter =yes/no*), un banc (*bench = yes/no*), une bande podotactile, etc<br>
En général, on ajoutera tout ça uniquement sur l'objet *platform* (mais il est courant de répéter le nom aussi sur le *stop_position*).

![image d'arrêt de bus avec les tags qui vont bien]({attach}images/20170528_bien_cartographier_les_bus/bus_stop_annote.png)

Une fois qu'on a bien cartographié notre arrêt, il nous faut indiquer quels bus s'y arrêtent.<br>
Les lignes de bus sont représentées dans OSM par des relations, c'est-à-dire des objets qui sont des regroupements d'autres objets.

Une ligne de bus dans OSM sera une relation de *type = route_master*.<br>
On lui ajoutera les autres tags suivants :

* *route_master = bus* pour indiquer son mode
* *ref = un nombre*, pour indiquer le numéro de la ligne
* *operator = ...*, pour renseigner l'entreprise qui fait rouler ces bus
* *network = ...*, pour indiquer le nom du réseau
* *name = ...*, pour indiquer le nom de la ligne

Dans cette relation ligne de bus, on mettra les objets OSM qui représentent les variantes de tracés de la ligne, ses parcours.<br>
En général, on aura au moins le parcours de la ligne en sens aller et le parcours de la ligne en sens retour. On trouvera aussi parfois le parcours spécial du matin qui s'arrête devant l'école, ou le parcours spécial du jeudi qui passe dans une autre rue à cause du marché.

Les parcours (variantes de lignes) sont aussi des relations, de *type = route*.<br>
On leur ajoute les tags suivants :

* *route = bus* pour indiquer le mode
* *ref = un nombre*, pour rappeler le numéro de la ligne
* *operator = ...*, pour rappeler l'entreprise qui fait rouler ces bus
* *network = ...*, pour rappeler le nom du réseau
* *name = ...*, pour indiquer le nom du parcours
* *from = ...*, pour indiquer le point de départ du parcours
* *to = ...*, pour indiquer la destination du parcours
* *public_transport:version = 2*, pour indiquer qu'on utilise le "nouveau" modèle et non le modèle historique

Et dans cette relation parcours, on ajoute :

* tous les chemins que prend le bus
* nos fameux arrêts, *platform* et *stop_position*, dans l'ordre où ils sont desservis.
![gif animé josm, avec tracé, stop position et platform]({attach}images/20170528_bien_cartographier_les_bus/josm_ptv2.gif)

En particulier, on ajoutera les *platform* avec le rôle ... *platform*, et les *stop_position* avec le rôle ... *stop* (ben oui, vous pensiez quand même pas que ça serait si simple !).<br>
Et on le fera bien sûr pour toutes les lignes (ou plus précisément variantes de lignes) qui s'arrêtent à cet arrêt.

Si vous avez bien suivi, on a donc des noeuds (*platform* et *stop_position*), qu'on met dans les relations (*type = route*), qu'on met elles-mêmes dans des relations (*type = route_master*)<br>
![route et route_master]({attach}images/20170528_bien_cartographier_les_bus/bus_dans_relation.png)

À noter que dans le modèle historique, les relations parcours (*type = route*) contenaient uniquement les arrêts (*highway = bus_stop*) avec le rôle *stop*. Avec le nouveau modèle, les objets qui ont le tag *highway=bus_stop* ont en général plutôt le rôle *platform*.<br>
Pour bien savoir ce que représente un objet qui a le rôle stop, on ajoute *public_transport:version = 1* sur les relations parcours (*type = route*) qui ont été cartographiées suivant le modèle historique et n'ont pas encore été mises à niveau.

Vous suivez toujours ? Parce que ce n'est pas fini !

Pour rassembler tous les arrêts en correspondance, on utilisera encore une autre relation, avec les tags *type = public_transport* et *public_transport = stop_area*.<br>
De la même manière, les *platform* auront le rôle *platform*, et les *stop_position* le rôle *stop*.<br>
Ces relations sont encore très peu répandues dans OSM ; pour les bus on les retrouve surtout dans les grandes gares routières.

![ouais, c'est pas facile]({attach}images/20170528_bien_cartographier_les_bus/bus_dans_plein_relations.png)

Une fois que vous avez ajouté vos *platform* et *stop_position* dans tous les parcours (*type = route* et *route = bus*) et dans sa zone d'arrêt (*type = public_transport* et *public_transport = stop_area*), vous avez fini !<br>
Félicitations, vous pouvez maintenant vous attaquer à l'arrêt de bus qui est de l'autre côté de la rue ;)

Le mot de la fin :<br>
Vous trouvez que tout ceci est bien compliqué pour pas grand chose, et qu'on devrait pouvoir faire ça de manière transparente dans une appli, directement quand on est sur le terrain ?<br>
Vous avez raison : soutenez le projet [Jungle Bus](http://junglebus.io) pour rendre tout ceci possible !

Vous pestez parce que je n'ai pas parlé des rôles *exit_only* et *entry_only*, ni du fait qu'il fallait parfois couper les chemins ? Rejoignez le projet [Jungle Bus](http://junglebus.io), les bussophiles sont y sont accueillis à bras ouverts ;)
