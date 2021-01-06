---
title: Programmation en Python avec turtle
---

# Le module `turtle`

Le module python `turtle` permet de dessiner des formes
en faisant bouger une flèche (historiquement c'était une tortue).

Ça va nous permettre de voir les bases de la programmation en Python.

1. Ouvrez l'**éditeur Mu** en mode Python3 (c'est le mode de base).
2. Créez un nouveau fichier avec le bouton *Nouveau* et enregistrez-le.
3. Écrivez `from turtle import *` sur la première ligne pour charger la bibliothèque
4. Lancez votre script (bouton *Lancer*)

Il ne se passe rien sauf qu'une fenêtre devrait s'ouvrir en base de l'écran avec les caractères `>>> `.
C'est la **console Python**, c'est là que sont affichés les messages (par exemples les messages d'erreur),
mais on peut aussi y écrire du code python qui sera exécuté directement sans être enregistré dans le programme.

5. Écrivez `forward(100)` dans la consle et appuyez sur *Entrée*.

Une fenêtre devrait s'ouvrir avec une flèche qui dessine un trait.
En fait on a fait avancer la tortue (`forward` = *en avant* en anglais)
d'une distance de 100 pixels, et elle dessine son chemin.

Voici quelques fonctions de base pour manipuler la tortue :

~~~python
forward(distance)  # faire avancer la tortue

backward(distance) # faire reculer la tortue

right(angle) # faire se tourner la tortue vers sa droite

left(angle)  # faire se tourner la tortue vers sa gauche

# ces angles sont donnés en degrés
~~~

6. Essayez ces fonctions dans la console (en mettant des nombres à la place de `distance` et `angle`).

# Séquence d'instructions

On veut faire dessiner des formes géométriques simples à la tortue, voici un programme qui dessine un triangle équilatéral :

~~~python
from turtle import *

forward(100)
left(120)
forward(100)
left(120)
forward(100)
~~~

1. Modifiez le code pour dessiner un carré.
2. modifiez le code pour dessiner une maison (un carré avec un triangle dessus).

# Variables

Une variable est une boîte qui a un nom et qui contient une valeur (un nombre, du texte, etc.).
Par exemple dans ce code :

~~~python
truc = 42
~~~

On crée une variable qui s'appelle `truc` (c'est son *nom*) et qui contient `42` (c'est sa *valeur*).

On peut ensuite écrire le nom de la variable dans le code et il sera remplacé par la valeur de la variable à l'exécution.

Exemple :

~~~python
from turtle import *

taille = 100

print(taille) # affiche le contenu de la variable dans la console

forward(taille) # la tortue va avancer de 100 pixels
~~~

1. Crééz une variable `taille` en lui donnant comme valeur 80
2. Modifiez le code qui dessine le carré ou celui qui dessine le triangle pour que chaque `forward(100)` soit remplacé par `forward(taille)`.
3. Lancez le programme, puis modifiez la valeur de la variable et relancez le programme

Ça devrait avoir dessiné la forme à des tailles différentes.

# Entrée de l'utilisateur

En plus d'envoyer des messages dans la console en utilisant `print()`, on peut demander à l'utilisateur de taper du texte dans la console pour le récupérer.

Pour cela on utilise la fonction `input()`, exemple :

~~~python
# On récupère une chaîne de caractères et on la met dans une variable 'nom'
nom = input("Écris ton nom : ")

# On affiche le contenu de cette variable dans la console
print("Bonjour", nom)
~~~

1. Testez ce code dans la console ou dans un nouveau programme.

La valeur de retour de `input()` (donc dans l'exemple le contenu de `nom`) est du texte.
Pour le transformer en nombre il faut ajouter un appel à `int()` de cette manière :

~~~python
nombre = int(input("Écris un nombre : "))
~~~

Maintenant le contenu de la variable sera un nombre, et la variable pourra être utilisée dans le code là où on a besoin d'un nombre.

2. Reprenez le code qui dessine une forme avec une variable `taille` :
   modifiez la ligne où vous créez la variable pour y mettre une valeur obtenue avec `int(input())` au lieu d'un nombre écrit directement dans le code.


# Instructions conditionnelles

On peut vouloir exécuter des lignes de code seulement dans certaines conditions, *si* une variable a la bonne valeur par exemple.
On utilise alors une structure **conditionnelle** (*si ... alors ... sinon ...*).

Exemple en python :

~~~python
nombre = int(input("Écris un nombre"))

# attention à bien mettre 2 signes '=' et un ':' à la fin
if nombre == 42:
   # ça ne sera exécuté que si le nombre est 42
   # le code est "décalé" à droite, on dit qu'il est "indenté"
   print("Ton nombre est 42")

print("Au revoir") # ce code est aligné à gauche, il est en dehors du 'if'
~~~

Exemple avec un *sinon* :

~~~python
prenom = input("Ton prénom : ")

if prenom == "Léo":
    print("tu as le meilleur prénom")
else:
    print("Tu as un prénom moyen ...")
~~~

On peut changer la couleur du trait de la tortue avec la fonction `color()`.

Par exemple :

~~~python
from turtle import *

color("red")

forward(100)
~~~

dessinera un trait rouge.

1. Dans le code dessinant une forme dont la tille est demandée à l'utilisateur, changez la couleur à rouge si la taille est supérieure (signe `>`) à 100.
2. Créez une variable `forme` où vous demanderez à l'utilisateur d'écrire du texte (donc avec `inpu()` mais sans `int()`). Si le texte est `"carre"` dessinez un carré, sinon dessinez un triangle.

# Boucles `for`

Les boucles `for` permettent de répetter une action ou une séquence d'actions un nombre précis de fois, exemple :

~~~python
# affiche 10 fois "lol" dans la console

for i in range(10):
    print("lol")
~~~

On remarque qu'on a encore une fois une ligne qui finit par ':', suivie d'un bloc de code indenté (une suite de lignes décalées à droite).

On peut s'en servir pour dessiner le carré plus efficacement :

~~~python
from turtle import *

for i in range(4):
    forward(100)
    left(90)
~~~

1. Utilisez une boucle for pour dessiner une étoile à 5 branches (l'angle est de 144°)
2. Dessinez une étoile à 36 branches (170°)
3. Dessinez une ligne de 10 carrés de 10 px de coté.
4. dessinez une grille de 10x10 carrés chacun de 10px de coté.

# Boucles `while`

Parfois on veut répéter une action, mais on ne sais pas encore combien de fois,
alors on ne peut pas utiliser de boucle `for`,
il faut vérifier à chaque répétition si on veut s'arrêter ou non :
c'est ce à quoi sert la boucle `while` (boucle *tant que*).

Exemple :

~~~python
nombre = int(input("choisis un nombre : "))

while nombre != 42: # '!=' veut dir 'est différent de'
    print("Mauvais nombre, essaye encore")
    
    # il faut maintenant changer la variable nombre,
    # sinon on ça recommence à l'infini !
    nombre = int(input("re-choisis un nombre : "))

# Si on est ici c'est qu'on a réussi à sortir de la boucle while
print("bravo, tu as choisi 42 !")
~~~

1. Dans le code où on demande la taille pour dessiner une forme, redemandez la taille tant qu'elle est inférieure à 10 (et affichez "taille trop petite"),
   puis seulement quand la taille est assez grande, dessinez la forme.

On peut faire un boucle qui ne se termine jamais et continue à l'infini en écrivant `while True:` (tant que *vrai*, et True sera toujours *vrai*).

On peut éffacer l'écran et remettre la tortue au départ avec `reset()`.

2. Écrivez un programme qui demande à l'utilisateur une forme (entre triangle et carré) et une taille et qui `reset()` l'écran et dessine cette forme.
   Une fois la forme dessinée, ça doit recommencer et directement redemander une forme.
   (indice : il faut mettre tout le code de demande à l'utilisateur, dessin, etc. dans une boucle `while True:`)

# Fonctions

Une fonction est un bloc de code qu'on met de coté pour l'utiliser plus tard.
Le moment ou on l'écrit et le met de coté s'appelle la *définition*, le moment où on l'utilise s'appelle *l'appel* de fontion.

On a appelé plein de fonctions depuis le début, par exemple `forward(100)` est un appel de fonction,
mais ces fonctions sont définies par d'autres personnes dans le module `turtle`.

Voyons comment définir nous même une fonction :

~~~python
from turtle import *

# On définit une fonction trait, elle n'est pas appellée pour l'instant
def trait():
    forward(100)
    backward(100) # pour revenir au début

# on appelle cette fonction, ça dessine un trait maintenant
trait()

# on peut l'appeler plusieurs fois :
for i in range(10):
    trait()
    left(36)
~~~

1. Mettez le code pour dessiner un carré dans une fonction `carre` et celui pour dessiner un triangle dans une fonction `triangle`,
   appelez ces fonction dans la boucle `while` ou lieu d'y mettre directement le code pour dessiner les formes.
