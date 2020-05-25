Title: Florilège de requêtes Overpass utiles pour les bus
Date: 2017-08-03 22:22
Author: nlehuby
Tags: #osm, #junglebus
Slug: overpass-bus

Le génial service [Overpass-turbo](https://overpass-turbo.eu/) permet depuis quelques temps de sauvegarder ses requêtes favorites via son compte OSM.

Voici la liste des requêtes que je me suis enregistrées, sur la thématique des bus :

**Arrêts à proximité**<br>
Liste des arrêts à 500 mètres d'une position (ici [48.86343,2.40997](http://www.openstreetmap.org/#map=18/48.86343/2.40997)) :
```
[out:csv(::"id", name, public_transport, "ref:FR:STIF", ::"user")];
//[out:json];
node
  (around:500,48.86343,2.40997)
  ["highway"="bus_stop"];
out;
```

**Arrêts à proximité, avec les parcours desservis**<br>
Liste des arrêts à 500 mètres d'une position, avec le détail des parcours qui passent à ces arrêts :
```
[out:json];
(
  node
    (around:500,48.86343,2.40997)
    ["highway"="bus_stop"];
)->.a;
rel(bn);
out body;
.a out body;
```

**Arrêts d'une zone, avec les parcours desservis**<br>
Liste des arrêts d'une zone géographique, avec comme précédemment, le détail des parcours qui passent à ces arrêts :
```
[out:json];
(
node
  ["highway"="bus_stop"]
  ({{bbox}})
)->.a;
rel(bn)["route"="bus"];
out center;
.a out body;
```

**Arrêts d'un parcours**<br>
Liste de tous les arrêts d'un parcours en particulier (défini par son id, ici 1083331)
```
[out:csv(::"id", name, public_transport, "ref:FR:STIF", ::"user")];
relation(1083331);node(r:"platform");out meta;
```

Si la ligne n'est pas en schéma v2, alors remplacer platform par stop :
```
[out:csv(::"id", name, public_transport, "ref:FR:STIF", ::"user")];
relation(1257174);node(r:"stop");out meta;
```

**Arrêts non desservis**<br>
Liste des arrêts qui ne sont desservis par aucune ligne de bus.
```
//[out:csv(::"id", name, public_transport)];
[out:json];
node({{bbox}})["highway"="bus_stop"]->.all;relation(bn.all)["route"="bus"];node(r);
( .all; - ._; );out skel;
```

**Arrêts sans nom**<br>
Liste des arrêts de bus sans nom d'une zone géographique :
```
[out:csv(::"id", public_transport, "ref:FR:STIF", ::"user")];
(
node
  ["highway"="bus_stop"][!"name"]
  ({{bbox}})
);
out body;
```

**Nombre d'arrêts sans nom d'un parcours**<br>
Liste des arrêts de bus d'un parcours qui n'ont pas de nom renseigné :
```
[out:csv(total)];
//[out:json];
relation(1083331);node(r:"platform")[!"name"];out count;
```
Comme précédemment, si la ligne respecte le schéma v1 et non le v2, alors il faudra remplacer platform par stop.

**Parcours d'une zone**<br>
Liste des parcours de bus dans une zone géographique :
```
[out:csv(::"id", name, network, operator, ::"user")];
(
  relation["route"="bus"]({{bbox}});
);
out meta;
```

**Parcours orphelins**<br>
Liste des parcours de bus qui n'ont pas de ligne de bus associée
```
[out:csv(::"id", name, network, operator, ::"user")];
rel({{bbox}})["route"="bus"]->.all;
rel["route_master"="bus"](br.all);
rel["route"="bus"](r);
( .all; - ._; );
out meta;
```

Avec ça, vous avez tout ce qu'il faut pour prendre soin des bus dans OSM ;)
