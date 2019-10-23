##Exo 1 : images binaires pbm

#Damier (énoncé)
f = open('damier.pbm', 'w')
f.write('P1\n')
f.write(str(500) + ' ' + str(500) + '\n')
for lig in range(500):
    for col in range(500):
        f.write(str((lig // 50 + col // 50) % 2) + ' ')
    f.write('\n')
f.close()

    
def inverser_couleurs_pbm(source, but):
    """
    Lit un fichier source au format pbm et le recopie dans un fichier
    but en inversant les couleurs
    """
    #ouverture de fichiers en mode lecture pour source et écriture pour but
    f = open(source, 'r')
    g = open(but, 'w')
    #on recopie l'en-tête (les deux premières lignes)
    for k in range(2):
        lig = f.readline()
        g.write(lig)
    #pour les lignes codant les pixels on inverse chaque valeur de pixel
    for lig in f:
        for caractere in lig:
            pass #à commenter puis compléter
    g.close()
    f.close()
    
                

## Exo 2 Images en niveaux de gris ppm


## Exo 3 Transformation du photomaton

from PIL import Image
import numpy

def copie(tableau):
    """Retourne la copie profonde d'un tableau à deux dimensions"""
    return numpy.array([[tableau[i][j] for j in range(len(tableau[i]))] 
    for i in range(len(tableau))], dtype = 'uint8')

            
def photomaton_iterer(source, k):
    im = Image.open(source)
    nom, extension = source.split('.')
    tab = numpy.asarray(im)
    for iteration in range(1, k + 1):
        pass  #à commenter puis compléter
    
    
