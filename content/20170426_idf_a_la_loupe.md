Title: Les réseaux d'Île-de-France à la loupe
Date: 2017-04-26 21:17
Author: nlehuby
Tags: #osm, #junglebus
Slug: junglebus-soiree-de-lancement

Ceci est, à peu de chose près, la retranscription de la présentation que j'ai donnée hier, à la soirée de lancement du projet [Jungle Bus](http://junglebus.io/), qui vise à révolutionner la production des plans de transport, en s'appuyant sur le crowdsourcing et OpenStreetMap.

![couverture]({attach}images/20170426_junglebus_lancement/couverture.png)

La plupart des villes du monde n'ont pas de plan de transport.<br>
Mais qu'en est-il de la votre ? Qu'en est-il de la mienne ?<br>
J'ai fait l'expérience, j'ai cherché un plan de transport de là où j'habite actuellement.

J'ai commencé par regarder du côté du STIF ; voici ce qu'ils proposent :<br>
![plan STIF]({attach}images/20170426_junglebus_lancement/plans/STIF.png)
source : [STIF](http://vianavigo.com/fileadmin/galerie/pdf/REGION_GF_V2016-02_p.pdf)

On retrouve quelques lignes : la ligne 100, les deux lignes 18, la ligne 19.<br>
Mais c'est un plan schématique qui n'affiche que les lignes structurantes : des choix de représentation ont dû être faits, toutes les lignes ne sont pas présentes, et on ne sait pas vraiment où elles passent et si on peut les prendre.<br>
On retrouve également les lignes Bus Direct qui, à ma connaissance, ne s'arrêtent pas, voire ne passent pas du tout ici.

Essayons en un autre ; voici celui de la RATP :<br>
![plan RATP]({attach}images/20170426_junglebus_lancement/plans/RATP.png)
source : [RATP](http://www.ratp.fr/informer/pdf/orienter/f_plan.php?fm=pdf&loc=secteur&nompdf=secteur11)

Celui-ci est plus précis, et prend en compte la réelle géographie de la ville : on voit des cours d'eau, des forêts, quelques rues.<br>
En terme de transport, on a maintenant des tracés, et des indications des arrêts. On retrouve les lignes RATP, la 211, la 220, la 321, la 421. On retrouve aussi la ligne 100 déjà présente sur le plan schématique du STIF.<br>
Bon ce n'est pas parfait, la ligne 100 n'est pas rouge mais bleue en réalité.<br>
Et les deux lignes 18 et la ligne 19 ?

Voyons celui du réseau Noctilien :<br>
![plan Noctilien]({attach}images/20170426_junglebus_lancement/plans/noctilien.png)
source : [Noctilien, STIF](http://vianavigo.com/fileadmin/galerie/pdf/NOCTILIEN_SE_2015-11_p.pdf)

Là encore c'est un plan qui tient compte de la géographie, mais sans surprise, seules les lignes du réseau Noctilien sont indiquées.<br>
Bon point tout de même, on a, en supplément de leur positions, les noms des arrêts.
J'y vois tout de même des positions qui me semble légèrement fausses.

Enfin, un petit dernier, proposé par le réseau Pep's<br>
![plan Pep's]({attach}images/20170426_junglebus_lancement/plans/Transdev.png)
source : [Transdev idf](http://www.transdev-idf.com/Plan-plan_de_reseau_pep's_a_partir_du_1er_septembre_2016-amv-pep's_051)

Celui-ci est vraiment pas mal !<br>
On a à présent une liste exhaustive de toutes les lignes de transport, et pas uniquement celles du réseau Pep's. On retrouve bien les lignes structurantes (la 100, les deux 18 et la 19), les lignes RATP citées plus tôt, les lignes Noctilien citées plus tôt, les lignes Pep's évidemment, et les quelques autres.

Mais faisons l'exercice, que donnerait un plan réalisé à partir des données OpenStreetMap ?<br>
Voici le fond transport actuel officiel du projet OpenStreetMap
![plan OSM]({attach}images/20170426_junglebus_lancement/plans/osm.png)
source : [OSM fond Transport](http://www.openstreetmap.org/#map=16/48.8373/2.6508&layers=T)

On ne va pas se mentir, ce n'est pas génial.<br>
On a des tracés, on a des numéros de lignes, on a des arrêts et des noms d'arrêts, mais c'est pas bien clair qui appartient à quoi.<br>
Pour les couleurs de lignes, on repassera : elles ont beau être renseignées, elles ne sont pas affichées. Et quant à savoir si toutes les lignes citées plus haut y sont, c'est loin d'être évident.<br>
C'est d'ailleurs un des objectifs du projet [Jungle Bus](http://junglebus.io/) : fournir un rendu cartographique des réseaux de transports lisible et exploitable.

Mais en attendant, essayons au moins de connaitre l'exactitude de cette carte.<br>
Pour cette zone géographique, je la connais, j'en ai cartographié moi-même une partie significative.
Mais à l'échelle de l'Île-de-France, quelle exactitude aurait un plan de transport fait à partir d'OSM ?

Voyons déjà la quantité d'information disponible :<br>
Si je compte les arrêts de transport de la région, j'en ai plus de 20 000 !
![arrêts OSM]({attach}images/20170426_junglebus_lancement/arrets/stops_osm.png)
source : <3 les contributeurs OSM (arrêts et contours)

Ok, ça fait beaucoup, mais est-ce qu'ils y sont tous ?<br>
Pour le savoir, c'est plus simple qu'il n'y parait !<br>
En effet, le STIF, qui organise et finance les transports publie un certain nombre d'informations sur son portail opendata, [j'en parlais déjà dans un précédent article](/les-donnees-horaires-du-stif-en-opendata.html).<br>
La liste et la position de tous les arrêts d'Île-de-France sont donc facilement récupérables et utilisables en comparaison.<br>
Voici la différence entre OSM et les données STIF, que nous considérerons ici comme la représentation la plus juste de la réalité en terme de quantités d'arrêts:<br>
![comparaison OSM/STIF sur les arrêts]({attach}images/20170426_junglebus_lancement/arrets/diff_osm_stif.gif)
source : données OSM (c) contributeurs OSM / données STIF - [portail opendata](https://opendata.stif.info/explore/dataset/offre-horaires-tc-gtfs-idf/)

Il en manque. Beaucoup. Surtout sur les bords.<br>

En réalité, le tableau est même plutôt sombre.<br>
Si on voulait faire un plan de transport de la région Île-de-France, il ressemblerait à ça : d'un côté une carte avec les lignes tracées, et de l'autre une liste des lignes pour pouvoir les retrouver facilement.<br>
![plan typique]({attach}images/20170426_junglebus_lancement/plans/plan_typique.png)

Si on réalisait aujourd'hui ce plan avec OSM, on aurait plutôt cela :<br>
![plan fait avec OSM]({attach}images/20170426_junglebus_lancement/plans/plan_osm.png)

Oui, plus de la moitié des lignes est aujourd'hui manquante dans OSM !<br>

Et tout cela donne une représentation faussée et inégale du territoire. Car les lignes cartographiées sont probablement les plus empruntées et celles où il y a le plus de contributeurs.<br>
La répartition des arrêts le montrait déjà, mais en voici un exemple encore plus frappant : voici le nombre de lignes par réseau, dans OSM, et dans les données du STIF :<br>
![diff de la répartition des lignes par réseau]({attach}images/20170426_junglebus_lancement/diff_reseaux.gif)
source : données OSM (c) contributeurs OSM / données STIF - [navitia.io](http://navitia.io)

On a ici une sur-représentation des données RATP et Noctilien, au détriment de la centaine d'autres réseaux qui co-existent en Île-de-France.<br>

Parlons un peu qualité à présent.<br>
Les données OSM sont réputées pour leur qualité, car c'est bien connu, les contributeurs prennent ce sujet très au sérieux.
![craftmapper]({attach}images/20170426_junglebus_lancement/craftmapper.png)

Le premier indicateur sur lequel OSM brille en général, c'est la précision de la position des arrêts.<br>
Voici à quoi ressemble la gare routière de Torcy, d'après notre référence, le STIF :
![opendata]({attach}images/20170426_junglebus_lancement/torcy/opendata.png)

L'accumulation d'arrêts superposés semble peu crédible, mais le reste semble ok.<br>
Mais sur le terrain, les arrêts sont régulièrements espacés sur des espaces piétons entourés de voies de bus.  Voici à quoi ça ressemble dans OSM, et en réalité :
![osm]({attach}images/20170426_junglebus_lancement/torcy/osm.png)

Rien de dramatique à première vue, on pourrait croire que les arrêts sont placés à quelques mètres près.<br>
Mais en faisant l'effort de regarder à quel arrêt OSM correspond un arrêt opendata, c'est nettement moins glorieux :
![diff]({attach}images/20170426_junglebus_lancement/torcy/diff.png)

Difficile de trouver un arrêt opendata bien positionné :(<br>
Donc impossible pour un voyageur qui ne connait pas le coin de faire sereinement une correspondance en s'appuyant sur l'information voyageur officielle mise à sa disposition : l'arrêt qu'on lui demande de trouver risque d'être sur le trottoir d'en face voire à l'autre bout de la gare routière ...

Autre point sur lequel OSM se distingue souvent : la réactivité en cas d'évolution sur le réseau.<br>
Il n'est en effet pas rare que les données OSM tiennent compte des nouveaux arrêts et prolongements de lignes un peu avant la mise en service, et plusieurs semaines avec la mise à jour dans l'opendata.
![twitter]({attach}images/20170426_junglebus_lancement/twitter.png)
La ligne de tramway 11, dont la mise en service est prévue pour juillet prochain est par exemple déjà en partie dans OSM.

Enfin, un dernier indicateur, un peu plus objectif et global à l'échelle de l'Île-de-France pour sortir du cas particulier dont on sait difficilement s'il est généralisable :<br>
En Île-de-France, chaque arrêt de bus a un nom, ce qui permet de le retrouver sans trop de difficultés sur un plan de ligne ou une grille horaire (même si on retrouve tout de même régulièrement sur le terrain des abribus dépourvus complètement d'information voyageur). Qu'en est-il dans OSM ? Combien d'arrêts ont un nom dans OSM ?<br>
![84 % des arrêts de bus ont un nom]({attach}images/20170426_junglebus_lancement/bus_sans_nom/noms.png)

Bref, même si ce n'est pas parfait, OSM semble se distinguer sur la qualité. Mais on l'a vu, côté quantité, plus de la moitié des données est manquante.<br>
Alors quoi ? c'est peine perdue, il faut laisser tomber l'idée de cartographier les réseaux de transport à partir d'OpenStreetMap ?

Non, bien sûr que non, on y croit !

Je sais, depuis longtemps, que cartographier du transport, c'est difficile, j'en ai déjà beaucoup parlé ici sur ce blog.
Et j'ai lancé un projet dans la communauté OSM en décembre dernier, autour du transport en Île-de-France : il s'agit de renseigner les identifiants du référentiel STIF dans les données OSM afin de pouvoir les relier et les comparer plus facilement (Le projet est toujours en cours, rejoignez-le [ici](https://framateam.org/bato-fr/channels/stif))

Ce petit projet a permis de dresser ce constat un peu triste de l'état de la cartographie transport en Île-de-France.

Mais surtout il a permis d'expérimenter des nouvelles choses. Voici quelques petits outils que j'ai pu mettre en place (article plus détaillé à venir ;))

Le rendu de transport n'est pas satisfaisant : on n'arrive pas à savoir si une ligne y est vraiment présente ou pas ?
Tentons une autre forme de représentation : voici une liste. Si tu cherches la ligne 12 du réseau Pep's, cherche "12" ou cherche "Pep's" et tu sauras.
![vue toutes les lignes]({attach}images/20170426_junglebus_lancement/outils/vues_toutes_lignes.png)

Difficile de savoir si une ligne est déjà bien renseignée ou s'il reste du travail à faire dessus ? Voici une vue qui met en valeur les tracés et les potentiels arrêts non cartographiés en s'appuyant encore une fois sur l'opendata STIF :
![vue tracé ligne]({attach}images/20170426_junglebus_lancement/outils/vizu.png)

Il est difficile de voir si un arrêt est bien cartographié avec la liste des lignes qui y passent dans OSM. C'est en effet une information un peu complexe à ajouter pour un débutant et non mise en valeur sur les rendus. Voici une vue qui l'affiche explicitement et permet d'ajouter celles qui manquent.
![vue microcosm]({attach}images/20170426_junglebus_lancement/outils/microcosm_popup.png)

Ajouter un nom sur un arrêt de bus, c'est parfaitement trivial ! Il n'est pas acceptable qu'on ait encore des arrêts de bus sans nom dans OSM.<br>
[Voici une solution pour y remédier](/mapsme-arrets-bus-sans-nom.html)

Et les résultats sont là : en quelques mois, un travail incroyable a été réalisé :<br>
![ce sont plus de 150 lignes de bus qui ont été ajoutées à OSM]({attach}images/20170426_junglebus_lancement/progression.png)

C'est une progression, certes pas fulgurante, mais régulière et significative, qu'on a pu observer ces quelques derniers mois.

Alors oui, en voyant ces résultats, on est rassurés : on peut révolutionner la production des plans de transport avec OSM. Après tout combien de réseaux ont plus de 150 lignes ?

Faisons confiance à la force des contributeurs. Avec les bons outils, on peut y arriver : soutenez le projet [Jungle Bus](http://junglebus.io/) !

Enfin, un dernier point : les données OSM sont aussi en opendata.<br>
Et l'opendata, c'est une opportunité de jouer collectif.<br>
Même s'il y a des trous d'offre, il est déjà possible aujourd'hui, pour un exploitant, un transporteur, une municipalité, etc de regarder ce qu'OSM propose et pourquoi pas d'en tirer parti.<br>
Il est déjà possible d'extraire les positions des arrêts d'OSM pour des comparaisons et pourquoi pas des corrections.
Il est déjà possible, pour les réseaux qui ne présentent que des schémas de lignes en thermomètre peu détaillé de tirer parti des tracés présents dans OSM pour proposer une carte plus détaillée.<br>
Les synergies possibles sont nombreuses, et la communauté [Jungle Bus](http://junglebus.io/) est prête à expérimenter et co-construire afin que les données OpenStreetMap ne soient plus considérées comme une autre base, ou une base concurrente, mais bien comme une base complémentaire, dans laquelle il y a du bon à puiser dès aujourd'hui !


**EDIT avril 2018** : Un an plus tard, j'ai co-réalisé pour Jungle Bus [un audit comparatif entre les données officielles en opendata et les données OSM sur les bus](http://junglebus.io/iledefrance/audit_2018_04/). N'hésitez pas à le consulter pour encore plus de détails chiffrés.
