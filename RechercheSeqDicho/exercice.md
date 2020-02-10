# Exercices sur la recherche séquentielle et la recherche dichotomique

## Exercice 1

Compléter le code de la fonction ci-dessous pour qu'elle retourne le maximum de l'ensemble des éléments contenus dans la variable `mat`passée en argument. `mat` est un matrice de nombres, c'est-à-dire une  liste de  listes d'entiers qui ont toutes la  même longueur.

~~~python
In [5]: mat = [[1,2,3], [4,5,6]]

In [6]: mat[1]
Out[6]: [4, 5, 6]

In [7]: mat[1][2]
Out[7]: 6
~~~

~~~python
def max_matrice(mat):
  nlig, ncol = len(mat), len(mat[0])
  maxi = .....
  for i in range(nlig):
    for j in range(ncol):
      "à compléter"
  return maxi
~~~


## Exercice 2

Ecrire une fonction de signature  `recherche_seq_matrice(mat, n)` qui retourne un booléen indiquant la présence du nombre  `n` parmi les nombres  contenus dans la variable `mat`passée en argument. `mat` est un matrice de nombres, c'est-à-dire une  liste de  listes d'entiers qui ont toutes la  même longueur.


## Exercice 3

Compléter la fonction de signature `insertion_dicho_gauche(L, e)` ci-dessous pour qu'elle retourne l'index du point d'insertion du nombre `e` dans la liste triée dans l'ordre croissant `L``, avec la convention suivante : 

* `e` doit s'insérer à gauche du premier élément de `L` supérieur ou égal à `e`
* si tous les éléments de `L` sont inférieurs à `e`, ce dernier est inséré à la fin de la liste

~~~python
def insertion_dicho_gauche(L, e):
     
    if e <= L[0]:  # Cas 1 : e inférieur ou égal au premier (et donc plus petit) élément de la liste
        return 0
    elif e > L[-1]:  #Cas 2 : e supérieur à tous les éléments de la liste 
        return len(L)
    else: #Cas 3 : on maintient l'invariant de boucle : L[gauche] < e <= L[droite]
        gauche, droite = 0, len(L) - 1
        while .......................:    #condition d'arret ? => condition d'entrée de boucle 
            milieu = (droite + gauche) // 2
            if L[milieu] < e:
                "à compléter"
            else:
                "à compléter"
        return .............
 ~~~
