  - [Crédits](#crédits)
  - [Programmation en Python](#programmation-en-python)
  - [Représentation des nombres, des textes ou des
    images](#représentation-des-nombres-des-textes-ou-des-images)
  - [Architecture](#architecture)
  - [Algorithmique](#algorithmique)
  - [Le Web](#le-web)

# Crédits

Plusieurs exercices sont tirés des questions proposées sur le site
<https://genumsi.inria.fr/>.

# Programmation en Python

**Exercice 1**

*Auteur : Aude Durand Senter, question n°178 Genumsi*

On a saisi le code suivant :

``` python
def mystere(nombre) :
    while nombre > 5 :
        nombre = nombre - 5
return nombre
```

Quelle affirmation est vraie dans celles proposées ci-dessous ?

Réponses :

1.  On sort de la boucle while dès que `nombre > 5`
2.  On sort de la boucle while dès que `nombre < 5`
3.  On sort de la boucle while dès que `nombre <= 5`
4.  On continue la boucle tant que `nombre <= 5`

**Exercice 2**

*Auteur : Nicolas Revéret*

On considère le programme ci-dessous :

``` python
a = 8
b = 5
a = a + b
b = a - b
a = a - b
```

Quelles sont les valeurs des variables `a` et `b` à la fin du programme
?

**Exercice 3**

*Auteur : Nicolas Revéret*

On souhaite que l’utilisateur saisisse une valeur entière comprise entre
1 et 20 (inclus).

Quel code est correct ?

Réponses :

1.  
<!-- end list -->

``` python
a = int ( input("Saisir un nombre entre 1 et 20") )
while (a < 1 and a > 20) :
      a = int ( input("Saisir un nombre entre 1 et 20") )
```

2.  
<!-- end list -->

``` python
while (a < 1 and a > 20) :
    a = int ( input("Saisir un nombre entre 1 et 20") )
```

3.  
<!-- end list -->

``` python
a = int ( input("Saisir un nombre entre 1 et 20") )
while (a < 1 or a > 20) :
    a = int ( input("Saisir un nombre entre 1 et 20") )
```

4.  
<!-- end list -->

``` python
a = int ( input("Saisir un nombre entre 1 et 20") )
while (a >= 1 and a >= 20) :
    a = int ( input("Saisir un nombre entre 1 et 20") )
```

**Exercice 4**

*Auteur : Nicolas Revéret*

On a saisi le code suivant :

``` python
a = 12
for i in range(3) :
  a = a * 2
  a = a - 10
```

Quelle est la valeur de la variable `a` après l’exécution du code ?

**Exercice 5**

Pour les questions suivantes, il faut utiliser obligatoirement deux
boucles imbriquées et au maximum deux fois la fonction `print`.

1.  Ecrire un script Python qui produit l’affichage 1 ci-dessous.
2.  Ecrire un script Python qui produit l’affichage 2 ci-dessous.

**Affichage 1**

``` python
0
01
012
0123
01234
```

**Affichage 2**

``` python
01234
12345
23456
34567
45678
```

**Exercice 6**

Pour le diplôme du baccalauréat, si on note
![m](https://latex.codecogs.com/png.latex?m "m") la moyenne du candidat,
quatre mentions sont possibles : *Passable* si ![10 \\leqslant m
\< 12](https://latex.codecogs.com/png.latex?10%20%5Cleqslant%20m%20%3C%2012
"10 \\leqslant m \< 12"), *Assez bien* si ![12 \\leqslant m
\< 14](https://latex.codecogs.com/png.latex?12%20%5Cleqslant%20m%20%3C%2014
"12 \\leqslant m \< 14"), *Bien* si ![14 \\leqslant m
\< 16](https://latex.codecogs.com/png.latex?14%20%5Cleqslant%20m%20%3C%2016
"14 \\leqslant m \< 16") et *Très bien* sinon. Recopier et compléter le
script Python ci-dessous pour qu’il affiche la mention d’un candidat
admis (on suppose sa moyenne supérieure ou égale à 10).

``` python
m = float(input('Moyenne du candidat ? '))
if 10 <= m < 12:
    print("Passable")
#to be completed
```

**Exercice 7**

*Auteur : Nicolas Revéret*

On considère le code suivant :

``` python
def f(tab):
  for i in range(len(tab)//2):
    tab[i],tab[-i-1] = tab[-i-1],tab[i]
```

Après les lignes suivantes :

``` python
tab = [2,3,4,5,7,8]
f(tab)
```

Quelle est la valeur de la variable `tab` ?

Réponses :

1.  `[2,3,4,5,7,8]`
2.  `[5,7,8,2,3,4]`
3.  `[8,7,5,4,3,2]`
4.  `[4,3,2,8,7,5]`

**Exercice 8**

*Auteur : Christophe Beasse*

Que contient la variable `a` si on exécute ce script ?

``` python
def carre(val):
  return val*val

def inc(val):
  return val + 1

a = carre(inc(3.0))
```

1.  9.0
2.  12.0
3.  10.0
4.  16.0

**Exercice 9**

*Auteur : Christophe Beasse*

Soit la liste suivante : `liste_pays =
["France","Allemagne","Italie","Belgique"]`

Que renvoie : `liste_pays[2]` ?

Réponses :

1.  `"France"`
2.  `"Allemagne"`
3.  `"Italie"`
4.  `"Belgique"`

**Exercice 10**

*Auteur : Christophe Beasse*

Quelle est le résultat de : `[ (a,b) for a in range(3) for b in range(a)
]` ?

Réponses :

1.  `[(1,0),(2,1),(2,1)]`
2.  `[(1,0),(2,1),(3,2)]`
3.  `[(1,0),(2,0),(2,1)]`
4.  `[(0,0),(1,1),(2,2)]`

**Exercice 11**

Ecrire une fonction `moyenne(t)` qui prend en argument un tableau de
nombres t et qui retourne sa moyenne arithmétique.

**Exercice 12**

*Auteur : Nicolas Revéret*

On dispose d’un tableau d’entiers, ordonné en ordre croissant.

On désire connaître le nombre de valeurs distinctes contenues dans ce
tableau.

Quelle est la fonction qui ne convient pas ?

Réponses :

1.  
<!-- end list -->

``` python
def compte(t):
    cpt = 1
    for i in range(1,len(t)):
    if t[i] != t[i-1]:
        cpt = cpt + 1
    return cpt
```

2.  
<!-- end list -->

``` python
    def compte(t):
      cpt = 0
      for i in range(0,len(t)-1):
        cpt = cpt + int(t[i] != t[i+1])
      return cpt
```

3.  
<!-- end list -->

``` python
    def compte(t):
      cpt = 0
      for i in range(0,len(t)-1):
        if t[i] != t[i+1]:
          cpt = cpt + 1
      return cpt+1
```

**Exercice 13**

*Auteur : Eric Rougier*

Quel est le résultat de l’évaluation de l’expression Python suivante ?

`[2 ** n for n in range(4)]`

Réponses :

1.  `[0, 2, 4, 6, 8]`
2.  `[1, 2, 4, 8]`
3.  `[0, 1, 4, 9]`
4.  `[1, 2, 4, 8, 16]`

**Exercice 14**

*Auteur : Germain Becker, question n°326 Genumsi* Quel est le tableau
`t` construit par les instructions suivantes ?

``` python
tab = [1, 2, -3, 7, 4, 10, -1, 0]
t = [e for e in tab if e >= 0]
```

Réponses :

1.  `t = [1, 2, 7, 4, 10, 0]`
2.  `t = [e, e, e, e, e, e]`
3.  `t = [1, 2, 7, 4, 10]`
4.  `t = [-3, -1, 0]`

**Exercice 15**

*Auteur : Germain Becker, question n°339 Genumsi*

On considère le tableau t suivant.

`t = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]`

Quelle est la valeur de t\[1\]\[2\] ?

Réponses :

1.  1
2.  3
3.  4
4.  2

**Exercice 16**

*Auteur : Eric Rougier, question n°150 Genumsi*

Quelle est la valeur de la variable image après exécution du script
Python suivant ?

``` python
image = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(4):
    for j in range(4):
        if (i+j) == 3:
            image[i][j] = 1
```

Réponses :

1.  `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]`

2.  `[[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]`

3.  `[[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]`

4.  `[[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]`

**Exercice 17**

*Auteur : Sylvie Genre, question n°197 Genumsi*

La fonction suivante doit calculer la moyenne d’un tableau de nombres,
passé en paramètre. Avec quelles expressions faut-il compléter
l’écriture pour que la fonction soit correcte ? :

``` python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```

Réponses :

1.  0 et `len(tableau)`
2.  0 et `len(tableau) + 1`
3.  1 et `len(tableau)`
4.  1 et `len(tableau) + 1`

**Exercice 18**

*Auteur : Nicolas Réveret, question n°379 Genumsi*

On a saisi le code suivant :

``` python
liste = [0, 1, 2, 3]
compteur = 0
for i in range(len(liste)-1) :
    for j in range(i,len(liste)) :
        compteur += 1
```

Que contient la variable compteur à la fin de l’exécution de ce script ?

**Exercice 19**

Quelle est la valeur référencée par la liste L après exécution du
programme ci-dessous ?

``` python
L = [731, 732, 734]
L[0], L[1] = L[1], L[0]
M = L
M[1] = 732
```

1.  \[732, 731, 734\]
2.  \[731, 732, 734\]
3.  \[732, 732, 734\]

# Représentation des nombres, des textes ou des images

**Exercice 20**

Le codage en base deux de l’entier 26 en base dix est :

1.  11010
2.  10010
3.  11001
4.  110010

**Exercice 21**

Le résultat de la somme ![\\overline{101101}^{2} +
\\overline{101111}^{2}](https://latex.codecogs.com/png.latex?%5Coverline%7B101101%7D%5E%7B2%7D%20%2B%20%5Coverline%7B101111%7D%5E%7B2%7D
"\\overline{101101}^{2} + \\overline{101111}^{2}") est :

1.  ![\\overline{1100100}^{2}](https://latex.codecogs.com/png.latex?%5Coverline%7B1100100%7D%5E%7B2%7D
    "\\overline{1100100}^{2}")
2.  ![\\overline{1110101}^{2}](https://latex.codecogs.com/png.latex?%5Coverline%7B1110101%7D%5E%7B2%7D
    "\\overline{1110101}^{2}")
3.  ![\\overline{1011100}^{2}](https://latex.codecogs.com/png.latex?%5Coverline%7B1011100%7D%5E%7B2%7D
    "\\overline{1011100}^{2}")
4.  ![\\overline{1111100}^{2}](https://latex.codecogs.com/png.latex?%5Coverline%7B1111100%7D%5E%7B2%7D
    "\\overline{1111100}^{2}")

**Exercice 22**

Le plus grand entier qu’on peut représenter en base deux sur 8 bits est
:

1.  11111111
2.  10000000
3.  255
4.  256

**Exercice 23**

Le codage en base seize de l’entier
![256](https://latex.codecogs.com/png.latex?256 "256") est :

1.  ![\\overline{F1}^{16}](https://latex.codecogs.com/png.latex?%5Coverline%7BF1%7D%5E%7B16%7D
    "\\overline{F1}^{16}")
2.  ![\\overline{A1}^{16}](https://latex.codecogs.com/png.latex?%5Coverline%7BA1%7D%5E%7B16%7D
    "\\overline{A1}^{16}")
3.  ![\\overline{FA}^{16}](https://latex.codecogs.com/png.latex?%5Coverline%7BFA%7D%5E%7B16%7D
    "\\overline{FA}^{16}")
4.  ![\\overline{FF}^{16}](https://latex.codecogs.com/png.latex?%5Coverline%7BFF%7D%5E%7B16%7D
    "\\overline{FF}^{16}")

**Exercice 24**

L’adresse MAC de la carte Wifi d’un smartphone est  avec six octets
codés en base seize.

La transcription en base dix de cette adresse MAC est :

1.  ![200:96:0:164:137:171](https://latex.codecogs.com/png.latex?200%3A96%3A0%3A164%3A137%3A171
    "200:96:0:164:137:171")
2.  ![20:6:0:14:17:21](https://latex.codecogs.com/png.latex?20%3A6%3A0%3A14%3A17%3A21
    "20:6:0:14:17:21")
3.  ![96:0:0:40:72:110](https://latex.codecogs.com/png.latex?96%3A0%3A0%3A40%3A72%3A110
    "96:0:0:40:72:110")
4.  ![140:6:0:74:152:186](https://latex.codecogs.com/png.latex?140%3A6%3A0%3A74%3A152%3A186
    "140:6:0:74:152:186")

**Exercice 25**

La fonction ci-dessous doit retourner la liste des chiffres en base deux
d’un entier n par ordre décroissant des poids de gauche à droite.

``` python
def nombre2chiffres(n):
    t = []
    while n >= 2:
        ..........
        n = n // 2
    ..............
    t.reverse()
    return t
```

Quelle instruction peut-on écrire en lignes 4 et 6 ?

1.  `t.append(n)`
2.  `t.append(n % 2)`
3.  `t.append(n // 2)`
4.  `t = t + [n % 2]`

**Exercice 26**

1.  Représenter en binaire le nombre d’écriture décimale 49.
2.  Représenter en base dix, le nombre dont l’écriture en base deux est
    ![1010110](https://latex.codecogs.com/png.latex?1010110 "1010110").
3.  Déterminer le successeur en base deux des entiers :
      - ![111](https://latex.codecogs.com/png.latex?111 "111")
      - ![10011](https://latex.codecogs.com/png.latex?10011 "10011")
      - ![10111](https://latex.codecogs.com/png.latex?10111 "10111")
4.  Déterminer le nombre de caractères qu’on peut coder sur un octet.

**Exercice 27**

On souhaite convertir 25 de base 10 en base 2. On obtient en binaire :

Réponses :

1.  11001
2.  10110
3.  10011
4.  11000

**Exercice 28**

Quelle est la valeur affichée par l’exécution du test suivant ?

``` python
In [1]: 0.1 + 0.2 == 0.3              
                                                                                                                                                                         
Out[1]: False
```

Réponses :

1.  `True`
2.  `False`
3.  0.3

**Exercice 29**

Quelle est la valeur affichée a l’exécution du programme Python suivant
?

``` python
x = 1 
for i in range(11): 
    x = x * 2 
print(x)
```

Réponses :

1.  1024
2.  2048
3.  23
4.  ![2^{2^{11}}](https://latex.codecogs.com/png.latex?2%5E%7B2%5E%7B11%7D%7D
    "2^{2^{11}}")

**Exercice 30**

Quelle est la valeur affichée a l’exécution du programme Python suivant
?

``` python
x = 2 
for i in range(10): 
    x = x ** 2 
print(x)
```

Réponses :

1.  1024
2.  2048
3.  ![2^{2^{10}}](https://latex.codecogs.com/png.latex?2%5E%7B2%5E%7B10%7D%7D
    "2^{2^{10}}")
4.  ![2^{2^{11}}](https://latex.codecogs.com/png.latex?2%5E%7B2%5E%7B11%7D%7D
    "2^{2^{11}}")

**Exercice 31**

1.  Convertir 3970 en base 6.
2.  Convertir en base dix l’entier naturel dont l’écriture en base six
    est 4321.
3.  Écrire en Python une fonction `base6(L)` qui renvoie la valeur
    entière correspondant à la liste des chiffres de l’écriture en base
    6.

Exemple : `base6([1, 3, 2])` doit renvoyer 56 car ![1 \\times 6^{2} + 3
\\times 6 + 2
= 56](https://latex.codecogs.com/png.latex?1%20%5Ctimes%206%5E%7B2%7D%20%2B%203%20%5Ctimes%206%20%2B%202%20%3D%2056
"1 \\times 6^{2} + 3 \\times 6 + 2 = 56").

**Exercice 32**

1.  Pour déterminer la liste des chiffres en base dix d’un entier
    naturel, un élève a écrit la fonction ci-dessous :

<!-- end list -->

``` python
def liste_chiffres(n):
    L = [n % 10]
    while n > 0:
        n = n // 10
        L.insert(0, n % 10)
    return L
```

Malheureusement sa fonction ne retourne pas le résultat attendu pour
l’entier ![730](https://latex.codecogs.com/png.latex?730 "730") :

``` python
>>> liste_chiffres(730)
[0, 7, 3, 0]
```

Proposer une version corrigée de la fonction `liste\_chiffres`.

2.  Compléter la fonction `somme_chiffres_base2(n)` pour qu’elle
    retourne la somme des chiffres en base deux de l’entier `n` passé en
    paramètre.

<!-- end list -->

``` python
def somme_chiffres_base2(n):
    s = 0
    while n > 0:
        s = s + n % 2
        ..............
    return s
```

3.  Déterminer une valeur possible de la variable  telle que :

<!-- end list -->

``` python
>>> somme_chiffres(secret)
734
```

4.  Écrire une fonction `maximum_chiffre(n)` qui retourne le plus grand
    chiffre de l’écriture en base dix de l’entier naturel `n` passé en
    paramètre.

**Exercice 33**

Le nombre de chiffres en base
![2](https://latex.codecogs.com/png.latex?2 "2") d’un entier naturel
![n](https://latex.codecogs.com/png.latex?n "n") est :

  - ![1](https://latex.codecogs.com/png.latex?1 "1") si
    ![n](https://latex.codecogs.com/png.latex?n "n") est égal à
    ![0](https://latex.codecogs.com/png.latex?0 "0") ;
  - l’unique entier ![p](https://latex.codecogs.com/png.latex?p "p") tel
    que ![2^{p-1} \\leqslant n
    \< 2^{p}](https://latex.codecogs.com/png.latex?2%5E%7Bp-1%7D%20%5Cleqslant%20n%20%3C%202%5E%7Bp%7D
    "2^{p-1} \\leqslant n \< 2^{p}") si
    ![n](https://latex.codecogs.com/png.latex?n "n") supérieur à
    ![0](https://latex.codecogs.com/png.latex?0 "0").

Compléter la fonction ci-dessous pour qu’elle retourne le nombre de
chiffres en base ![2](https://latex.codecogs.com/png.latex?2 "2") de
l’entier  passé en paramètres.

``` python
def nbchiffres_base2(n):
    if n == 0:
        return 1
    nbchiffre = 1
    puissance = 1
    while ..............:
        .........................
        .........................
    return ......................
```

# Architecture

**Exercice 34**

En 1945, John Von Neumann a décrit un modèle d’architecture qui est
encore valable pour les ordinateurs actuels. Quelles sont les entités de
ce modèle et comment communiquent-elles ?

**Exercice 35**

A quelle expression logique correspond cette table de vérité ?

| A | B | f(A, B) |
| :-: | - | ------- |
| 0 | 0 | 1       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

**Exercice 36**

A quelle expression logique correspond cette table de vérité ?

| A | B | f(A, B) |
| :-: | - | ------- |
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

**Exercice 37**

A quelle expression logique correspond cette table de vérité ?

| A | B | f(A, B) |
| :-: | - | ------- |
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 1       |

**Exercice 38**

A quelle expression logique correspond cette table de vérité ?

| A | B | f(A, B) |
| :-: | - | ------- |
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

# Algorithmique

**Exercice 39**

Écrire une fonction `min2(a, b)` qui retourne le minimum de deux nombres
passés en paramètre, sans utiliser la fonction min du module builtins.

**Exercice 40**

Écrire une fonction `min_liste(L)` qui retourne le minimum d’une liste
de nombres passée en paramètre.

**Exercice 41**

Un élève a écrit la fonction ci-dessus pour déterminer si le premier
paramètre n est dans la liste L passée en second paramètre. Le
professeur lui indique que son code comporte des erreurs. Proposer une
version corrigée de cette fonction.

``` python
def element_dans_liste(n, L):
    for k in range(len(L)):
        if e == n:
            return True
        else:
            return False
```

**Exercice 42**

Pour chacune des listes ci-dessous, déterminer si l’algorithme le plus
adapté pour qu’une machine y recherche une valeur est l’algorithme de
recherche séquentielle ou l’algorithme de recherche dichotomique.

1.  Liste A :
    `[4, 6, 15, 20, 21, 26, 31, 41, 42, 50, 69, 87, 88, 92, 97]`
2.  Liste B :
    `[41, 97, 91, 59, 7, 45, 3, 96, 26, 32, 18, 11, 67, 74, 54]`

**Exercice 43**

Compléter le code de la fonction `recherche_dicho_dec(x, L)` qui prend
en paramètres un nombre `x` et une liste de nombres `L` triée dans
l’ordre décroissant. Elle doit retourner `True` si `x` appartient à L
et False sinon.

``` python
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
```

# Le Web

**Exercice 44**

Le protocole qui permet à un client de faire une requête de page Web
auprès d’un serveur Web s’appelle :

Réponses :

1.  Internet Protocol
2.  HTML
3.  HTTP
4.  TCP
5.  WWW

**Exercice 45**

Si la page demandée n’est pas disponible, le serveur Web renvoie au
client un code d’erreur :

Réponses :

1.  404

2.  504

3.  403

4.  503

**Exercice 46**

L’inventeur du World Wide Web au CERN est :

Réponses :

1.  Tim Berners-Lee

2.  Ted Nelson

3.  Louis Pouzin

4.  Vinton Cerf

**Exercice 47**

Dans le fichier source d’une page Web, le code qui permet de créer un
lien hypertexte vers la page <https://www.w3schools.com/> est :

Réponses :

1.  `<a href="https://www.w3schools.com/">lien hypertexte</a>`

2.  `<a
    href="https://www.w3schools.com/">https://www.w3schools.com/</a>`

3.  `<a href="lien hypertexte">https://www.w3schools.com/</a>`

4.  `<href a="https://www.w3schools.com/">lien hypertexte</href>`
