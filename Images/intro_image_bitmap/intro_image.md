1. Créer un fichier `chapitre_image_bitmap.py`  avec  `Pyzo`

![Lena](./lenagray.png)

2. Récupérer le fichier [`lenagray.png`](./lenagray.png) et le copier dans le même répertoire que `chapitre_image_bitmap.py`

3. Copier/Coller  le code `Python` ci-dessous dans `chapitre_image_bitmap.py`. Exécuter puis chercher à  comprendre.

~~~python
from PIL import Image
import numpy


#on ouvre l'image
im = Image.open('lenagray.png')

#on affiche les dimensions, le format de fichier et le mode de l'image (binaire, niveaux de gris (L), RGB)
print(im.size,im.format, im.mode)

#on transforme l'image en tableau numpy à 2 dimensions  de pixels    
tab = numpy.asarray(im)

#on affiche le pixel en première ligne et dernière colonne
print(tab[0][511])

#on affiche les vingt premiers pixels de la première ligne
print(tab[0][:20])

#on affiche le pixel en dernière ligne et première colonne
print(tab[511][0])

#on crée un tableau 2 de mêmes dimensions que tab et rempli de 0
#Attention à bien créer un tableau numpy et à préciser le type 'uint8' qui correspond à un octer par pixel
nblig, nbcol = len(tab), len(tab[0])
tab2 = numpy.array([ [0] * nbcol for _ in range(nblig) ], dtype ='uint8')

#on recopie tab dans tab 2 mais en inversant l'ordre des lignes  (flop)
for lig in range(0, nblig):
    for col in range(0, nbcol):
        tab2[lig][col] = tab[nblig - 1 - lig][col]
        
#on transforme tab2 en image
im2 = Image.fromarray(tab2)
#on enregistre cette image sur le disque
im2.save("lenagray-flop.png")
~~~

3. Compléter le programme avec un code qui crée l'image ci-dessous :


![Lena-flip](./lenagray-flip.png)

4. Compléter la fonction `negatif` pour qu'elle enregistre sur le disque un négatif de l'image source en niveaux de gris.

~~~python
def negatif_gris(source, but):
    """Enregistre sur le disque un négatif de l'image source en niveaux de gris"""
    imsource= Image.open(source)
    tab = numpy.asarray(imsource)
    nbcol, nblig = len(tab[0]), len(tab)
    tab2 = numpy.array([ [0] * nbcol for _ in range(nblig) ], dtype ='uint8')    
    "à compléter"
    imbut = Image.fromarray(tab2)
    imbut.save(but)
~~~

Voici le résultat attendu pour `negatif_gris('lenagray.png', 'lenagray-negatif.png')` :


![Lena-negatif](./lenagray-negatif.png)
