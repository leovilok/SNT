# Technique (séance 1)

# présentation

* à l'aide des illustrations
* en comparant avec le modèle client-serveur

# Activités :

On prend un cas simple d'un serveur et 3 clients tous interconnectés directement :

1. Est-ce qu'il y a plus ou moins de données transférées (exemple sur un réseau simple avec 1 serveur et 3 clients interconnectés)
   -> même nombre de données, mais moins devant le serveur (plus réparties sur le réseau)

2. combien de temps ça prend pour :
  - 3 Go à transférer à 3 nœuds avec une connexion illimitée -> 1sec en mode client serveur, 2sec en mode P2P
  - idem mais avec 3 Go/s max en sortie du serveur de départ -> 3sec en mode client serveur, 2sec en mode P2P

## Avantages / inconvénients :

(à discuter en groupe à la lumière de l'activité précédente)

### avantages p2p :
-  on peut partager un fichier sans avoir de grosse connexion
-  les données sont répliquées, donc le serveur principal peut mourrir, s'éteindre, ...

### inconvénients
- il faut connaître les adresses IP de tout le monde (résolu techniquement)
- plus de lent qu'un serveur central très bien connecté
- il faut que des gens laissent leur ordi allumé, ne supprimment pas tout de suite le fichier

# Usage (séance 2)

## Diffusion de la vidéo "Le piratage c'est du vol", diffusée dans les DVD et au cinéma

Questions aux élèves / débat (classe entière) :

* Qui a produit / fait mettre cette vidéo dans les films ?
* Qu'est ce que vous pensez du slogan ("Le piratage c'est du vol") ?  Est-ce que télécharger un film est légal ?

## Critères légaux pour interdire / autoriser de partager une œuvre

Qu'est-ce qui peut interdire le partage :
* Copyright / droit d'auteur (jusqu'à 70 ans après la mort de l'auteur)
* censure : contenus interdits (appels à la violence, nazisme, terrorisme, pedopornographie, ...)
* droit à l'image / données personnelles

Qu'est-ce qui peut autoriser le partage :
* autorisation de l'auteur
* autorisation de la personne filmé/photographiée (et des parents pour un mineur)
* licence libre (Creative Commons, logiciels libres, ...)

## Quels usages de P2P (plus généralement du partage de fichiers) sont légaux

En groupes, dire si les activités suivantes sont légales, illégales, si ça dépend, et pourquoi.

Liste :

* réseau utilisé par les cinémas pour recevoir les films qu'ils diffusent
* logiciel d'installation de Windows
* plateforme "Peertube" : site de partage de vidéo à la youtube (e.g. lycee connecté)
* "torrent" (partage de fichiers, publique) pour partager :
  * photos de vacances
  * votre dernière "œuvre" faite sous Paint
  * une chanson de Michael Jackson
  * une vidéo de vous qui reprennez une chanson de Michael Jackson (ou un artiste vivant ?)
  * un roman de Victor Hugo
  * un film que vous avez acheté en DVD
  * une vidéo que vous avez récupéré sur youtube
  * un article Wikipédia, ou une image trouvée sur cet article
  * le logiciel "Firefox"
  * le jeu "Rocket League"
  * le bulletin du premier trimestre d'un élève
