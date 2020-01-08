# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:32:45 2019
@author: Jonathan Molieres
"""


# =============================================================================
# Programme principale du jeux d'echec
# =============================================================================
from time import sleep

# import des classes
from Echiquier import Echiquier8x8
print("\n\033[4mJeux d'echecs, exit permet d'arreter le jeux\033[0m")
      
if  __name__=='__main__':
    print("\nEntrer 1v1 pour jouer contre un humain et ia pour jouer contre l'ordinateur")  
    choix = input("Choix du mode de jeu : ")
    ech=Echiquier8x8()
    '''boucle infinie pour le jeux d'échec'''
    if choix == "1v1" :
        while True:
            ech.__str__()
            if ech.tourJoueur=='blanc':
                print("Entrer la case de départ du pion à déplacer puis la case d'arrivée. Par exemple : a7a6 "+
                      "permet de déplacer le pion de a7 en a6. \nPour roquer, il faut écrire le mot roque suivi "+
                      "de la position de la tour que l'on souhaite 'roquer'. Par exemple roqueh1")
                mouvement=input('Entrer le mouvement (exit permet de quitter) : ')
                if mouvement  == 'historique':
                    ech.affichageHistorique()
                elif len(mouvement)==7:
                    try: 
                        ech.roque(mouvement[2:])
                    except:
                        print("\033[31mCommande non valide. Veuillez Recommencer\033[0m")
                        sleep(2)
                        
                elif len(mouvement)==4:
                    if mouvement=='exit': 
                        break
                    else:
                        try:
                            ech.deplacer(mouvement[:2],mouvement[2:]) 
                        except:
                            print("\033[31mCommande non valide. Veuillez Recommencer\033[0m")
                            sleep(2)
                else:
                    print("\033[31mCommande non valide. Veuillez Recommencer\033[0m")
                    sleep(2)
    elif choix == "ia" :
        print("Le mode de jeu contre une intelligence artificielle n'est pas encore disponible")
