## Exercice 1

def chiffres2nombre(t):
    """Retourne l'écriture en base 10 d'un entier à partir de
    la liste de ses chiffres"""
    n = 0
    expomax = len(t) - 1
    for k in range(expomax + 1):
        n = n + 10 ** (expomax - k) * t[k]
    return n

## Exercice 3
def bits2nombre(t):
    """Retourne l'entier en base dix représenté
    par une liste de bits t avec bits de poids fort
    à gauche"""
    n = 0
    for bit in t:
        n = n * 2 + bit
    return n

## Exercice 4

def additionBinaire8bits(t1, t2):
    t3 = [0]  * 8
    retenue = 0
    for k in range(7, -1 , -1):
        s = t1[k] + t2[k] + retenue
        t3[k] =  s % 2
        retenue = s // 2
    return t3