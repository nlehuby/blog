Title: Migration du blog
Date: 2016-06-13 10:16
Author: nlehuby
Tags: #hack
Slug: migration-du-blog-pelican



Après quelques années de bons et loyaux services, mon hébergeur [DrupalGardens](http://drupalgardens.com) jette l'éponge. C'est pour moi l'occasion de déménager mon blog vers [5apps](https://5apps.com), et j'en profite au passage pour le migrer de [Drupal](https://www.drupal.org/) vers [Pelican](http://docs.getpelican.com).

Drupal c'est cool. Je suis tombée dedans il y a longtemps, alors que j'étais encore en école d'ingé, et j'ai même eu l'occasion de m'impliquer dans la [communauté francophone de Drupal](http://drupalfr.org/) pendant quelques années.

Mais faire mon blog avec Drupal, c'est un peu comme louer une cuisine professionnelle pour se faire un oeuf sur le plat : ça marche, mais pour le [KISS](https://fr.wikipedia.org/wiki/Principe_KISS), on repassera.

Donc j'ai décidé de passer à un site statique.

Pelican, c'est assez fun à utiliser : on écrit ses articles en rst ou en markdown, puis pélican compile / transforme tout ça en pages html, qu'on peut héberger très simplement puisque c'est juste du html tout con.

Un peu comme [Sphinx](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation)), mais pour un blog.

Quelques détails sur la migration :

J'ai commencé par installer Pelican. Ça s'installe en local (voir à ce propos le [très bon article de SpF sur ce sujet](https://sanspseudofix.fr/migration-de-worpdress-a-Pelican.md/)) et c'est sans difficicultés particulières.

Ensuite, j'ai migré le contenu existant en utilisant l'import par flux RSS.

C'est loin d'être parfait : j'ai dû repasser sur tous les articles pour virer les balises html en trop dans le fichier md généré... C'est là que je suis bien contente de n'avoir que 24 articles publiés !

Mais ça m'a permis d'avoir une nouvelle instance de blog qui tourne en quelques heures, avec tous mes anciens contenus.

Bon, ce n'est qu'une façade, car tous les liens pointent encore sur l'ancien site, ainsi que les images, mais bon si les migrations entre services étaient si faciles, ça se saurait ;)

Pour l'hébergement, J'ai choisi 5apps.com, car je l'utilise déjà pour héberger mes petites appli en html (dont [Horaires-Bus](https://horaires-bus.5apps.com/liste.html), mon appli pour consulter les horaires des bus même quand y a plus de réseau) et j'en suis très satisfaite.

C'est aussi simple à utiliser qu'un hébergement web chez github (on fait git push pour déployer), mais avec des services sympa en plus (notamment la génération automatique d'AppCache. Si vous utilisez cette techno et que je vous le faites à la mano, je pense que vous voyez pourquoi c'est cool :p)

Bref, je vais m'arrêter là, parce que j'ai toujours trouvé ça très méta les gens qui tiennent un blog pour ... parler de leur blog.

Tout ça pour dire que la nouvelle adresse de ce blog est <https://nlehuby.5apps.com> (ou <https://nlehuby.5apps.com/feeds/all.atom.xml> pour les lecteurs de flux)
