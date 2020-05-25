Title: Retour d'expérience - cartographie OSM d'une gare routière (1 / 2)
Date: 2014-03-24 16:34
Author: nlehuby
Tags: #osm
Slug: retour-dexperience-cartographie-osm-dune-gare-routiere-1-2

Je trouve qu'il y a étonnamment peu de récit de ce genre sur le net,
donc aujourd'hui, je vous propose un retour d’expérience sur la
cartographie, dans OSM, d'une gare routière, puis des lignes de bus qui
y passent.

</p>

Premier article : une gare routière et ses arrêts de bus

</p>

[Deuxième article]({filename}retour-dexperience-cartographie-osm-dune-gare-routiere-2-2.md) : une gare
routière et quelles lignes s'y arrêtent

</p>

[Troisième article]({filename}retour-dexperience-cartographie-osm-de-quelques-lignes-de-bus.md) : on prend
le bus à la gare de routière, et on cartographie carrément toute la
ligne

</p>

Ceci n'est pas un tutoriel, mais uniquement un retour d'expérience !

</p>

 

</p>

Un peu de contexte tout d'abord : Boissy-Saint-Léger, ville du
Val-de-Marne (94) possède un pôle multimodal : on y retrouve, entre
autres, la gare RER (terminus de l'axe sud-est du RER A) et une gare
routière où passent près d'une dizaine de lignes de bus urbaines et
interurbaines, opérées par les transporteurs RATP, STRAV, SITUS et
SETRA.

</p>

Avant mon intervention, la gare routière n'est représentée que par un
unique arrêt de bus.

</p>

Autant dire qu'il y a du boulot ...

</p>
![image : sur le fond OSM]({attach}img/201404_carto_gare_12/tous-0.png)

</p>
</p>

**Étape 1 : le terrain**

</p>

Même si je passe tous les jours à cet endroit, je ne vais pas le
cartographier de tête … Donc un repérage sur le terrain s'impose.

</p>

Là, plusieurs méthodes existent : certains prennent énormément de photos
ou des vidéos panoramiques, certains notent tout sur papier, etc

</p>

Pour cette fois, j'opte pour la trace GPS.

</p>

J'utilise pour cela l'application *OSMTracker for Android TM* de mon
smartphone low cost :

</p>

-   J’active le GPS de mon téléphone, je lance l'appli, je démarre une
    nouvelle trace.
-   J'attends un peu que le GPS soit prêt et m'offre une géolocalisation
    suffisamment précise, et je commence à parcourir la gare routière.
-   Lorsque je passe devant un élément que je veux ajouter dans OSM, je
    l'indique sur l'application : arrêt de bus, poubelle, banc, horloge,
    etc

</p>

 

</p>

Premier arrêt de bus, ok, tout va bien, je me mets une note : c'est le
bus J2 qui s'arrête là.

</p>

Deuxième arrêt, ok, c'est la ligne 5. etc

</p>

Aïe, quatrième arrêt, pas la moindre indication : un abribus sans rien
écrit dessus. En terme d'info voyageur et de signalétique, on peut mieux
faire !

</p>

Mais c'est là qu'intervient la fameuse connaissance du terrain (*local
knowledge*) tant vantée des défenseurs d'OSM : comme je passe à cet
endroit tous les jours, je sais que c'est l'arrêt desservi par la ligne
12. Je me note mentalement de regarder demain le sens, car je n'ai
jamais pris cette ligne, je ne sais donc pas dans quelle direction va le
bus qui s'arrête là...

</p>

Je continue, jusqu'au huitième arrêt de bus, et j'arrête mon
enregistrement GPS ! Ça tombe bien, les gens commencent à me regarder
bizarrement en se demandant ce que je fais …

</p>

 

</p>

**Étape 2 : la saisie “facile”**

</p>

De retour chez moi, je transfère la trace GPS sur mon ordinateur.

</p>

Je lance ensuite l'éditeur de données JOSM, qui est particulièrement
adapté à ce type de saisie.

</p>

Je télécharge les données OSM déjà existantes pour les alentours de la
gare, je charge ma trace qui s'affiche alors également à l'écran, puis
j'affiche l'image satellite Bing, histoire d'avoir quelques repères
visuels.

</p>

C'est assez déroutant, les images satellite au zoom max sont très
anciennes et ne correspondent pas du tout à l'état actuel de la gare
routière (le pôle multimodal a été refait à neuf en 2009), tandis qu'à
un zoom moins important, on a bien notre gare routière telle que je la
vois tous les jours … Mais il suffit de ne pas trop zoomer pour
retrouver ses petits.

</p>

C'est parti !

</p>
![image : jOSM]({attach}img/201404_carto_gare_12/josm.png)

</p>
</p>

 

</p>

Je commence par ce qui me tient le plus à cœur : les arrêts de bus !

</p>

En me basant sur l'image satellite (l'ombre des abribus est très
visible) et sur ce que j'ai récupéré avec mon smartphone, j'ajoute mon
premier arrêt de bus.

