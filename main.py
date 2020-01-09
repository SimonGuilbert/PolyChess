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
from IA import IA
print("\n\033[4mJeux d'echecs, exit permet d'arrêter le jeu\033[0m")
      
if  __name__=='__main__':
 
    print("\nEntrer \033[31m1v1\033[0m pour jouer contre un humain 1et \033[31mia\033[0m pour jouer contre l'ordinateur")  
    choix = input("Choix du mode de jeu : ")
    ech=Echiquier8x8()
    ia=IA()
    '''boucle infinie pour le jeux d'échec'''
    if choix == "1v1" :
        # Au début de la partie, aucun roi n'est en échec donc echec = False
        echec = False
        while True:  
            ech.__str__()
            print("\nEntrer la case de départ du pion à déplacer puis la case d'arrivée. Par exemple \033[31ma7a6\033[0m "+
                  "permet de déplacer le pion de a7 en a6. \n\nPour roquer, il faut écrire le mot roque suivi "+
                  "de la position de la tour que l'on souhaite 'roquer'. Par exemple \033[31mroqueh1\033[0m")
            if echec == False :
                mouvement=input('Aux '+str(ech.tourJoueur)+'s de jouer (exit permet de quitter) : ')        
            if mouvement  == 'historique':
                ech.affichageHistorique()
            elif len(mouvement)==7:
                try: 
                    ech.roque(mouvement[-2:])
                except:
                    print("\033[31mCommande non valide. Veuillez Recommencer1\033[0m")
                    sleep(2)
                    
            elif len(mouvement)==4:
                if mouvement=='exit': 
                    break
                else:
                    try:
                        ech.deplacer(mouvement[:2],mouvement[2:]) 
                        nbPosRoi=ech.echec()
                        if nbPosRoi!=0 and nbPosRoi!=-1:
                            echec = True
                            mouvement=input('Vous êtes en échec. Aux '+str(ech.tourJoueur)+'s de jouer (exit permet de quitter) : ')
                            #ajouter code ici pour le cas echec        
                    except:
                        print("\033[31mCommande non valide. Veuillez Recommencer2\033[0m")              
                        sleep(2)    
            else:
                print("\033[31mCommande non valide. Veuillez Recommencer3\033[0m")
                sleep(2)            
    
    elif choix == "ia" :
        #print("Le mode de jeu contre une intelligence artificielle n'est pas encore disponible")
        # Au début de la partie, aucun roi n'est en échec donc echec = False
        tours=0
        echec = False
        while True:  
            ech.__str__()
            if tours%2 == 0:
                print("\nVous jouez avec les blancs.\nEntrer la case de départ du pion à déplacer puis la case d'arrivée. Par exemple \033[31ma7a6\033[0m "+
                      "permet de déplacer le pion de a7 en a6. \n\nPour roquer, il faut écrire le mot roque suivi "+
                      "de la position de la tour que l'on souhaite 'roquer'. Par exemple \033[31mroqueh1\033[0m")
                if echec == False :
                    mouvement=input('A vous de jouer (exit permet de quitter) : ')        
                if mouvement  == 'historique':
                    ech.affichageHistorique()
                elif len(mouvement)==7:
                    try: 
                        ech.roque(mouvement[-2:])
                    except:
                        print("\033[31mCommande non valide. Veuillez Recommencer1\033[0m")
                        sleep(2)
                        
                elif len(mouvement)==4:
                    if mouvement=='exit': 
                        break
                    else:
                        try:
                            ech.deplacer(mouvement[:2],mouvement[2:]) 
                            nbPosRoi=ech.echec()
                            if nbPosRoi!=0 and nbPosRoi!=-1:
                                echec = True
                                mouvement=input("Vous êtes en échec. A l'IA de jouer (exit permet de quitter) : ")
                                #ajouter code ici pour le cas echec  
                        except:
                            print("\033[31mCommande non valide. Veuillez Recommencer\033[0m")
                            sleep(2)
                else:
                    print("\033[31mCommande non valide. Veuillez Recommencer\033[0m")
                    sleep(2)
                tours+=1
            else:
                print("\nA l'IA de jouer")
#                if ia.ouverture()!= None:
#                    mouvement=ia.ouverture()
#                    ech.deplacer(mouvement[:2],mouvement[2:])
                break

        
        
        
        
        
        
        
        
        
