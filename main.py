# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:32:45 2019
@author: Jonathan Molieres
"""


# =============================================================================
# Programme principale du jeux d'echec
# =============================================================================

# import des classes
from echiquier import Echiquier8x8
print("Jeux d'echec , exit permet d'arreter le jeux ")
      
if  __name__=='__main__':
    ech=Echiquier8x8()
    '''boucle infini pour le jeux d'échec'''
    while True:
        ech.__str__()
        if ech.tourJoueur=='blanc':
            print("Entrer la case du pion souhaiter  puis la case de deplacement par exemple; a8a6 permet de faire deplacer le pion en a8 en a6 ")
            mouvement=input('entrer le mouvement:')
            if len(mouvement)==4:
                if mouvement=='exit': 
                    break
                else:
                    ech.deplacer(mouvement[:2],mouvement[2:])
            
                    