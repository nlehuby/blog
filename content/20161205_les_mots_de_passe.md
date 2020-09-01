Title: Mes mots de passe
Date: 2016-12-05 21:08
Author: nlehuby
Tags: #vie_numérique
Slug: mots-de-passe


J'ai toujours eu du mal avec les mots de passe. Les inventer, les mémoriser, les changer ... l'angoisse.<br>
Mais, au fil de mon évolution dans le monde <s>digital</s> numérique, je crois que j'ai finalement trouvé comment m'authentifier sans crise de nerf.

Au début, comme tout le monde, j'avais le même mot de passe partout. Nous l'appellerons d'ailleurs Passe-partout ;)<br>
Puis, assez rapidement et heureusement pour moi, les sites ont commencé à le refuser, car Passe-Partout était trop court et tout pourri.<br>
J'ai donc commencé à mettre des mots de passe plus élaborés, mais évidemment, pas moyen de m'en souvenir...<br>
C'est ainsi, plus ou moins malgré moi, que je suis passé à une stratégie "sans mot de passe", ou passwordless. <br> C'est-à-dire que je ne m'embarrasse pas de mot de passe : à la création, j'en génère un, de préférence bien compliqué à 12 caractères, je le copie bêtement partout où on me le demande, puis, je l'oublie instantanément.<br>
À la prochaine connexion, je n'essaye même pas de me souvenir du mot de passe, je clique direct sur "J'ai oublié mon mot de passe". <br>
Puis je clique bien sagement sur le lien reçu par mail, pour recréer un mot de passe aléatoire que j'oublie aussitôt, puis faire ce que j'ai à faire sur le site.

Au début, c'était involontaire : j'essayais toutes les variantes possibles de Passe-Partout dans le champ, en ajoutant de la ponctuation, des majuscules, etc puis de rage je finissais pas me résigner à changer de mot de passe.<br>
Mais maintenant c'est complètement assumé, et croyez-le ou non, j'ai gagné un certain temps en authentification, et également pas mal en tranquilité d'esprit.<br>

De plus, ça me permet d'avoir un mot de passe différent sur chaque site, et de changer de mot de passe régulièrement. Deux conseils très répandus, mais qui sont un peu comme "Mangez 5 fruits et légumes par jour" et "Épargnez, et commencez quand vous êtes jeune" : on sait tous qu'il faut le faire, mais bon ... on verra demain hein !<br>

Bon bien sûr, il faut que le système qui veut nous authentifier soit potable : <br>
J'ai souvenir d'une époque où l'Assurance maladie gérait la réinitialisation de mot de passe par courrier ...<br>
Et des fois, la réinitialisation consiste parfois à me renvoyer un mail avec mon mot de passe. En clair dans un mail. <br>
Heureusement, j'ai l'impression que les choses ont quand même un peu progressé depuis.<br>
Tellement qu'il semblerait que je ne sois pas la seule à avoir cette idée, et que certains proposent même de [concevoir son système d'authentification sur cette solution](https://medium.com/@ninjudd/lets-boycott-passwords-680d97eddb01).

Mais bon, soyons honnêtes, la stratégie passwordless fonctionne bien quand on n'est pas pressé et qu'on a sa boîte mail sous la main.<br>
Pour gérer ses factures trois fois par an, ou utiliser un site de e-commerce à Noël, c'est pas mal, mais ce n'est très adapté pour le quotidien.<br>

En complément de ma stratégie "sans mot de passe", j'ai donc développé une deuxième stratégie que j'appelle "sans mémoire".<br>
Cela consiste à générer un mot de passe pour le site où je veux m'authentifier, à partir d'une technique reproductible.<br>
L'idée étant que, à la prochaine connexion, je puisse re-générer très exactement le même mot de passe, en appliquant la technique, sans jamais avoir eu à retenir ou stocker ce mot de passe en question.<br>
![c'est magique]({attach}images/20161205_mots_de_passe/mgc.gif)

Au début, je le faisais à la main, et je concaténais le nom du service avec le bon vieux Passe-Partout.<br>
Maitenant, j'utilise un service web qui reprend ce concept, avec une technique un peu plus sure que la concaténation, bien sûr ;) [SuperGenPass](https://chriszarate.github.io/supergenpass/).

Cette stratégie est plutôt efficace pour les sites du quotidien car ça n'alourdit pas trop le processus d'authentification et ça fonctionne très bien sur toutes les plateformes, y compris le mobile, y compris si c'est un Firefox OS, y compris si ce n'est pas ton mobile !

En revanche, dès que le site impose de changer de mot de passe de temps en temps, c'est le drame.<br>
On peut bien sûr ruser et ajouter des caractères manuellement à la fin du mot de passe généré par SuperGenPass, mais bon, c'est un coup à oublier, et quitte à retenir qu'on doit ajouter ";12!" à la fin, autant retenir [correct_horse_battery_staple](https://xkcd.com/936/).

D'où la troisième stratégie : la base Keepass, qui est basiquement un gros post-it <s>crypté</s>  chiffré.<br>
En effet, Keepass est une solution libre de gestion de mot de passe : les mot de passes sont stockés dans une base chiffrée avec une phrase de passe (un gros mot de passe bien long). Il suffit donc de retenir uniquement cette <s>passe de phrase</s> phrase de passe pour accéder à tous les mots de passe des services où l'on souhaite s'authentifier.<br>
Bon on peut prendre Passe-Partout encore une fois mais s'il est vraiment court et pourri, ça revient un peu à installer une porte blindée mais à toujours laisser la clef sous le paillasson ;)

Et on peut même sauvegarder le login par la même occasion, des fois que ça soit l'id de notre compte dans la base de données du système...<br>
Par contre, comme pour un post-it, il faut l'avoir toujours sur soi, donc avoir des moyens de mettre à disposition de ses différents terminaux la base Keepass par une solution de synchronisation ou de partage quelconque, ce qui ajoute un peu de complexité et des potentiels risques de sécurité.

Plus précisément, j'utilise une base Keepass (kdbx) hébergée que je consulte avec [Keeweb](https://keeweb.info/), une interface web de gestion de mot de passe compatible avec le format Keepass.<br>
L'intérêt étant d'avoir quelque chose qui tourne aussi sur mobile y compris si c'est un Firefox OS. Et ça permet d'avoir une interface jolie et ergonomique, parce que c'est pas parce que j'ai envie d'utiliser des logiciels libres que je suis obligée d'utiliser que des trucs moches.

Au final, je jongle un peu entre les statégies, mais je m'en sors pas si mal.<br>
Bon, là par exemple, je viens d'essayer de me connecter sur un site en statégie "sans mot de passe", mais le changement de mot de passe, que j'ai voulu faire avec la stratégie "sans mémoire", n'a pas fonctionnée car ... c'était déjà mon précédent mot de passe. Et à tous les coups, si je cherche dans Keeweb je vais trouver que le mot de passe SuperGenPass y est déjà consigné :p
