Title: Cartographier une gare routière
Date: 2025-08-23 18:18
Author: nlehuby
Tags: #osm, #junglebus
Slug: bien-cartographier-une-gare-routiere



Mettre à jour une gare routière dans OpenStreetMap n'est pas une opération triviale, surtout s'il y a déjà des informations qui ont été précédemment saisies par d'autres contributeurs et qu'elles ne sont plus à jour. Je vous propose aujourd'hui un peu de méthodologie pour mener à bien cette tâche.

**Étape 1 : la collecte de données sur le terrain**

Même pour une gare routière qu'on connaît bien, je préconise de commencer par aller sur le terrain faire des relevés. Les informations qui nous intéressent prioritairement sont :

- les positions des arrêts de bus (combien y en a-t-il, où sont-ils situés, ont-ils un numéro de quai, etc)
- les lignes qui desservent chacun des arrêts de bus
- éventuellement où passent les bus (où sont les voies de bus, sont-elles à sens unique, etc)
- éventuellement les équipements (abribus, poubelles, bancs, toilettes, etc)

Pour cette étape, le plus simple est d'enregistrer une trace GPS en parcourant la gare routière, en prenant des notes sur les arrêts. Je recommande de noter a minima le numéro de quai s'il existe, ainsi que les numéros de lignes desservies. En complément, prendre des photos des en-têtes des grilles horaires affichées ou d'autre information pertinente qui permet d'identifier la direction.

![exemple de trace GPS dans la gare routière de Vernouillet Verneuil. On y voit le chemin suivi, et les emplacements des arrêts, avec le numéro des quais]({attach}images/20250823_bus_station/step1_gps.png)

Si on dispose d'une caméra 360, il peut également être utile de faire un tour de la gare routière en prenant des photos. Cela peut d'ailleurs être suffisant si la signalétique est large et écrite très gros, ce qui est tout de même assez rare. Mais cela reste pertinent quoi qu'il arrive pour avoir une vue d'ensemble de la gare routière, se remémorer les lieux, voir la position des arrêts les uns par rapport aux autres, visualiser les voies de bus et les cheminements piétons dans la gare, ou encore les équipements auxquels on n'a pas forcément prêté attention lorsqu'on collectait les informations des arrêts, etc

