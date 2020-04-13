---
title : Préparation à l'oral du Bac
author : Terminale ISN Lycée du Parc
numbersections: true
fontsize: 11pt
geometry:
- top=20mm
- left=20mm
- right=20mm
- heightrounded    
--- 

# Crédits 

Plusieurs exercices sont tirés des questions proposées sur le site [https://genumsi.inria.fr/](https://genumsi.inria.fr/).

# Programmation en Python


:::exercice

_Auteur : Aude Durand Senter, question n°178 Genumsi_

On a saisi le code suivant :

~~~python
def mystere(nombre) :
    while nombre > 5 :
        nombre = nombre - 5
return nombre
~~~

Quelle affirmation est vraie dans celles proposées ci-dessous ?

Réponses :

1. On sort de la boucle while dès que `nombre > 5`
1. On sort de la boucle while dès que `nombre < 5`
3. On sort de la boucle while dès que `nombre <= 5`
4. On continue la boucle tant que `nombre <= 5`
:::


:::exercice

_Auteur : Nicolas Revéret_

On considère le programme ci-dessous : 

~~~python
a = 8
b = 5
a = a + b
b = a - b
a = a - b
~~~

Quelles sont les valeurs des variables  `a` et `b` à la fin du programme ?
:::

:::exercice

_Auteur : Nicolas Revéret_

On souhaite que l'utilisateur saisisse une valeur entière comprise entre 1 et 20 (inclus).

Quel code est correct ?

Réponses :

1. Réponse 1

~~~python
a = int ( input("Saisir un nombre entre 1 et 20") )
while (a < 1 and a > 20) :
      a = int ( input("Saisir un nombre entre 1 et 20") )
~~~

2. Réponse 2

~~~python
while (a < 1 and a > 20) :
    a = int ( input("Saisir un nombre entre 1 et 20") )
~~~

3. Réponse 3

~~~python
a = int ( input("Saisir un nombre entre 1 et 20") )
while (a < 1 or a > 20) :
    a = int ( input("Saisir un nombre entre 1 et 20") )
~~~

4. Réponse 4

~~~python
a = int ( input("Saisir un nombre entre 1 et 20") )
while (a >= 1 and a >= 20) :
    a = int ( input("Saisir un nombre entre 1 et 20") )
~~~

:::

:::exercice

_Auteur : Nicolas Revéret_

On a saisi le code suivant :

~~~python
a = 12
for i in range(3) :
  a = a * 2
  a = a - 10
~~~

Quelle est la valeur de la variable `a` après l'exécution du code ?
:::


:::exercice
Pour les questions suivantes, il faut utiliser obligatoirement deux boucles imbriquées et au maximum deux fois la fonction `print`.

1. Ecrire un script Python qui produit l'affichage 1 ci-dessous.
2. Ecrire un script Python qui produit l'affichage 2 ci-dessous.

__Affichage 1__
```python
0
01
012
0123
01234
```

__Affichage 2__
```python
01234
12345
23456
34567
45678
```
:::


:::exercice
Pour le diplôme du baccalauréat, si on note $m$ la moyenne du candidat, quatre mentions sont possibles :
_Passable_ si $10 \leqslant m <  12$, _Assez bien_ si $12 \leqslant m < 14$, _Bien_ si $14 \leqslant  m < 16$ et _Très bien_ sinon.
Recopier et compléter le script Python ci-dessous pour qu’il affiche la mention d’un candidat admis (on suppose sa moyenne supérieure ou égale à 10).

~~~python
m = float(input('Moyenne du candidat ? '))
if 10 <= m < 12:
    print("Passable")
#to be completed
~~~
:::


:::exercice 

_Auteur : Nicolas Revéret_

On considère le code suivant :

~~~python
def f(tab):
  for i in range(len(tab)//2):
    tab[i],tab[-i-1] = tab[-i-1],tab[i]
~~~

Après les lignes suivantes :

~~~python
tab = [2,3,4,5,7,8]
f(tab)
~~~

Quelle est la valeur de la variable `tab` ?

Réponses :

1. `[2,3,4,5,7,8]`
2. `[5,7,8,2,3,4]`
3. `[8,7,5,4,3,2]`
4. `[4,3,2,8,7,5]`
:::


:::exercice

_Auteur : Christophe Beasse_

Que contient la variable `a` si on exécute ce script ?

~~~python
def carre(val):
  return val*val

def inc(val):
  return val + 1

a = carre(inc(3.0))
~~~

1. 9.0
1. 12.0
3. 10.0
4. 16.0
:::

:::exercice

_Auteur : Christophe Beasse_

Soit la liste suivante : `liste_pays = ["France","Allemagne","Italie","Belgique"]`

Que renvoie : `liste_pays[2]` ?

Réponses :

1. `"France"`
1. `"Allemagne"`
3. `"Italie"`
4. `"Belgique"`

:::

:::exercice

_Auteur : Christophe Beasse_

 Quelle est le résultat de : `[ (a,b) for a in range(3) for b in range(a) ]` ?

Réponses :

1.  `[(1,0),(2,1),(2,1)]`
1.  `[(1,0),(2,1),(3,2)]`
3.  `[(1,0),(2,0),(2,1)]`
4.  `[(0,0),(1,1),(2,2)]`

:::

:::exercice
Ecrire une fonction `moyenne(t)` qui prend en argument un tableau de nombres t et qui retourne sa moyenne
arithmétique.
:::


:::exercice

_Auteur : Nicolas Revéret_

On dispose d'un tableau d'entiers, ordonné en ordre croissant.

On désire connaître le nombre de valeurs distinctes contenues dans ce tableau.

Quelle est la fonction qui ne convient pas ?

Réponses :

1. Réponse 1
~~~python
def compte(t):
    cpt = 1
    for i in range(1,len(t)):
        if t[i] != t[i-1]:
            cpt = cpt + 1
    return cpt
~~~

2. Réponse 2
~~~python
    def compte(t):
      cpt = 0
      for i in range(0,len(t)-1):
        cpt = cpt + int(t[i] != t[i+1])
      return cpt
~~~

3. Réponse 3
~~~python
    def compte(t):
      cpt = 0
      for i in range(0,len(t)-1):
        if t[i] != t[i+1]:
          cpt = cpt + 1
      return cpt+1
~~~
:::

:::exercice
_Auteur : Eric Rougier_

Quel est le résultat de l'évaluation de l'expression Python suivante ? 

`[2 ** n for n in range(4)]`

Réponses :

1. `[0, 2, 4, 6, 8]`
2. `[1, 2, 4, 8]`
3. `[0, 1, 4, 9]`
4. `[1, 2, 4, 8, 16]`
:::

:::exercice
_Auteur : Germain Becker, question n°326 Genumsi_
Quel est le tableau `t` construit par les instructions suivantes ?

~~~python
tab = [1, 2, -3, 7, 4, 10, -1, 0]
t = [e for e in tab if e >= 0]
~~~

Réponses :

1.   `t = [1, 2, 7, 4, 10, 0]`
2.   `t = [e, e, e, e, e, e]`
3.   `t = [1, 2, 7, 4, 10]`
4.   `t = [-3, -1, 0]`
:::

:::exercice
_Auteur : Germain Becker, question n°339 Genumsi_

On considère le tableau t suivant.

`t = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]`

Quelle est la valeur de t[1][2] ?

Réponses :

1. 1
2. 3
3. 4
4. 2



:::

:::exercice
_Auteur : Eric Rougier, question n°150 Genumsi_

Quelle est la valeur de la variable image après exécution du script Python suivant ?

~~~python
image = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(4):
    for j in range(4):
        if (i+j) == 3:
            image[i][j] = 1
~~~

Réponses :

1.   `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]`

2.   `[[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]`

3.   `[[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]`

4.  `[[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]`

:::


:::exercice
_Auteur : Nicolas Réveret, question n°379 Genumsi_

On a saisi le code suivant :

~~~python
liste = [0, 1, 2, 3]
compteur = 0
for i in range(len(liste)-1) :
    for j in range(i,len(liste)) :
        compteur += 1
~~~

Que contient la variable compteur à la fin de l’exécution de ce script ? 
:::

:::exercice

Quelle est la valeur référencée par la liste L après exécution du programme ci-dessous ?

~~~python
L = [731, 732, 734]
L[0], L[1] = L[1], L[0]
M = L
M[1] = 732
~~~

1. [732, 731, 734]
2. [731, 732, 734]
3. [732, 732, 734]

:::

:::exercice

On considère l'extrait de code suivant :

~~~python
while (a < 20) or (b > 50):
    .......
    .......
~~~

Quelles conditions permettent de mettre fin à cette boucle ?



1. __Réponse 1 :__   la boucle prend fin lorsque `a < 20 ou b > 50`

2. __Réponse 2 :__ la boucle prend fin lorsque `a < 20 et b > 50`

3. __Réponse 3 :__  la boucle prend fin lorsque `a >= 20 ou b <= 50`

4. __Réponse 4 :__  la boucle prend fin lorsque `a >= 20 et b <= 50`
:::



:::exercice

On exécute le script suivant :

~~~python
L = [12,0,8,7,3,1,5,3,8]

a = [elt for elt in L if elt < 4]
~~~

Quelle est la valeur de a à la fin de son exécution ?

Réponses :


1. __Réponse 1 :__ `[12,0,8]`


2. __Réponse 2 :__  `[12,0,8,7]`


3. __Réponse 3 :__  `[0,3,1,3]`


4. __Réponse 4 :__  `[0,3,1]`


:::


:::exercice
On définit :  `L = [10,9,8,7,6,5,4,3,2,1]`.

Quelle est la valeur de  `L[L[3]]` ?

Réponses :


1. __Réponse 1 :__  3


2. __Réponse 2 :__   4 


3. __Réponse 3 :__ 7


4. __Réponse 4 :__  8
:::


:::exercice
On définit une grille G remplie de 0, sous la forme d\'une liste de
listes, où toutes les sous-listes ont le même nombre d\'éléments.

~~~python
G = [ [0, 0, 0, ..., 0],
[0, 0, 0, ..., 0],
[0, 0, 0, ..., 0],

......
[0, 0, 0, ..., 0]]
~~~

On appelle *hauteur* de la grille le nombre de sous-listes contenues
dans G et *largeur* de la grille le nombre d'éléments dans chacune de
ces sous-listes. Comment peut-on les obtenir ?

Réponses :

1. __Réponse 1:__
~~~python
hauteur = len(G[0])
largeur = len(G)
~~~

2.  __Réponse 2 :__
~~~python
hauteur = len(G)
largeur = len(G[0])
~~~

3.  __Réponse 3 :__
~~~python
hauteur = len(G[0])
largeur = len(G[1])
~~~

4. __Réponse 4 :__
~~~python
hauteur = len(G[1])
largeur = len(G[0])
~~~
:::


:::exercice

Quelle est la valeur de l'expression  `[[0] * 3 for i in range(2)]` ?

Réponses :

1. __Réponse 1 :__   `[[0,0], [0,0], [0,0]]`
2. __Réponse 2 :__   `[[0,0,0], [0,0,0]]`
3. __Réponse 3 :__   `[[0.000], [0.000]]`
4. __Réponse 4 :__   `[[0.00], [0.00], [0.00]]`
:::


:::exercice

On exécute le script suivant :

~~~python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
~~~

Que contient la variable `c` à la fin de cette exécution ?

Réponses :

1. __Réponse 1 :__  `[5,7,9]`

2. __Réponse 2 :__  `[1,4,2,5,3,6]`

3. __Réponse 3 :__  `[1,2,3,4,5,6]`

4. __Réponse 4 :__  `[1,2,3,5,7,9]`
:::


:::exercice
On exécute le script suivant :

~~~python
asso = []
L=[['marc','marie'],['marie','jean'],
    ['paul','marie'], ['marie','marie'],
    ['marc','anne']]
for c in L :
    if c[1]=='marie':
        asso.append(c[0])
~~~

Que vaut asso à la fin de l\'exécution ?

Réponses :

1. __Réponses 1:__ `['marc', 'jean', 'paul']`

2. __Réponses 2 :__  `[['marc','marie'], ['paul','marie'], ['marie','marie']]`

3. __Réponses 3 :__  `['marc', 'paul', 'marie']`

4. __Réponses 4 :__  `['marie', 'anne']`

:::


:::exercice
Quelle est la valeur de la variable n à la fin de l'exécution du script ci-dessous ?

~~~python
n = 1
while n != 20:
    n = n + 2
~~~

Réponses :

1. __Réponse 1:__  1

2. __Réponse 2:__  20

3. __Réponse 3:__ 22

4. __Réponse 4:__ le programme ne termine pas, la boucle tourne indéfiniment
:::


:::exercice

On définit en Python la fonction suivante :

~~~python
def f(L):
    S = []
    for i in range(len(L)-1):
        S.append(L[i] + L[i+1])
    return S
~~~


Quelle est la liste renvoyée par `f([1, 2, 3, 4, 5, 6])` ?


1. `[3, 5, 7, 9, 11, 13]`
2. `[1, 3, 5, 7, 9, 11]`
3. `[3, 5, 7, 9, 11]`
4. cet appel de fonction déclenche un message d'erreur
:::


# Représentation des nombres, des textes ou des images


:::exercice
Le codage en base deux de l’entier 26 en base dix est :

1. 11010
2. 10010
3. 11001
4. 110010

:::


:::exercice
Le résultat de la somme $\overline{101101}^{2} + \overline{101111}^{2}$ est :

1. $\overline{1100100}^{2}$
2. $\overline{1110101}^{2}$
3. $\overline{1011100}^{2}$
4. $\overline{1111100}^{2}$

:::

:::exercice
Le plus grand entier qu’on peut représenter en base deux sur 8 bits a pour écriture décimale :

1. 11111111
2. 10000000
3. 255
4. 256
:::


:::exercice
Quelle est l'écriture décimale de l'entier qui s'écrit 1010 en binaire ?

Réponses :

1.  5

2. 10

3. 20

4. 22
:::


:::exercice
Combien d'entiers positifs ou nuls (entiers non signés) peut-on représenter en machine sur 32 bits ?

Réponses :

1. $2^{32} - 1$
2. $2^{32}$
3. $2 \times 32$
4. $32^{2}$
:::


:::exercice

Combien de bits faut-il au minimum pour coder le nombre décimal 4085 ?

Réponses :

1. 4
2. 12
3. 2042
4. 2043
:::


:::exercice
Parmi les propositions suivantes, laquelle est la représentation binaire de 761 ?

Réponses :

1. 11 1100 1101
2. 11 1110 0101
3. 10 0111 1001
4. 10 1111 0001
:::


:::exercice
Le codage d'une couleur se fait à l'aide de trois nombres compris
chacun, en écriture décimale, entre 0 et 255 (code RVB).

La couleur « vert impérial » est codée, en écriture décimale, par (0,86, 27).

Le codage hexadécimal (base 16) correspondant est :

Réponses :

1. (0, 134, 39)
2. (0, 134, 1B)
3. (0, 56, 1B)
4. (0, 56, 39)
:::

:::exercice

Quelle est l'écriture binaire du nombre entier 183 ?

Réponses :

1. 0100 1000
2. 1110 1101
3. 1011 0111
4. 1001 0101
:::

:::exercice
Le codage en base seize de l'entier $256$ est :

1. $\overline{F1}^{16}$
2. $\overline{A1}^{16}$
3. $\overline{FA}^{16}$
4. $\overline{FF}^{16}$
:::

:::exercice

L'adresse MAC de la carte Wifi d'un smartphone  est \texttt{c8:60:00:a4:89:ab} avec six octets codés en base seize.

La transcription en base dix de cette adresse MAC est :

1. $200:96:0:164:137:171$
2. $20:6:0:14:17:21$
3. $96:0:0:40:72:110$
4. $140:6:0:74:152:186$
:::


:::exercice
La fonction ci-dessous doit retourner la liste des chiffres en base deux d'un entier
n par ordre décroissant des poids de gauche à droite.

~~~python
def nombre2chiffres(n):
    t = []
    while n >= 2:
        ..........
        n = n // 2
    ..............
    t.reverse()
    return t
~~~

Quelle instruction peut-on écrire en lignes 4 et 6 ?

1. `t.append(n)`
2. `t.append(n % 2)`
3. `t.append(n // 2)`
4. `t = t + [n % 2]`
:::



:::exercice
1. Représenter en binaire le nombre d’écriture décimale 49.
2. Représenter en base dix, le nombre dont l'écriture en base deux est $1010110$.
3. Déterminer le successeur en base deux des entiers :
   * $111$
   * $10011$
   * $10111$
4. Déterminer le nombre de caractères qu'on peut coder sur un octet.
:::

:::exercice
On souhaite convertir 25 de base 10 en base 2.
On obtient en binaire :

Réponses :

1.    11001
2.    10110
3.    10011
4.    11000
:::

:::exercice
Quelle est la valeur affichée par l'exécution du test suivant ?

~~~python
In [1]: 0.1 + 0.2 == 0.3              
                                                                                                                                                                         
Out[1]: False
~~~

Réponses :

1. `True`
2. `False`
3.  0.3
:::

:::exercice
Combien de bits sont nécessaires pour représenter 15 en binaire ?

Réponses :

1. 2
2. 3
3. 4
4. 5
:::


:::exercice
Quelle est la valeur affichée a l'exécution du programme Python suivant ?

~~~python
x = 1 
for i in range(11): 
    x = x * 2 
print(x)
~~~

Réponses :

1.  1024
2.  2048
3.  23
4.  $2^{2^{11}}$
:::


:::exercice
Quelle est la valeur affichée a l'exécution du programme Python suivant ?

~~~python
x = 2 
for i in range(10): 
    x = x ** 2 
print(x)
~~~

Réponses :

1.  1024
2.  2048
3.  $2^{2^{10}}$
4.  $2^{2^{11}}$
:::


:::exercice

1. Convertir 3970 en base 6.
2. Convertir en base dix l’entier naturel dont l'écriture en base six est 4321.
3. Écrire en Python une fonction `base6(L)` qui renvoie la valeur entière correspondant à la liste des chiffres de l'écriture en base 6.

Exemple : `base6([1, 3, 2])` doit renvoyer 56 car $1 \times 6^{2} + 3 \times 6 + 2 = 56$.
:::


:::exercice
1. Pour déterminer la liste des chiffres en base dix d'un entier naturel, un élève a écrit la fonction ci-dessous :
   
~~~python
def liste_chiffres(n):
    L = [n % 10]
    while n > 0:
        n = n // 10
        L.insert(0, n % 10)
    return L
~~~

Malheureusement sa fonction ne retourne pas le résultat attendu pour l'entier $730$ :

~~~python
>>> liste_chiffres(730)
[0, 7, 3, 0]
~~~

Proposer une version corrigée de la fonction `liste\_chiffres`.

2. Compléter la fonction `somme_chiffres_base2(n)` pour qu'elle  retourne la somme des chiffres en base deux de l'entier `n` passé en paramètre. 

~~~python
def somme_chiffres_base2(n):
    s = 0
    while n > 0:
        s = s + n % 2
        ..............
    return s
~~~

3. Déterminer une valeur possible de la variable \texttt{secret} telle que :

~~~python
>>> somme_chiffres(secret)
734
~~~

4. Écrire une fonction `maximum_chiffre(n)` qui retourne le plus grand chiffre de l'écriture en base dix de l'entier naturel  `n`  passé en paramètre. 
:::


:::exercice
Le nombre de chiffres en base $2$ d'un entier naturel $n$ est :

* $1$ si $n$ est égal à $0$ ;
* l'unique entier $p$ tel que $2^{p-1} \leqslant n < 2^{p}$ si $n$ supérieur à $0$.

Compléter la fonction ci-dessous pour qu'elle retourne le nombre de chiffres en base $2$ de l'entier \texttt{n} passé en paramètres. 

~~~python
def nbchiffres_base2(n):
	if n == 0:
		return 1
    nbchiffre = 1
    puissance = 1
    while ..............:
        .........................
        .........................
    return ......................
~~~
:::


# Logique booléenne et architecture


:::exercice
En 1945, John Von Neumann a décrit un modèle d’architecture qui est encore valable pour les ordinateurs
actuels. Quelles sont les entités de ce modèle et comment communiquent-elles ?
:::



:::exercice
Parmi les quatre expressions suivantes, laquelle s\'évalue en True ?

Réponses :

1. __Réponse 1 :__  `False and (True and False)`

2. __Réponse 2 :__   `False or (True and False)`

3. __Réponse 3 :__  `True and (True and False)`

4. __Réponse 4 :__   `True or (True and False)`
:::

:::exercice
Sachant que l'expression `not(a or b)` a la valeur True, quelles peuvent
être les valeurs des variables booléennes a et b ?

Réponses :

1. True et True
2. False et True
3. True et False
4. False et False
:::

:::exercice
A quelle expression logique correspond cette table de vérité ?

| A      | B    | f(A, B)    |
|:------:|------|------------|
| 0      | 0    |   1        |
| 0      | 1    |   1        |
| 1      | 0    |   1        |
| 1      | 1    |   0        |

:::

:::exercice
A quelle expression logique correspond cette table de vérité ?

| A      | B    | f(A, B)    |
|:------:|------|------------|
| 0      | 0    |   0        |
| 0      | 1    |   0        |
| 1      | 0    |   0        |
| 1      | 1    |   1        |

:::

:::exercice
A quelle expression logique correspond cette table de vérité ?

| A      | B    | f(A, B)    |
|:------:|------|------------|
| 0      | 0    |    0       |
| 0      | 1    |    1       |
| 1      | 0    |    1       |
| 1      | 1    |    1       |

:::



:::exercice
A quelle expression logique correspond cette table de vérité ?

| A      | B    | f(A, B)    |
|:------:|------|------------|
| 0      | 0    |     0      |
| 0      | 1    |     1      |
| 1      | 0    |     1      |
| 1      | 1    |     0      |

:::

:::exercice
Choisir une expression booléenne pour la variable S qui satisfait la
table de vérité suivante.

  A   B   S
  --- --- ---
  0   0   1
  0   1   0
  1   0   1
  1   1   1

Réponse :

1. A ou (non B)
2. (non A) ou B
3. (non A) ou (non B)
4. non (A ou B)
:::

# Algorithmique

:::exercice
T est un tableau de nombres entiers non vide. Que représente la valeur
de s renvoyée par cette fonction ?

~~~python
def mystere(T):
    s = 0
    for k in T:
        if k % 2 == 0:
            s = s+k
    return s
~~~

Réponses :

1. __Réponse 1 :__  la somme des valeurs du tableau T

2. __Réponse 2 :__  la somme des valeurs positives du tableau T

3. __Réponse 3 :__  la somme des valeurs impaires du tableau T

4. __Réponse 4 :__  la somme des valeurs paires du tableau T
:::


:::exercice

Soit $n$ un entier naturel. Sa factorielle est le produit des nombres
entiers strictement positifs qui sont plus petits ou égaux à $n$. Par
exemple la factorielle de 4 vaut $1 \times 2 \times 3 \times 4 = 24$.

Quelle est la fonction correcte parmi les suivantes ?

Réponses :

1. __Réponse 1 :__ 
~~~python
def factorielle(n):
    i = 0
    fact = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    return fact
~~~

2. __Réponse 2 :__ 
~~~python
def factorielle(n):
    i = 1
    fact = 1
    while i < n:
        fact = fact * i
        i = i + 1
    return fact
~~~

3. __Réponse 3 :__  
~~~python
def factorielle(n):
    i = 0
    fact = 1
    while i < n:
        i = i + 1
        fact = fact * i
    return fact
~~~

4. __Réponse 4 :__
~~~python
def factorielle(n):
    i = 0
    fact = 1
    while i <= n:
        i = i + 1
        fact = fact * i
    return fact
~~~
:::


:::exercice
Écrire une fonction `min2(a, b)` qui retourne le minimum de deux nombres passés en
paramètre, sans utiliser la fonction min du module builtins.
:::


:::exercice
En voulant programmer une fonction qui calcule la valeur minimale d'une liste d'entiers, on a écrit :

~~~python
def minimum(L):
    mini = 0
    for e in L:
        if e < mini:
            mini = e
    return mini
~~~

Cette fonction a été mal programmée. Pour quelle liste ne donnera-t-elle
pas le résultat attendu, c'est-à-dire son minimum ?

Réponses :

1. __Réponse 1 :__  `[-1,-8,12,2,23]`
2. __Réponse 2:__   `[0,18,12,2,3]`
3. __Réponse 3:__   `[-1,-1,12,12,23]`
4. __Réponse 4:__   `[1,8,12,2,23]`
:::


:::exercice
Écrire une fonction `min_liste(L)` qui retourne le minimum d’une liste de nombres passée
en paramètre.
:::

:::exercice
Quelle est la valeur de element à la fin de l'exécution du code suivant :

~~~python
L = [1,2,3,4,1,2,3,4,0,2]
element = L[0]
for k in L:
    if k > element:
        element = k
~~~

1. __Réponse 1 :__ 0
2. __Réponse 2:__  1
3. __Réponse 3:__  4
4. __Réponse 4:__  10
:::



:::exercice
Un élève a écrit la fonction ci-dessus pour déterminer si le premier paramètre n est dans la
liste L passée en second paramètre. Le professeur lui indique que son code comporte des erreurs.
Proposer une version corrigée de cette fonction.

~~~python
def element_dans_liste(n, L):
    for k in range(len(L)):
        if e == n:
            return True
        else:
            return False
~~~
:::

:::exercice

Pour chacune des listes ci-dessous, déterminer si l'algorithme le plus adapté pour qu'une
machine y recherche une valeur est l’algorithme de recherche séquentielle ou l’algorithme
de recherche dichotomique.

1. Liste A : `[4, 6, 15, 20, 21, 26, 31, 41, 42, 50, 69, 87, 88, 92, 97]`
2. Liste B : `[41, 97, 91, 59, 7, 45, 3, 96, 26, 32, 18, 11, 67, 74, 54]`
:::


:::exercice

Compléter le code de la fonction `recherche_dicho_dec(x, L)` qui prend en paramètres
un nombre `x` et une liste de nombres `L` triée dans l’ordre décroissant. Elle doit retourner
`True` si `x` appartient à L et False sinon.

~~~python
def recherche_dicho_dec(x, L):
    a, b = 0, len(L) - 1
    while a <= b:
        m = (a + b) // 2
        if L[m] > x:
            ..................
        elif L[m] < x:
            ................
        else:
            .................
    .........................
~~~


:::


:::exercice
_Auteur Sylvie Genre_

La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il remplacer les
points de suspension pour que la fonction soit correcte ?

~~~python
def moyenne(tableau):
    total = ...
    for valeur in tableau:
        total = total + valeur
    return total / ...
~~~

Réponses :

1. __Réponse 1 :__ 1 et `(len(tableau) + 1)`
2. __Réponse 2:__  0 et `(len(tableau) + 1)`
3. __Réponse 3:__  0 et `len(tableau)`
:::


:::exercice
On considère le code incomplet suivant qui recherche le maximum dans une liste.

~~~python
liste = [5,12,15,3,15,17,29,1]
iMax = 0
for i in range(1,len(liste)):
    .........
iMax = i
print (liste[iMax])
~~~

Par quoi faut-il remplacer la ligne pointillée ?

Réponses :

1. __Réponse 1 :__  `if i > iMax:`
2. __Réponse 2:__   `if liste[i] > liste[iMax]:`
3. __Réponse 3:__  `if liste[i] > iMax:`
4. __Réponse 4:__ `if i > liste[iMax]:`
:::

# Le Web

:::exercice
Le protocole qui permet à un client de faire une requête de page Web auprès d'un serveur Web s'appelle :

Réponses :

1. Internet Protocol
2. HTML
3. HTTP
4. TCP
5. WWW
:::


:::exercice
Si la page demandée n'est pas disponible, le serveur Web renvoie au client un code d'erreur : 

Réponses :

1. 404
   
2. 504
   
3. 403
   
4. 503
:::


:::exercice
L'inventeur du World Wide Web au CERN est   : 

Réponses :

1. Tim Berners-Lee
   
2. Ted Nelson
   
3. Louis Pouzin
   
4. Vinton Cerf
:::


:::exercice
Dans le fichier source d'une page Web, le code qui permet de créer un lien hypertexte vers la page [https://www.w3schools.com/](https://www.w3schools.com/) est :

Réponses :

1. `<a href="https://www.w3schools.com/">lien hypertexte</a>`

2. `<a href="https://www.w3schools.com/">https://www.w3schools.com/</a>`

3. `<a href="lien hypertexte">https://www.w3schools.com/</a>`

4. `<href a="https://www.w3schools.com/">lien hypertexte</href>`
:::


:::exercice
Pour créer un lien vers la page d'accueil de Wikipédia, que devra-t-on
écrire dans une page Web ?

__Réponses :__

1. __Réponse 1 :__ `<a target="http://fr.wikipedia.org">Wikipédia</a>`

2. __Réponse 2 :__  `<a href="http://fr.wikipedia.org">`

3. __Réponse 3 :__  `<a href="http://fr.wikipedia.org">Wikipédia</a>`

4. __Réponse 4 :__  `<link src="http://fr.wikipedia.org">Wikipédia</link>`
:::