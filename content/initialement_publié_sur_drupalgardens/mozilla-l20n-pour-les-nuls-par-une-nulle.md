Title: Mozilla l20n pour les nuls (par une nulle)
Date: 2014-06-12 20:14
Author: nlehuby
Tags: #hack
Slug: mozilla-l20n-pour-les-nuls-par-une-nulle

Comme je me suis lancée récemment dans l'internationalisation (je l'ai
écrit une fois, maintenant, ça sera i18n et puis c'est tout) de mon
petit site [**OpenBeerMap**](http://openbeermap.github.io/), et comme
c'est ma première expérience en tant que développeur sur ce sujet et que
j'ai vraiment galéré, je vous propose un article à mi-parcours entre le
tutoriel et le retour d'expérience sur l'utilisation de l20n en
javascript.

</p>

Comment j'ai pas tout bien compris, si vous avez des retours et repérez
des erreurs, n'hésitez pas à me le signaler ;)

</p>

**Commençons par les basiques : c'est quoi ?**

</p>

L'i18n, c'est tout simplement avoir du texte adapté à la langue de la
personne qui utilise le site ou le appli. Mais ce n'est pas tout, c'est
aussi respecter les conventions propres à un pays (voire une région) par
exemple le format de date.

</p>

Il existe des bibliothèques dans un peu tous les langages de
programmation pour réaliser ceci. Mon site étant en html et javascript,
j'ai opté pour une bibliothèque js.

</p>

Bon, j'ai pas choisi la plus facile mais j'avais envie d'expérimenter la
solution Mozilla : [l20n](http://l20n.org/).

</p>

En particulier, le format des fichiers de traduction permet de gérer des
tas de choses qui doivent donner bien mal à la tête en temps normal,
comme par exemple les langues avec des déclinaisons (l'allemand, le
polonais, etc), les pluriels (qui s'expriment potentiellement
différemment dans les différentes langues), etc. Mais ... je ne vous
parlerai pas de ça dans cet article : la documentation sur le super
format de fichiers de traduction est abondante et facile à trouver. Je
vais "seulement" vous montrer comment commencer l'i18n d'un site et
arriver au moment où vous écrivez ces fichiers de traduction au format
si merveilleux.

</p>

**Comment ça fonctionne ?**

</p>

Un peu de théorie avant de partir tête baissée !

</p>

L'idée de base, c'est que l20n recherche tous les éléments textuels
qu'on a identifié comme à traduire, puis les remplace par leur valeur
dans la langue que *le navigateur web lui demande d'utiliser*, ou par
une valeur dans la langue par défaut (ou par une clef de traduction si
la valeur n'a pas été renseignée nulle part).

</p>

Bon, j'avoue que sur la partie en italique : c'est une approximation ...
Il y a moyen de raffiner énormément avec l'API de l20n mais 1) j'ai rien
compris et 2) pour commencer, la langue du navigateur, c'est déjà pas
mal et ça couvre l'essentiel des besoins.

</p>

En bref, l20n repasse sur toute la page HTML une fois qu'elle est
affichée entièrement et remplace le texte par les traductions donc

</p>

-   le texte écrit dans le HTML ne sert à rien : on peut mettre lorem
    ipsum à la place, ça marche tout aussi  bien
-   si le traducteur d'une langue qu'on ne maitrise pas veut nous faire
    un coup bas, il ya surement moyen d'injecter du code malicieux dans
    les traductions et de le voir interprété par l20n ... mais bon, il
    parait qu'ils ont pris leur précaution, ça doit être mon côté parano
    ...
-   si y a des bouts de HTML qui sont ajoutés dynamiquement par du
    javascript, ben ... ça va pas être évident, il faudra demander
    spécifiquement la traduction à la l20n au moment où on ajoute ce
    texte dynamique !

</p>

**Allons-y !**

</p>

Prenons donc notre super site en HTML et javascript, et introduisons un
peu de l20n dedans !

</p>

<u>Première étape : ajouter l20n.js à la liste des scripts à
exécuter</u>

</p>
~~~~ {.line}
  <script src="l20n.js"></script>
~~~~
</p>

<u>Étape 1 bis : trouver une version de l20n.js qui fonctionne</u>

</p>

ça a l'air de rien, mais j'ai déjà commencé à galérer à cette étape.

</p>

La [doc](https://github.com/l20n/l20n.js/blob/master/docs/html.md)
indique que la dernière version à jour se trouve
[ici.](https://github.com/l20n/builds/blob/master/l20n.js)

</p>

Perso, je n'ai pas trouvé cette version super fonctionnelle et j'ai opté
pour [la version proposée en téléchargement sur le site
officiel](https://raw.githubusercontent.com/l20n/builds/master/l20n.min.js). 

</p>

<u>Étape 2 : configurer l20n avec le manifeste</u>

</p>

Le manifeste permet d'indiquer quelles langues sont supportées et quelle
est la langue par défaut.

</p>

Le remplissage de ce fichier est assez trivial.

</p>
![image : c'est trivial]({attach}img/media_crop/156/public/201406/empty1.png)


</p>
</p>

Une fois le manifeste rempli, il faut indiquer où le trouver dans le html.
~~~~ {.line}
  <script type="application/l10n-data+json">
~~~~


J'avoue avoir sauté cette étape et utilisé la version proposée dans le
dépot github, dans un premier temps.

</p>

 

</p>

<u>Étape 3 : marquer les chaines à traduire</u>

</p>

Les chaines à traduire sont identifiées en ajoutant un attribut aux
balises HTML.

</p>

Par exemple, si j'ai le texte suivant et que je veux le traduire :

</p>
~~~~ {.line}
    <h1>Bonjour bonjour !</h1>
~~~~
</p>

je le transforme en :
~~~~ {.line}
        <h1 data-l10n-id="code_hello">Bonjour bonjour !</h1>
~~~~


Là, si vous enregistrez et retournez sur votre site, il ne plus bonjour
mais "code\_hello". C'est normal, don't panic !

</p>

 

</p>

<u>Étape 4 : traduire !</u>

</p>

En effet, il faut maintenant créer les traductions associées aux
éléments identifiés dans le HTML, à l'aide du fameux format de fichier
trop bien qui gère tout un tas de trucs.

</p>

C'est là que vous pouvez retourner sur la documentation de l20n et
trouver votre bonheur !

</p>

il faut donc créer un fichier pour chaque langue définie dans le
manifeste, à l'endroit défini par le manifeste

</p>

locales  
├── ast.l20n  
├── en.l20n  
├── es.l20n  
├── fr.l20n  
└── manifest.json

</p>

Et dans ce fichier, on peut écrire les chaines à utiliser comme
traduction :

</p>
~~~~ {.line}
      <code_hello "Hello !">
~~~~


 

</p>

Voilà, y a plus qu'à reproduire les étapes 3 et 4 à l'infini !

</p>

[Bon, ça ne fonctionne pas super bien avec le navigateur
Chromium](https://bugzilla.mozilla.org/show_bug.cgi?id=1026746) ... Mais
sous Firefox, c'est impec.

</p>

**Encore quelques petites remarques :**

</p>

<u>Comment tester ?</u>

</p>

l20n se fonde sur la langue du navigateur pour choisir la langue parmi
celles du manifeste. S'il ne la trouve pas dans son manifeste, il prend
la langue par défaut du manifeste.

</p>

Pour changer la langue du navigateur : dans Firefox, c'est dans *Outils
\> Options* ou *Édition \> Préférences*, onglet *Contenu*.

</p>

Il faut bien sûr recharger la page pour que ça prenne effet.

</p>

<u>Subtilités (simples) du format génial :</u>

</p>

Si vous avez du texte un peu long : il est possible d'avoir la
traduction sur plusieurs lignes

</p>

</p>
~~~~ {.line}
      <about_long_contenu """ Voilà un texte très très long !
                              Tellement long qu'il tient sur plusieurs
                              lignes """>

~~~~
 

</p>

Vous remarquerez peut-être qu'il n'est pas possible de mettre des
balises HTML dans le fichier de traduction :(

</p>

Pour gérer le cas où on veut traduire tout un paragraphe qui contient
des liens, voici comment procéder

</p>
~~~~ {.line}
    <div data-l10n-id="credits_contenu">
    Carte fournie par <a href="http://www.openstreetmap.org" target="_blank">OpenStreetMap</a>
    </div>

~~~~

puis

</p>
~~~~ {.line}
    <credits "Carte fournie par <a>OpenStreetMap</a>">

~~~~

pas très intuitif, mais tout à fait efficace.

</p>

 

</p>

Pour le reste, je vous invite à jeter un oeil [à cette
adresse](http://l20n.org/learn/).
