##image binaires pbm

#Damier (énoncé)
f = open('damier.pbm', 'w')
f.write('P1\n')
f.write(str(500) + ' ' + str(500) + '\n')
for lig in range(500):
    for col in range(500):
        f.write(str((lig // 50 + col // 50) % 2) + ' ')
    f.write('\n')
f.close()

def creer_image_pbm(but, L, H, generateur):
    """Crée un fichier but au format pbm, représentant une image
    de dimensions L x H dont le pixel en (lig, col) est généré par
    generateur(lig, col)
    """
    f = open(but, 'w')
    f.write('P1\n')
    f.write(str(L) + ' ' + str(H) + '\n')
    for lig in range(H):
        for col in range(L):
            f.write(str(generateur(lig, col)) + ' ')
        f.write('\n')
    f.close()
    
def generateur1(lig, col):
    return  ((lig + col) // 50) % 2
    
    
def generateur2(lig, col):
    return  (lig // 50 + col// 50) % 2
    
    
    
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
            if caractere == '1':    #lecture d'un 1
                g.write('0')
            elif caractere == '0':  #lecture d'un 0
                g.write('1')
            else:           #lecture d'un espace ou d'un caractère de fin de ligne
                g.write(c)
    g.close()
    f.close()
                

##images en niveaux de gris ppm
from PIL import Image
import numpy as np

def convert_bitmapgray_to_ppm(source, but):
    """Convertit un fichier source d'image bitmap en niveaux de gris
    en fichier texte ppm"""
    im = Image.open(source)
    H = im.height
    L = im.width
    tab = np.asarray(im)
    f = open(but,'w')
    f.write('P2\n')
    f.write(str(L) + ' ' + str(H) + '\n')
    f.write('255\n')
    for lig in tab:
        for val in lig:
            f.write(str(val) + ' ')
        f.write('\n')
    f.close()
    

    
def rechercher_pixel_ppm(source, lig, col):
    f = open(source, 'r')
    for k in range(3 + lig - 1):
        f.readline()
    ligne = f.readline().split()
    f.close()
    return int(ligne[col])
        
        
        
def flop_ppm(source, but):
    """
    Lit un fichier source au format ppm et le recopie dans un fichier but 
    en lui appliquant un flop, symétrie axiale par rapport au bord inférieur
    """
    #ouverture de fichiers en mode lecture pour source et écriture pour but
    f = open(source, 'r')
    g = open(but, 'w')
    #on recopie l'en-tête (les trois premières lignes)
    for k in range(3):
        lig = f.readline()
        g.write(lig)
    #on lit les lignes suivantes de la source
    lignes_source = f.readlines()
    #on les recopie dans l'ordre inverse
    for lig in reversed(lignes_source):
        g.write(lig)
    g.close()
    f.close()
    
def flip_ppm(source, but):
    """
    Lit un fichier source au format ppm et le recopie dans un fichier but 
    en lui appliquant un flip, symétrie axiale par rapport au bord droit
    """
    #ouverture de fichiers en mode lecture pour source et écriture pour but
    f = open(source, 'r')
    g = open(but, 'w')
    #on recopie l'en-tête (les trois premières lignes)
    for k in range(3):
        lig = f.readline()
        g.write(lig)
    #pour les lignes codant les pixels on inverse chaque valeur de pixel
    for lig in f:
        pixel_lig = lig.split()
        g.write(' '.join(pixel_lig[::-1])+ '\n')
    g.close()
    f.close()
    
#recopie d'un fichier à l'envers

f = open('endroit.txt', 'r')
g = open('envers.txt', 'w')
lig = f.readline() #saut de la première ligne
g.write(lig)
liste_lignes = f.readlines()
for lig in reversed(liste_lignes):
    g.write(lig)
f.close()
g.close()

## Transformation du photomaton

from PIL import Image
import numpy


def transformation(i, j, n):
    """
    Retourne les coordonnées du pixel image du pixel de coordonnées (i, j)
    par la transformation du photomaton appliquée à une image n x n
    """
    if i % 2 == 0 and j % 2 == 0:
        return (i // 2, j // 2)
    elif i %2 == 0 and j % 2 == 1:
        return (i // 2, (n + j) // 2)
    elif i % 2 == 1 and j % 2 == 0:
        return ((n + i) // 2, j // 2)
    else:
        return ((n + i) // 2, (n + j) // 2)
        
def copie(tableau):
    """Retourne la copie profonde d'un tableau à deux dimensions"""
    return numpy.array([[tableau[i][j] for j in range(len(tableau[i]))] 
    for i in range(len(tableau))], dtype = 'uint8')
    
def photomaton(tableau):
    """Retourne le tableau calculé obtenu après application de la transformation
    du photomaton au tableau passé en paramètre"""
    tableau2 = copie(tableau)
    n = len(tableau)
    for i in range(n):
        for j in range(n):
            (i2, j2) = transformation(i, j, n)
            tableau2[i2][j2] = tableau[i][j]
    return tableau2
            
def photomaton_iterer(source, k):
    im = Image.open(source)
    nom, extension = source.split('.')
    tab = np.asarray(im)
    for iteration in range(1, k + 1):
        tab = photomaton(tab)
        im = Image.fromarray(tab)
        im.save(nom + '-photomaton-iteration-' + str(iteration) + '.' + extension)
    
    
    