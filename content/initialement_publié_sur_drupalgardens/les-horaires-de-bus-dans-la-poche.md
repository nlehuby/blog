Title: Les horaires de bus dans la poche
Date: 2015-06-11 15:23
Author: nlehuby
Tags: #hack, #opendata, #firefoxos
Slug: les-horaires-de-bus-dans-la-poche


Je me suis enfin décidée à publier [ma deuxième application
FirefoxOS](https://marketplace.firefox.com/app/horaires-bus/).



Elle a une mission très simple : sauvegarder et restituer les horaires
théoriques de passage de bus à un arrêt.



Son fonctionnement est simple : en deux étapes



**l'initialisation** (quand j'ai une connexion internet)



-   je choisis mon arrêt.
-   je sélectionne la ligne et la direction
-   je vois alors les horaires, et je peux les enregistrer

![init]({attach}img/201506/01.png)



**l'utilisation** (quand je suis en déplacement, potentiellement sans
connexion internet)



-   je vois la liste de mes fiches horaires enregistrées
-   je sélectionne celle que je veux, et je consulte les horaires

![liste]({attach}img/201506/02.png) ![détail]({attach}img/201506/03.png)



Cette application utilise les données opendata d'Île-de-France, grâce à
l'API [navitia.io](http://navitia.io)



Si vous voulez l'utiliser ailleurs, faites-moi signe : si votre région
est couverte par navitia.io, je peux vous en déployer une version avec
les horaires qui vous intéressent.



Cette application a été initiée pendant un hackathon chez Mozilla Paris
en novembre 2014, puis peufinée par mes soins avec plus ou moins
d'assiduité et de motivation pendant plusieurs mois.



C'est bien sûr open-source [si vous voulez contribuer au code ou
remonter des bugs](https://github.com/nlehuby/Transport_Schedules). Si
vous voulez supporter le coût de développement (énorme !) de l'appli,
j'accepte les
[Flattries](https://flattr.com/thing/f9d454c6ae5459f245a4d6014fb1c4a2)
(et les bières, toujours).



 



Le but initial était de pouvoir avoir toujours sur moi les horaires de
mon bus de banlieue peu fréquent, pour adapter mon itinéraire en
connaissance de cause, et ce même si ça ne capte pas ...



Dans la pratique, j'ai déménagé depuis et ne prends plus ce bus de
banlieue, et ses horaires ne sont toujours pas en opendata, donc
j'aurais une utilisation assez limitée de l'application.



*EDIT : le STIF a ouvert les données transport théoriques de toute
l'Île-de-France donc ... l'appli fonctionne à présent sur les bus de
banlieue !*



J'espère que d'autres en auront l'usage ou sauront s'en inspirer pour
d'autres utilisations.



 