</p>

*highway = bus\_stop*

</p>

Il est abrité et possède un banc donc j'ajoute les attributs

</p>

*shelter = yes*

</p>

*bench = yes*

</p>

 

</p>

Puis là, CTRL+C, CTRL+V pour les 7 autres car ils ont tous les mêmes
caractéristiques.

</p>

Pour que ça soit complet, il faudrait que j'indique quelles lignes
s'arrêtent à ces abris, mais c'est une étape légèrement plus délicate,
qui fera l'objet d'une seconde saisie (dans l'article suivant).

</p>

À la place, j'ajoute un attribut note avec comme valeur les lignes,
ainsi que les directions quand je les ai.

</p>

J'ai également noté que les abribus avaient tous un panneau indiquant un
nom de quai. Un peu étrange comme terminologie mais soit … J'ajoute donc
également un attribut *ref* avec comme valeur le nom du quai (de A à I)

</p>

 

</p>

Ensuite, j'ajoute les deux bancs qui se situent sur les côtés (*amenity
= bench*) ainsi que l'horloge (*amenity = clock*).

</p>

Il y a aussi deux poubelles, mais pas moyen de me rappeler de l'attribut
à utiliser.

</p>

Je commence à faire des recherches dans le wiki, mais ça n'est pas
immédiat.

</p>

Heureusement, je me souviens que j'ai mappé il y a quelques mois une
poubelle dans une rue à proximité de la gare. Je vérifie le valeur de
l'attribut (*amenity = waste\_basket*), et voilà !

</p>

 

</p>

Il ne reste plus qu'à envoyer tout ça dans OSM.

</p>

 

</p>

Quelques instants plus tard, je retourne sur la carte pour voir un peu
ce que ça donne. C'est finalement un peu décevant : au lieu d'un unique
picto pour représenter la gare routière, on a maintenant 7 pictos tous
serrés (le huitième ne s'affiche qu'au zoom max car il est trop proche
de la sanisette …) et un peu moches. Mais bon, il parait qu'”on ne
cartographie pas pour le rendu” !

</p>
![image : rendu]({attach}img/201404_carto_gare_12/rendu.png)

</p>
</p>

**Étape 3 : retour sur le terrain et corrections en conséquence**

</p>

Le lendemain, je regarde avec un peu plus d'attention le ballet des bus
pour noter où s'arrêtent ceux que je n'ai jamais pris.

</p>

Je retrouve ainsi les directions de mon bus 12 et surprise : un arrêt
que je n'avais encore jamais remarqué !

</p>

C'est un simple poteau, là où les autres sont des abris, et le bus 6
(dont je n'avais jamais entendu parler avant ...) s'y arrête.

</p>

Hop hop hop une seconde saisie pour ajouter tout ça et le tour est joué
!

</p>

 

</p>

J'ajoute également la route empruntée par le bus (qui est une voie
réservée aux bus), et voilà, on a quelque chose d'assez proche de la
réalité :

</p>
![image : rendu final]({attach}img/201404_carto_gare_12/rendu_final.png)

[La suite, dans l’article
suivant]({filename}retour-dexperience-cartographie-osm-dune-gare-routiere-2-2.md) !
