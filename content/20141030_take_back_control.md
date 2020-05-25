Title: Reprenez le contrôle de votre Android
Date: 2014-10-30 16:44
Author: nlehuby
Tags: #android, #firefoxos, #vie_numérique
Slug: take-back-control

> Si un jour on vous avait dit que vous seriez espionné par votre lampe

> de poche, vous auriez crié au Philippe K Dick http://t.co/IFSUJbUYqd

> ![twitter_img](https://o.twimg.com/2/proxy.jpg?t=HBhQaHR0cDovL2ltZy5waG9uYW5kcm9pZC5jb20vMjAxNC8xMC9hcHBsaWNhdGlvbnMtbGFtcGUtcG9jaGUtY29sbGVjdGUtZG9ubmVlcy5qcGcU-AoU3AUcFIQGFJQDAAAWABIA&s=fe-LM2U4jCwNbTc24kEHOz9a4L_pckrTMA0hoz35plQ)

> — Jean-noël Lafargue (@Jean_no) [October 29, 2014](https://twitter.com/Jean_no/status/527364492624429056)

La lecture récente de ce tweet ainsi que ma participation à l'OpenWorldForum, dont le thème pour cette année était "Take back control", m'ont incitée à écrire cet article que j'avais en tête depuis fort longtemps.

En effet, il y a quelques mois, j'ai voulu télécharger une application de lampe de poche. Un truc tout con qui allume le flash de l'appareil photo en un clic et dont on peut mettre un raccourci sur son bureau. Je me suis donc rendue sur le marché d'application de mon smartphone Android et ai recherché une application répondant à ce besoin.

Et là, j'avoue que j'ai été fort étonnée.

Déjà, par le poids des applications. C'est une info assez peu mise en valeur, il faut chercher un peu pour trouver combien pèse une application. Mais j'ai un passif d'utilisation d'un smartphone low cost, le genre où il faut désinstaller les mises à jour des applications systèmes pour être bien sûr d'avoir assez d'espace dispo pour recevoir ses SMS ... donc c'est une information que je regarde toujours avec attention.

Donc bref, les premières applications proposées pesaient aux alentours de 5 Mo.<br>
J'ai souvenir d'avoir utilisé (en dépannage) une distribution linux complète pesant à peine le double ! M'enfin bref, admettons que je me résigne à en installer une tout de même.

Et là surprise, pour allumer la lampe de mon appareil photo, elle me demande des autorisations tout à fait incongrues telles que l'accès à mes contacts (WTF ??).<br>
Le site Snoopwall a d'ailleurs tout récemment publié un article [dressant également ce constat](http://www.phonandroid.com/mefiez-vous-applications-lampe-poche-vous-etes-espionnes.html).

En plus parano. Moi, je m'étais naïvement dit que les développeurs avaient dû coder ça dans l'urgence et dans le besoin d'une lampe de poche, et qu'ils avaient oublié de retirer les dépendances et les autorisations non nécessaires ... Ah, l'insouciance du grand public :p

Donc bref, ceci n'est qu'un exemple tout à fait quelconque, mais cela fait réfléchir à ce que les gens mettent dans les applications que nous installons les yeux fermés parce que c'est pratique et que la distribution de nos données privées ne nous tracasse pas plus que ça.

Mais plutôt que de se lamenter, je vous propose de vous parler de deux alternatives, qui apportent des solutions à ces deux problèmes cités plus haut.

**Fuir les applis qui nous espionnent** <br>
Étonnamment, la solution à ce problème est assez simple. Il se trouve qu'il existe un autre marché d'application, ne proposant que des logiciels opensource et fournissant des indications sur le niveau de confiance que l'on peut attribuer à ces applications. Ça s'appelle [F-droid](https://f-droid.org/), et c'est téléchargeable et installable sur son téléphone de manière tout à fait triviale.<br>
Ce que j'apprécie particulièrement, c'est le fait qu'il prenne en charge les applications déjà installées.<br>
Par exemple, lorsque j'ai installé F-droid, il m'a indiqué que j'utilisais les applications suivantes qu'il avait lui-même dans sa base d'applications : [OSMTracker](https://f-droid.org/repository/browse/?fdfilter=osmtracker&fdid=me.guillaumin.android.osmtracker) (une appli de contribution à OSM qu'elle est bien) ou encore Firefox.<br>
Lorsqu'on navigue sur une application, en plus de la description de l'application, il nous propose (en gros, gras et rouge) des avertissements sur l'application. Par exemple, pour Firefox, il me met en garde du fait que "cette application promeut des extensions privatives" (en effet, des addons peuvent être installés, et ne sont pas nécessairement opensource(s?)) et également que "cette application épie et rapporte votre activité (en effet, des stats sont envoyés régulièrement aux développeurs pour améliorer le navigateur ; fonctionnalité bien sur désactivable dans les paramètres).<br>
Nous voilà informés et donc en mesure de faire des choix pertinents !

Quelques points négatifs tout de même : je suis souvent tombée sur des applications peu abouties et où il fallait un peu lutter pour trouver comment ça marche (voire même ce que ça rend comme service).<br>
Ce n'est pas sans rappeler les applications libres d'il y a quelques années, où rien qu'à voir l'IHM, on sentait bien que ça avait été fait par des geeks qui en avaient eu le besoin et non par une entreprise qui fait un logiciel pour rendre un service facturé à des utilisateurs clients ...<br>
Mais pas de généralisation hâtive, on y trouve également quelques applications très satisfaisantes : j'ai par exemple découvert avec surprise [Twidere](https://f-droid.org/repository/browse/?fdfilter=twidere&fdid=org.mariotaku.twidere), qui est un client Twitter que j'utilise maintenant régulièrement.<br>
J'y ai également trouvé [ma lampe de poche](https://f-droid.org/repository/browse/?fdfilter=torch&fdid=com.colinmcdonough.android.torch), qui pèse 112 ko (oui oui), est distribuée sous licence Apache 2 et ne demande que l'autorisation d'accéder à mon appareil photo et de bloquer l'extinction automatique de l'écran pendant qu'elle est en cours d'utilisation.<br>

F-droid répond à la problématique des applications qui, sous prétexte de gratuité, bafouent notre droit à la vie privée. Mais ça ne répond pas nécessaire au problèmes des applications codées avec les pieds qui prennent tout l'espace disponible sur le téléphone inutilement.<br>
Pour répondre à ce problème, j'ai trouvé une solution du côté de Mozilla.

**Fuir les applications qui pèsent trop lourd** <br>
Pour bien comprendre, je pense qu'il est important de resituer le contexte. Contrairement à ce qu'on pourrait naïvement penser, Mozilla est une fondation qui a pour objectif, non pas de conquérir le monde avec un navigateur qui ressemble à un renard de feu / un panda roux. Non, Mozilla a pour but de favoriser l'accès à internet. De désenclaver les utilisateurs enfermés dans leurs systèmes privateurs en leur offrant un accès universel (notemment via le web).<br>
Le navigateur Firefox est un outil qui répond très bien à ce besoin.<br>
Thunderbird également, en nous rappelant que le mail est un outil de communication et non un logiciel Microsoft ou une IHM web de Google.<br>
Et pour le mobile, les applications Firefox pour Android répondent également à ce besoin.<br>
En effet, ces applications sont des encapsulations d'applications web qui s'installent et s'utilisent comme des vraies applications Android.

L'intégration des ces applications dans l'éco-système Android est réellement bluffant : ces applications

* s'installent comme des app android à partir d'un marché d'applications
* sont listées avec les autres applications dans le système
* se mettent à jour comme les autres applications

[EDIT 2016 : Mozilla a mis fin à ce programme, il n'est plus possible d'installer sur Android des applications FirefoxOS avec Firefox pour Android. Mais les applications Firefox OS qui sont des réelles appli web restent utilisables sur Android (c'est le cas d'OpenBeerMap)]

Une fois installées, il est même parfois difficile de les différencier des autres. Ici, OpenBeerMap, installée sur un Android depuis le marché d'application de Firefox :
![capture 1 de l'intégration d'OpenBeerMap]({attach}images/20141030_takebackcontrol/2014-08-21_12.03.01.png)
![capture 2 de l'intégration d'OpenBeerMap]({attach}images/20141030_takebackcontrol/2014-08-21_12.07.21.png)
![capture 3 de l'intégration d'OpenBeerMap]({attach}images/20141030_takebackcontrol/2014-08-21_12.05.56.png)

Un point important à noter : ces applications peuvent fonctionner hors ligne (si elles sont bien foutues. Pas OpenBeerMap, donc). Ce sont les technologies du web, mais ça ne veut pas forcément dire qu'un accès au web est nécessaire à tout moment.<br>
Bon ok c'est cool me diriez-vous, mais une application, en général, ça rend un service un peu plus avancé qu'un site web. Effectivement, mais Mozilla a aussi une réponse pour ça : des API d'accès au matériel sont en développement et en cours de standardisation.<br>
Elles permettent donc à des applications web d'accéder à l'appareil photo ou aux contacts, d'afficher des notifications ou de faire vibrer le téléphone.

L'implémentation effective de ces APIs est encore au stade expérimental mais il y a déjà des choses sympa qui fonctionnent et on a déjà des services efficaces proposés ainsi.<br>
Les applications sont téléchargeables sur le marché d'application de Firefox OS, le système d'exploitation basé sur les technologies du web que Mozilla a lancé il y a quelques années et qui a débarqué en France depuis quelques mois.

Par exemple, [l'application de prise de notes](https://marketplace.firefox.com/app/litewrite) de mon téléphone est une application Firefox pour Android<br>
Elle fonctionne parfaitement hors ligne et sauvegarde en local les notes que je prends.<br>
Elle permet également un stockage dans le cloud, pour permettre d'utiliser l'application depuis plusieurs terminaux.<br>
Sans mentir, c'est sans doute une des meilleures appli de prise de note que j'ai testées sous Android.


C'est aussi sur le marché d'application de Firefox OS que j'ai trouvé l'application de météo que j'utilise au quotidien : [l'appli F&C](https://marketplace.firefox.com/app/fc)<br>
Avec un design simplifié au max mais néanmoins convaincant et terriblement efficace, elle permet d'avoir une tendance sur la météo. Et elle pèse environ 350 Ko (dont la moitié occupée par des données, telles que les endroits où j'ai voulu connaitre la météo et que j'ai sauvegardés).

![capture de F&C]({attach}images/20141030_takebackcontrol/111562.png)
![autre capture de F&C]({attach}images/20141030_takebackcontrol/111559.png)

Ces applications battent des records de poids. Mais pour le moment, elles ne répondent pas à ma première problématique et il est aujourd'hui difficile de savoir si elles sont utilisées pour collecter des données sur leurs utilisateurs.

Espérons qu'une solution adressant ces deux problématiques verra le jour prochainement.
