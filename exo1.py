from math import pi,sqrt
import requests

def exercice_1(a,b):
    """
    Ecrire une fonction qui renvoie le produit des deux elements a et b

    """
    if isinstance(a,int) and isinstance(b,int):
        return a*b
    else:
        raise TypeError


def exercice_2(x, a, b):
    """
    Ecrire une fonction qui renvoie :
        -255 si x<a
        x si a<x<b
        255 si x>b
    (A faire en TDD)
    """
    pass

    if x < a:
        return -255
    if x > b :
        return 255

from math import pi
from math import sqrt

class Exercice_3:
    """
    Ecrire une classe qui renvoie des informations sur un cercle
    """

    def __init__(self, r):
        self.r = r

    def aire(self,r):
        """
        Ecrire une fonction qui renvoie l'aire d'un disque de rayon r
        """
        return pi*self.r**2

    def perimetre(self):
        """
        Ecrire une fonction qui renvoie le perimÃ¨tre d'un cercle de rayon r
        """
        return 2*pi*self.r

    def dans_cercle(self, x, y):
        """
        Ecrire une fonction qui renvoie True si le point (x, y) est dans
        le cercle de r et de centre (0, 0)
        """
        res = sqrt(x**2 +y**2)
        if  res <= self.r:
            return True
        else:
            return False

