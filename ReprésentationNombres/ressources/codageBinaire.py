
def codageBinaireGlouton(n):
    """Retourne une liste d'entiers représentant le codage
    binaire de l'entier n écrit en base 10"""
    binaire = []
    #recherche de la plus petite puissance de 2 supérieure ou égale à n
    puissance2 = 1
    while puissance2 < n:
        puissance2 = puissance2 * 2
    #à compléter
    return binaire


def codageBinaire2(n):
    """Retourne une liste d'entiers représentant le codage
    binaire de l'entier n écrit en base 10.
    Algorithme des divisions successives"""
    binaire = []
    while n > 2:
        "à compléter"
    #décommenter l'instruction suivante
    #si vous avez stocké les bits dans l'ordre inverse
    binaire.reverse()
    return binaire
