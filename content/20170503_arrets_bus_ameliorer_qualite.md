Title: Améliorer la qualité des arrêts de bus dans OSM
Date: 2017-05-03 21:42
Author: nlehuby
Tags: #osm, #junglebus
Slug: mapsme-arrets-bus-ameliorer-qualite


Il y a un petit plus d'un mois, je vous proposais [une méthode étonnamment simple](/mapsme-arrets-bus-sans-nom.html) pour améliorer un peu la qualité des arrêts de bus dans OSM au quotidien, en ajoutant les noms lorsqu'ils manquaient.<br>
C'était trop facile, vous en voulez encore ?!

Ça tombe bien, [on l'a vu dans mon précédent article](/junglebus-soiree-de-lancement.html), il y a encore plein de choses à faire en Île-de-France sur le sujet :)<br>
En attendant que le projet [Jungle Bus](junglebus.io) ne nous permette de changer le monde en mettant toujours plus de réseaux de transport sur la carte, voici ce que vous pouvez déjà faire en Île-de-France :<br>
Un peu plus difficile que mon précédent challenge, je vous propose aujourd'hui d'ajouter dans OSM les lignes qui passent aux arrêts de bus.

Voici [une liste d'arrêts où aucune information n'est disponible sur les lignes qui s'arrêtent](https://ref-lignes-stif.5apps.com/autres/bussansligne.kml).<br>
Si vous la téléchargez sur votre mobile, vous pouvez visualiser tout cela dans MAPS.ME (en rose à présent)

![y en a plein !!!!]({attach}images/20170503_arrets_bus_ameliorer_qualite/plein.png)
Comme vous pouvez le voir, il y a du boulot.

Puis, quand on passe devant l'arrêt, on peut cliquer sur le signet, puis sur "AJOUTER DES LIGNES".
![sur le terrain, je me promène et je clique]({attach}images/20170503_arrets_bus_ameliorer_qualite/ajouter.png)

On ne peut malheureusement pas visualiser ou modifier les lignes qui desservent les arrêts dans MAPS.ME.<br>
On est en fait redirigé vers [MicrocOSM](https://microcosm.5apps.com), une autre webapp de mon cru ;)

NB : à la première utilisation, il faudra revenir à l'accueil de MicrocOSM pour se connecter à OSM, refermer la page, et refaire la manip depuis MAPS.ME

On peut alors cliquer sur Modifier.
![m'enfin clique !]({attach}images/20170503_arrets_bus_ameliorer_qualite/modifier.png)

Là, dans le champ TODO, on peut rechercher une ligne et l'ajouter.

![oh ! je peux chercher des lignes de bus !]({attach}images/20170503_arrets_bus_ameliorer_qualite/TODO.png)

Ne pas oublier de cliquer sur Enregistrer quand on a ajouté toutes les lignes ;)

Si vous ne trouvez pas votre ligne dans la liste, c'est probablement que la ligne n'existe pas encore dans OSM, ou qu'elle est en piteux état.<br>
Mais ça, ça sera peut-être l'objet d'un prochain challenge et d'un prochain article de blog !<br>
Quoiqu'il en soit, n'hésitez pas à me [contacter sur OSM](http://www.openstreetmap.org/message/new/nlehuby) si vous rencontrez des soucis.

Et si c'est encore trop facile pour vous, voici un autre challenge :<br>
[Tous ces arrêts de bus ont un tag FIXME](https://ref-lignes-stif.5apps.com/autres/busfixme.kml).<br>
Votre mission, si vous l'acceptez, est d'aller sur le terrain voir de quoi il est question, et de faire le nécessaire pour pouvoir retirer ce tag !

Quelques volumétries à date :

* [bus sans nom](https://nlehuby.github.io/kml_osm_survey/bussansnom.kml) : 3248
* [bus non desservi](https://nlehuby.github.io/kml_osm_survey/bussansligne.kml) : 10 097
* [bus avec FIXME](https://nlehuby.github.io/kml_osm_survey/busfixme.kml) : 101

Rendez-vous dans quelques semaines pour faire le bilan.

EDIT : un grand merci à prhod et Manu1400 pour leurs contributions opensource pour améliorer ces outils suite à la première publication de cet article ;)

EDIT octobre 2018 : mise à jour de liens (les fichiers kml sont maintenant hébergés sur github).
