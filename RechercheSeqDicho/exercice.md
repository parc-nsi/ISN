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
