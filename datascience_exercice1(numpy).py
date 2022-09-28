# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 20:45:07 2022

@author: Jephté Dunia
"""

import numpy as np


def initialisatiion(m, n):
    mon_tableau = np.empty((m,n), dtype=np.float16)
    return mon_tableau

print("--------------------------------------------------------------------")
print()
lignes = int(input("Veuillez saisir le nombre des lignes : "))
colonnes = int(input("Veuillez saisir le nombre des colonnes : "))

tableau = initialisatiion(lignes, colonnes)

print(tableau)