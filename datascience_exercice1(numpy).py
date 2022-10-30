# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 20:45:07 2022

@author: Jephté Dunia
"""

import numpy as np

# Cette fonction initialisation retourne une matrice aléatoire (m, n+1)
# Avec une colonne à droite remplie de '1'

def initialisatiion(m, n):
    # m: nombre de lignes
    # n : nombre de colonnes

    mon_tableau = np.empty((m,n), dtype=np.int16)
    # mon_tableau : création d'une matrice aléatoire
    fusion_array = np.ones((m,1))
    # fusion_array : stock une matrice à 'm' lignes et 1 colonne

    fusion = np.concatenate((mon_tableau, fusion_array), axis=1)
    # fusion --> stock la fusion horizontale de la matrice 'mon_tableau' et 'fusion_array'

    return fusion

print("--------------------------------------------------------------------")
print()
lignes = int(input("Veuillez saisir le nombre des lignes : "))
colonnes = int(input("Veuillez saisir le nombre des colonnes : "))

tableau = initialisatiion(lignes, colonnes)

print(tableau)