[![exemple de photo Panoramax dans la gare routière de Marne-la-Vallée Chessy Nord. On y voit un arrêt, avec son numéro de quai et la ligne qui s'y arrête]({attach}images/20250823_bus_station/step1_panoramax.png)](https://panoramax.openstreetmap.fr/?background=streets&focus=pic&map=19.5/48.8708842/2.783975&pic=4b3c072d-8669-4230-8d62-cdef96b6acc5&speed=200&xyz=343.21/-0.06/45)

**Étape 2 : la reconstitution de la gare routière**

Il s'agit alors de retraiter les données collectées sur le terrain aux formats variés (points GPS, photos, etc) et de transformer ça en un premier plan de gare routière qui nous servira pour cartographier.

Je recommande d'effectuer cette étape sur papier car on aura envie de griffonner dessus plus tard.

On commence par dessiner grossièrement l'agencement de la gare, en positionnant les arrêts les uns par rapport aux autres sur papier. S'ils ont un numéro de quai, on peut l'utiliser, sinon, on peut leur attribuer une lettre ou un numéro pour les identifier plus facilement. Pas besoin que ça soit à l'échelle ou joli, il s'agit surtout de construire une représentation visuelle de la gare.

![plan très schématique des 9 arrêts de la gare routière de Cergy St-Christophe]({attach}images/20250823_bus_station/step2_plan.png)

Ensuite, on crée l'index des lignes : on reporte le numéro de l'arrêt, puis on indique la ligne et sa destination, une ligne (sur le papier) pour chaque ligne (de bus) en s'aidant des informations de la trace GPS et des photos.

![index des lignes desservant les 9 arrêts de la gare routière de Cergy St-Christophe]({attach}images/20250823_bus_station/step2_index.png)

Il n'est pas rare à ce stade de trouver des incohérences qui étaient passées inaperçues lors de la collecte terrain, comme une ligne qui serait indiquée sur le côté de l'abribus mais n'aurait pas de fiche horaire, ou une ligne qui serait indiquée sur plusieurs abribus alors qu'il est peu probable que le même bus s'arrête plusieurs fois dans la gare, mais on fait au mieux.

À la fin de cette étape, on a normalement un beau schéma papier. Il est temps de passer aux choses sérieuses et de regarder ce qu'OSM en dit.

**Étape 3 : modifier la gare et les arrêts**

On charge donc la zone dans JOSM.

En fonction de l'activité des contributeurs du coin sur cette thématique, ce que vous verrez peut varier du simple au tout, il peut y avoir uniquement un arrêt de bus représentant la totalité de la gare routière, ou bien il peut y avoir déjà des voies de bus, des arrêts de bus et des lignes qui les desservent.

Commençons par l'objet le plus simple : la gare routière en elle-même.

On la représente avec un polygone (chemin fermé) et les tags *amenity=bus_station* + *public_transport=station*.

Si l'objet n'existe pas, on peut donc le créer. S'il existe déjà, on vérifie qu'il englobe bien tous les arrêts de la gare routière.
On peut lui ajouter un nom (*name = Gare routière de Trifouillis*), et éventuellement d'autres infos comme la présence de toilettes (*toilets=yes*) ou de wifi (*internet_acces=wlan*).

Ensuite, on va s'attaquer aux arrêts dans la gare routière. En s'aidant de notre schéma, de l'imagerie aérienne, des photos 360 et de la trace GPS, on peut positionner les arrêts de bus au sein de la gare, en reprenant les éventuels arrêts déjà existants et en créant ceux qui seraient manquants.

On les représente avec un point (nœud) et les tags *highway=bus_stop* + *public_transport=platform*. S'il y a un numéro de quai, on l'ajoute également avec le tag *local_ref*. Enfin, si on a relevé les équipements des arrêts (abribus, banc, poubelle, écran d'affichage temps réel des prochains départs etc), c'est également le bon moment pour les ajouter.

Enfin, on peut passer en revue les tags *name* de ces arrêts et s'assurer qu'ils ont tous le même. À noter qu'il n'est pas nécessaire d'ajouter le nom du quai dans le nom de l'arrêt, puisqu'on l'ajoute déjà dans le tag *local_ref*.

Il arrive parfois qu'on rencontre des abribus qui semblent ne pas être utilisés. Je recommande de les cartographier comme des arrêts classiques, et de leur ajouter un tag *description=arrêt non utilisé*. Cela clarifie la situation pour quelqu'un qui verrait l'arrêt sur l'imagerie et se demanderait pourquoi il n'est pas dans OSM, et ça permet de l'avoir déjà tout prêt si la situation évolue dans la gare routière à l'avenir.

On peut déjà envoyer cela dans OSM dans un premier changeset.

**Étape 4 : collecter les lignes existantes dans OSM**

On souhaite à présent indiquer sur chaque arrêt les lignes desservies. Cela se fait dans OSM en ajoutant l'arrêt de bus dans une relation avec *type=route* + *route=bus*. Ces relations *route* représentent les trajets des lignes de bus. On ajoute par ailleurs ces relations dans une relation *type=route_master* + *route_master=bus* qui représente la ligne elle-même, avec ses différents trajets. En cas de doute, n'hésitez pas à relire cet autre [article de blog qui détaille le modèle de données pour les lignes de bus](https://nlehuby.5apps.com/bien-cartographier-les-bus.html).

La suite de notre contribution ne porte donc plus sur les arrêts de bus, mais sur les relations des trajets de ligne de bus, qu'on doit modifier pour insérer les arrêts de notre gare routière.

Il est possible que certains arrêts préexistants dans OSM portent déjà des lignes de bus. De même, si des voies de bus étaient déjà tracées dans OSM, il est également possible qu'elles portent des lignes de bus. On a donc déjà potentiellement plusieurs trajets et lignes déjà chargés dans JOSM. On peut les voir dans l'encart "Relations" de JOSM (on peut filtrer en écrivant "bus" si la liste est vraiment trop longue à naviguer). Notre objectif pour boucler cette étape est d'avoir dans JOSM la liste complète de tous les trajets de notre gare routière.

Le jeu à présent est d'identifier ces lignes en les comparant à notre schéma.

Là encore, ce jeu sera plus ou moins délicat en fonction de la qualité des précédentes contributions sur ce domaine : si les relations sont bien en ordre, elles ont des tags qui permettent de comprendre sans équivoque de quelle ligne il s'agit et cette étape est assez simple et rapide.

Si ce n'est pas le cas, il sera nécessaire de passer un peu de temps au préalable pour renseigner les tags descriptifs des relations existantes. Les tags *name*, *ref*, *operator*, *network*, *from*, *to* sont un minimum sur les relations *route* et *route_master*. Prenez le temps de télécharger tous les membres de ces relations, de comprendre où elles vont, voire de rechercher un peu d'information voyageur sur le net pour renseigner les informations manquantes. Vous pouvez activer les validateurs Jungle Bus dans JOSM pour vous faciliter un peu la tâche.

![animation montrant comment ajouter les validateurs Jungle Bus dans JOSM](https://github.com/Jungle-Bus/transport_mapcss/raw/master/add_validator.gif)

Quand vous arrivez à savoir à quel trajet ou ligne correspond chaque relation, vous pouvez donc identifier les trajets qui nous intéressent, c'est-à-dire ceux de notre schéma papier. Marquez-les avec une petite coche par exemple. On va alors pouvoir se concentrer sur ceux qui sont sur notre schéma papier mais pas dans JOSM.

Là, nous avons deux possibilités :

- soit ces trajets existent déjà dans OSM, mais ne sont pas assez bien mappées et ne passent pas encore par là
- soit ces trajets sont manquants et il faut les créer dans OSM

Pour retrouver ces lignes dans OSM, vous pouvez rechercher sur le wiki si la page du réseau existe, ou effectuer une recherche avec [Unroll](https://jungle-bus.github.io/unroll/), avec le nom du réseau ou de l'opérateur ou le numéro de ligne ou juste rechercher toutes les lignes d'une ville.

![Capture d'écran du site Unroll avec la recherche de la ligne 1235 dans OSM]({attach}images/20250823_bus_station/step4_unroll.png)

Si vous trouvez cette ligne, ajoutez-la dans JOSM (par exemple en utilisant Fichier > Télécharger un objet et en renseignant l'id OSM de la relation).

Si malgré vos recherches, vous ne la trouvez pas, c'est qu'il faut la créer : on va commencer par créer une ou plusieurs relations de trajet (avec *type=route* + *route=bus*). Ajoutons n'importe quel arrêt de votre gare routière dedans afin de ne pas laisser la relation vide. Puis on crée la relation ligne (avec *type=route_master* + *route_master=bus*) et on y met les trajets. Ne pas oublier de bien renseigner les tags descriptifs nécessaires, histoire que les contributeurs qui passeront derrière arrivent bien à retrouver ces nouveaux objets ...

L'outil [Réglisse](https://jungle-bus.github.io/transport-relation-creator/) peut vous éviter quelques copiés-collés : il propose un formulaire avec les informations de la ligne, et permet de charger les 3 relations dans JOSM avec les tags indispensables pré-remplis.

![Capture d'écran du site Réglisse, avec la création d'une ligne de bus]({attach}images/20250823_bus_station/step4_reglisse.png)

Et si vous avez ainsi créé des relations, vous pouvez envoyer vos modifications, c'est déjà pas mal !

Normalement, à la fin de cette étape, on a donc une petite coche devant chaque trajet qui passe dans la gare routière, et tous ces trajets sont accessibles dans notre session JOSM. Il ne reste plus alors qu'à relier tout ça.

**Étape 5 : première passe de modification des lignes**

À présent, nous allons passer sur chacun des arrêts de la gare routière, et l'ajouter dans les relations *route* des trajets qui s'y arrêtent.

Pour ne pas vous perdre en chemin, je vous conseille de les faire dans l'ordre de votre schéma. Le mode opératoire est simple :

- sélectionner l'arrêt
- vérifier dans l'encart Attributs les relations dont il est membre : ce n'est en effet pas nécessaire de l'ajouter dans une relation s'il en fait déjà partie
- si le trajet n'est pas dans la liste, cliquer sur ce trajet dans l'encart Relations, puis sur le bouton "Modifier la relation" en bas de l'encart
- dans la fenêtre de modification de la relation, ajouter l'arrêt (qui apparaît dans l'encart Sélection) dans la liste des membres (qui apparaît dans l'encart Membres) en utilisant les boutons. S'il y a déjà un autre arrêt de la gare routière dans la relation, on ajoute notre arrêt juste avant ou juste après afin de conserver l'ordre, puis on supprime l'arrêt initialement présent des membres (car il est rare qu'une ligne s'arrête à deux arrêts d'une même gare routière). Sinon, on peut l'ajouter tout en haut, mais il faut se noter de prendre du temps plus tard pour remettre tous les arrêts de ce trajet dans le bon ordre (par exemple avec un autre type de coche sur notre super schéma).
- valider
- recommencer pour tous les trajets de l'arrêt
- recommencer pour tous les arrêts

![Capture d'écran de JOSM : on y voit comment modifier un trajet pour ajouter un arrêt desservi, en préservant l'ordre de desserte]({attach}images/20250823_bus_station/step5_josm.png)

**Étape 6 : deuxième passe de modification des lignes**

À la fin de la première passe, on a les lignes desservies qui sont bien indiquées sur chacun des arrêts de la gare routière, mais il peut également y avoir encore d'anciennes associations lignes / arrêts qu'il nous faut à présent nettoyer.

Voici le mode opératoire :

- sélectionner l'arrêt
- dans l'encart Attributs, identifier les trajets qui n'ont rien à faire là (en s'aidant encore une fois du schéma)
- s'il faut supprimer le trajet, cliquer dessus dans l'encart Attributs et utiliser le bouton Supprimer de l'encart. JOSM vous demandera sûrement une confirmation (car vous êtes en train de modifier une relation alors que vous avez juste sélectionné un arrêt)

Bref, la manipulation est simple, mais vous verrez qu'elle nécessite en fait souvent pas mal de réflexion pour déterminer s'il faut supprimer le trajet ou s'il est légitime. En effet, il peut y avoir pas mal de cas particuliers.

Le cas le plus fréquent est celui des trajets qui sont terminus dans cette gare routière. Dans ce cas, il est rare qu'on ait de l'information voyageur à l'arrêt : en effet, personne ne monte ici, donc personne n'attend son bus à cet endroit, donc l'information voyageur n'est pas indispensable. On a donc potentiellement aucune info collectée à ce propos lors de notre visite terrain alors qu'il y a déjà des arrêts dans OSM dans les relations de trajet correspondant. Il faut alors "deviner" quel est le bon arrêt et modifier si nécessaire la relation de trajet. Je vois trois options :

- s'il y a un quai de "dépose voyageur" ou un "quai de descente" d'indiqué, c'est un bon candidat
- s'il y a un arrêt d'un autre trajet de la ligne dans la gare routière (le trajet retour par exemple), c'est également un bon candidat
- sinon, laisser l'arrêt déjà présent dans OSM faute de mieux

De même, il peut arriver qu'il y ait dans OSM des relations *route* pour des trajets spéciaux (le trajet spécial du matin qui passe devant l'école, ou le trajet spécial du mercredi qui a un autre itinéraire parce qu'il y a le marché) et qu'on ne trouve pas de trace de ces trajets dans l'information voyageur en gare lors du relevé. Là encore, on fait au mieux, et on essaye de trouver l'arrêt le plus probable, c'est-à-dire probablement l'arrêt qui est déjà desservi par le trajet habituel de la ligne dans ce sens.

Exemple : la ligne 1206 de mon exemple va généralement de la Gare de Cergy-le-Haut à la Gare de Pontoise Place du Général de Gaulle. Mais elle a tout de même des variantes. Sur cette fiche horaire (incomplète), on voit notamment

- une variante qui continue après la gare de Pontoise et va jusqu'à l'arrêt Stade C. Léon à Osny
- une variante qui dessert l'arrêt Maison d'Arrêt

![capture d'écran d'une fiche horaire, permettant d'identifier des variantes]({attach}images/20250823_bus_station/step6_hours.png)

Dans OpenStreetMap, on retrouve certains de ces trajets : en complément des deux trajets les plus fréquents, j'ai les trajets suivants :

- Gare de Cergy-le-Haut → Osny - Stade Christian Léon
- Gare de Cergy-le-Haut → Osny - Maison d'Arrêt → Gare de Pontoise - Place du Général de Gaulle
- Gare de Pontoise - Place du Général de Gaulle → Osny - Maison d'Arrêt → Gare de Cergy-le-Haut

Même si je n'ai pas d'information voyageur spécifique à ces trajets dans la gare routière, je peux déduire que l'arrêt qui dessert la ligne en direction de Gare de Pontoise - Place du Général de Gaulle est très probablement le même que celui de la variante qui va jusqu'au stade Christian Léon à Osny, et de la variante qui va à Pontoise en s'arrêtant à la Maison d'Arrêt d'Osny.

Bref, il va falloir investiguer un peu en s'aidant des grilles horaires des lignes et de l'information voyageur qu'on a pu collecter pour deviner où s'arrêtent les trajets.

Pour ne pas se perdre, je recommande de garder la trace (avec encore un autre type de coche sur le schéma) des arrêts nettoyés au fur et à mesure de notre passe de modifications.

**Étape 7 : nettoyage complémentaire des arrêts**

Encore une dernière petite passe sur les arrêts. Cette fois, on va s'intéresser aux tags que des contributeurs pourraient avoir mis sur l'arrêt pour indiquer les lignes qui s'y arrêtent. On souhaite en effet vérifier que les informations indiquées là sont ok, et à défaut les corriger ou tout simplement supprimer ces tags, qui sont en effet redondants avec les informations portées par les relations.

Le plus fréquent est le tag *route_ref*, qui contient généralement un ou plusieurs numéro de ligne. Ce tag sert surtout à indiquer cette information lorsqu'on n'a pas le temps ou l'outil qui va bien pour modifier proprement les relations, donc je ne l'édite jamais : je le laisse s'il est juste et je le supprime s'il indique des informations qui ne sont plus à jour. C'est particulièrement le cas en Île-de-France, où une campagne de renumérotation de toutes les lignes de la région est en cours depuis quelques années, et où les *route_ref* deviennent vite pleins d'informations obsolètes.

Il peut également y avoir des informations ajoutées via un tag *note*, *description*, *fixme* voire *operator*, pour les mêmes raisons. C'est l'occasion de vérifier si elles sont toujours d'actualité et de les supprimer le cas échéant.

Enfin, il peut y avoir des attributs d'interopérabilité avec les données open data, comme des codes pour accéder au temps réel des prochains passages à l'arrêt ou l'identifiant de l'arrêt dans le [GTFS](https://nlehuby.5apps.com/de-gtfs-a-osm.html), avec des attributs comme *ref:FR:qqch* ou *gtfs:qqch*. Là aussi des modifications de ces tags peuvent être nécessaires si vous avez beaucoup modifié la gare routière. Le mode opératoire dépend du contexte local, je vous laisse chercher par vous-même comment faire pour vérifier si les codes sont toujours bons et lesquels mettre à la place s'il faut les changer.

Comme d'habitude, gardez la trace de votre avancement sur votre schéma : vous pouvez barrer les arrêts au fur et à mesure de votre progression car c'était la dernière étape les concernant :)

![l'index des lignes de notre exemple précédent, tout plein de coches]({attach}images/20250823_bus_station/step7_schema.png)

Si vous êtes arrivés jusque là, félicitations ! Vous avez mis à jour les arrêts de la gare routière. Envoyez vos modifications et faites une petite pause pour célébrer.

**Étape 8 (optionnelle) : on prend les mêmes et on recommence**

S'il y a des stop_position dans votre gare routière, j'ai le regret de vous annoncer que vous pouvez tout recommencer !

Petit rappel théorique : les objets *public_transport=stop_position* sont des points placés sur la chaussée (donc des nœuds qui sont membres d'un objet *highway=residential/secondary/service/etc*). Ils servent à représenter l'endroit où le véhicule s'arrête (par opposition à nos arrêts habituels, avec *public_transport=platform* qui représente l'endroit où le voyageur attend le véhicule). On les retrouve assez systématiquement sur les modes de transport guidés comme le métro car historiquement, c'est plutôt cela qu'on cartographiait pour indiquer un arrêt (car les quais souterrains sont plus compliqués à tracer). Pour les bus, leur apport est moins évident.<br/>
Je recommande de ne pas s'embarrasser à les créer s'ils ne sont pas préexistants dans OSM car la complexité et la duplication d'information apportée ne me semble pas valoir le coup.

![illustration du modèle de données transport](https://nlehuby.5apps.com/images/20170528_bien_cartographier_les_bus/bus_stop_annote.png)

Donc s'il n'y a pas de stop_position dans votre gare routière, on peut passer cette étape.

En revanche, s'il y en a, il faut également modifier les relations des trajets pour que le bon stop_position soit référencé. Dans la pratique, j'en parle à présent par souci de clarification pédagogique mais le plus simple est de les traiter en même temps que les arrêts habituels. En effet, chaque arrêt habituel avec *highway=bus_stop* + *public_transport=platform* a en général un unique *public_transport=stop_position* correspondant, donc lorsqu'on ajoute ou supprime l'un à une relation, il faut également le faire sur l'autre.

**Étape 9 (bonus) : mise à jour des tracés**

Une relation de trajet est constituée de nos arrêts (les habituels *platform* et éventuellement les *stop_position*) dans l'ordre où ils sont desservis, ainsi que des routes qui constituent le trajet suivi par le bus, dans l'ordre où les rues sont parcourues.

Donc si on a modifié l'association des arrêts aux trajets, il peut être nécessaire de modifier un peu ces tracés, pour retirer ou ajouter un petit morceau des routes de la gare routière dans la relation. Comme pour l'étape précédente, il peut être plus efficace de mettre à jour les tracés lorsqu'on ajoute/supprime un arrêt plutôt que de le faire à la fin, à vous de choisir la méthode la plus simple pour ne pas perdre son fil et arriver au bout de votre index de lignes sans encombres.

À noter que cette étape n'est pas toujours réalisable : elle nécessite d'avoir au préalable cartographié les voies utilisées par les bus au sein de la gare routière, avec notamment les éventuels sens uniques pour pouvoir déterminer le trajet de chaque bus dans la gare routière. Dans les gares simples, ça peut être trivial mais dans certaines gares cela nécessitera un relevé dédié. De plus, ça dépend de la qualité des relations déjà existantes dans OSM : si aucun tracé n'est préexistant, il est tout à fait acceptable de passer cette étape.

**Étape 10 (bonus) : mise à jour de l'ordre des arrêts**

La relation de trajet contient les arrêts dans l'ordre où le bus les dessert, mais dans le cadre de la modification d'une gare routière, on fait un focus très restreint sur un arrêt. Il peut donc arriver qu'on sache qu'il faut ajouter un arrêt dans la relation de trajet, mais qu'on ne sache pas où dans la relation le placer.

Dans ce cas, j'ai suggéré (à l'étape 5) de l'ajouter tout en haut. Il est à présent temps de corriger cela en étudiant le trajet concerné dans sa globalité.

Pour cela, dans l'encart Relations, on clique sur la relation de trajet qu'on veut éditer, puis clic droit > Télécharger les membres

Puis il s'agit de parcourir le tracé s'il existe, en s'aidant de la grille horaire et/ou du plan de la ligne, pour remettre les arrêts dans le bon ordre.

Le plugin PT Assistant vous sera d'une grande aide pour mieux mettre en valeur la ligne courante, je vous recommande de l'activer si ce n'est pas déjà fait.

Là encore, griffonner sur notre schéma peut être utile pour suivre le travail à réaliser sur les différentes lignes.

**Étape 11 : peaufiner**

À ce stade, on a déjà fait du beau boulot et il ne reste plus grand chose à faire concernant la partie transport en commun. Mais si le relevé terrain était assez précis, il peut être intéressant de passer un peu de temps sur les cheminements dans la gare routière.

J'ai déjà mentionné les voies de bus, mais il est également intéressant de s'attarder sur les cheminements piétons, qu'on représente avec *highway=footway* :

S'il y a des passages piétons, on les ajoutera également, avec *highway=crossing* (et d'autres tags) sur le nœud à l'intersection avec la route, et *highway=footway* + *footway=crossing* pour tracer le cheminement piéton lui-même

S'il y a des bandes de guidage, on pourra les créer avec *highway=footway* + *footway=guiding_strips* + *tactile_paving=yes*.

Si on avait relevé les positions des éventuels toilettes, poubelles, bancs, arbres, etc, c'est le bon moment de les ajouter pour compléter le micromapping de la gare.

**Étape 12 : admirer son œuvre**

À partir de là, les différents outils qui utilisent OpenStreetMap et affichent des informations de transport vont pouvoir se mettre à jour (cela peut être plus ou moins long, un peu de patience) et bénéficier de vos modifications.

On peut bien sûr citer [l'application mobile OsmAnd que j'ai déjà mentionnée sur ce blog](https://nlehuby.5apps.com/plus_de_bus_osmand.html) ou [la carte Jungle Bus](https://jungle-bus.github.io/map/#18.31/49.049821/2.034086), qui affichent tous deux les informations des lignes desservis lorsqu'on sélectionne un arrêt.

Mais le meilleur endroit pour apprécier son travail est sûrement le site [Unroll](https://jungle-bus.github.io/unroll/bus_station.html?bus_station_id=w997211475) propose également une page dédiée aux gares routières qui reprend tous les éléments qui nous intéressent :

- les attributs de la gare elle-même
- la carte, qui permet de visualiser les emplacements des arrêts et leurs éventuels numéros de quai
- pour chaque arrêt, la liste des lignes desservies.

![Capture d'écran du site Unroll, avec la carte de la gare routière]({attach}images/20250823_bus_station/step12_unroll_1.png)

-

![Capture d'écran du site Unroll, avec le détail de quelques arrêts]({attach}images/20250823_bus_station/step12_unroll_2.png)

