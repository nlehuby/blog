Title: OpenBeerMap – où trouver ma bière préférée ?
Date: 2014-05-19 16:43
Author: nlehuby
Tags: #osm, #hack, #firefoxos
Slug: openbeermap-ou-trouver-ma-biere-preferee

**EDIT** : pour suivre l'actualité d'OpenBeerMap, suivez le mot-dièse
\#OpenBeerMap et le journal
OSM <https://www.openstreetmap.org/user/OpenBeerMapContributor/diary>

Parfois, lorsque je sors avec des acolytes, on se retrouve dans un bar
qui sert une bière blonde <s>dégueulasse</s> <s>tout juste bonne à faire
des panachés</s> classique, et on découvre en sortant que le bar d’à côté
sert de la bière belge d’abbaye.

</p>

Je ne suis pas une grande amatrice de bière, mais je trouve ça plutôt
frustrant.

</p>

Et qui dit frustration dit besoin sous-jacent.

</p>

Et qui dit besoin dit « il me faut une application pour ça ! »

</p>

 

</p>

Bref, c’est ainsi qu’il m’est venu l’idée de faire une carte affichant
les bars et les bières qui y sont servies, à partir des données
OpenStreetMap bien sûr !

</p>

Le résultat est visible ici : <http://openbeermap.github.io/>

</p>

 

</p>

Voici comment ça s’est déroulé.

</p>

Bon, j’ai commencé par apprendre les bases du javascript (parce que mon
langage de prédilection, c’est plutôt le python, mais c’est quand même
nettement moins adapté pour faire des cartes sur le web).

</p>

Je suis parti d’un plugin Leaflet (qui est un bibliothèque javascript
efficace pour afficher des cartes) pour [afficher des données à partir
de l’API
Overpass](https://github.com/kartenkarsten/leaflet-layer-overpass).

</p>

L’API Overpass (qui est testable sur cet IDE
(<http://overpass-turbo.eu/>) permet de faire des requêtes sur les
données OSM avec toutes sortes de filtres.

</p>

Dans mon cas, c’est *amenity = pub* (ou *bar* ou *cafe*) et *brewery =
{nom de ma bière}*

</p>

 

</p>

Assez rapidement et sans y connaitre grand-chose, j’ai pu faire une joli
carte avec des cases à cocher pour les différents types de bière :

</p>
![image : OBM]({attach}img/media_crop/66/public/201405/openbeermap1.png)

</p>

 

</p>

Puis, j’ai intégré tout ça dans
[BootLeaf](https://github.com/bmcbride/bootleaf), une template basé sur
Leaflet et Bootstrap, afin d’avoir quelque chose de responsive et
surtout de plus joli, notamment sur mes info-bulles

</p>

![image : OBM]({attach}img/media_crop/71/public/201405/openbeermap2.png)

</p>

 

</p>

Puis, je me suis rendue compte que j’avais pas beaucoup de bars où
l’information était fournie …

</p>

Un petit tour sur
[Taginfo](http://taginfo.openstreetmap.fr/keys/brewery) m’apprend qu’il
n’y a que 15 objets dans OSM sur toute la France avec le tag brewery de
renseigné !

</p>

Autant dire qu’il y a du travail de contribution à prévoir si je veux
que mon site ait vraiment un intérêt.

</p>

 

</p>

Du coup, j’en profite pour rajouter un petit formulaire permettant de
renseigner directement sur le site les bières dispo, et les autres infos
pertinentes (pour l’instant, j’ai retenu uniquement nom du bar, accès
wifi, heures d’ouverture et heures d’happy hours) :

</p>

![image : OBM]({attach}img/media_crop/76/public/201405/openbeermap3.png)

</p>

Les informations saisies dans le formulaires partent directement
enrichir la base de données OpenStreetMap, ce qui me permet de les
re-consommer derrière pour afficher quelles bières sont dispo : un
cercle vertueux à consommer sans modération ;)

</p>

C'était la partie la plus délicate à réaliser pour moi qui n'était pas
familière avec l'API d'édition d'OSM et toute la cinématique nécessaire
pour réaliser des modifications ... D'ailleurs, la gestion des conflits
a été soigneusement éludée pour le moment...

</p>

 

</p>

Bon, j’ai finalement temporairement retiré les heures (opening\_hours et
happy\_hours) car je pense qu’un simple champ texte n’est pas très
adapté pour enrichir ce type de donnée : j’oublie moi-même tout le temps
le format de ce tag et je n’ai pas très envie d’implémenter une
vérification du format dans le formulaire, donc ce n’est pas optimal …
affaire à suivre.

</p>

 

</p>

Maintenant, y a plus qu’à !

</p>

Je compte sur vous pour participer et ajouter les bières servies dans
vos débits de boisson favoris.

</p>

 

</p>

Et sinon, c’est tout open-source, et toute contribution est la
bienvenue !

</p>

Par exemple, si une âme charitable avec des compétences en graphisme
pouvait me fournir des images (en SVG et libre de droit) des verres à
bières, ça serait merveilleux. J’ai essayé de dessiné le verre de la
Kwak … mais j’ai renoncé !

</p>

*EDIT* : c'est chose faite, tout juste 4 mois après le lancement du
projet : Affligem, Carmélite Triple, Chouffe, Guinness et même Kwak ont
leurs icônes intégrées dans OpenBeerMap 

</p>

![image : kwak]({attach}img/201409/obm.png)

</p>

Et l'ergonomie pourrait être améliorée sur le choix des bières (aussi
bien sur l'affichage que la contribution) j'imagine.

</p>




