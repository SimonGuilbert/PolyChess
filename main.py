# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:32:45 2019
@author: Jonathan Molieres
"""
# =============================================================================
# Programme principale du jeux d'echec
# =============================================================================
# import des classes
from Echiquier import Echiquier
from time import sleep
from IA import IA
print('=============================================================================')
print("                            Jeux d'echecs")
print('=============================================================================')
if  __name__=='__main__':
 
    print("\nEntrer \033[31m1v1\033[0m pour jouer contre un humain 1et \033[31mia\033[0m pour jouer contre l'ordinateur")  
    choix = input("Choix du mode de jeu : ")
    ech=Echiquier()
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
                    ech.changementDeCouleur()
                except:
                    print("\033[31mCommande non valide. Veuillez Recommencer1\033[0m")
                    sleep(2)
                    
            elif len(mouvement)==4:
                if mouvement=='exit': 
                    break
                else:
                    
                    if ech.testeDeplacer(mouvement[:2],mouvement[2:]):
                        ech.deplacer(mouvement[:2],mouvement[2:]) 
                        BoolEchec=ech.echec()
                        print('bool='+str(BoolEchec))
                        if BoolEchec==True:
                             mouvement=input('Vous êtes en échec. Aux '+str(ech.tourJoueur)+'s de jouer (exit permet de quitter) : ')
                             ech.deplacer(mouvement[:2],mouvement[2:]) 
                    else:
        
                        print("\n\033[31mLe coup n'est pas possible. Réessayez\033[0m")
                        sleep(2)
            else:
                print("\033[31mCommande non valide. Veuillez Recommencer3\033[0m")
                sleep(2)             
    
        elif choix == "ia" :
        # Au début de la partie, aucun roi n'est en échec donc echec = False
        tours=0
        echec = False
        while True:  
            ech.__str__()
            if ech.get_TourJoueur()=='blanc':
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
                        print("\033[31mCommande non valide. Veuillez Recommencer11\033[0m")
                        sleep(2)
                        
                elif len(mouvement)==4:
                    if mouvement=='exit': 
                        break
                    else:
                        try:
                            #Test si le mouvement sont possibles
                            if ech.testeDeplacer(mouvement[:2],mouvement[2:]):
                                ech.deplacer(mouvement[:2],mouvement[2:]) 
                                tours+=1
                                BoolEchec=ech.echec()
                                #Verifie si il y a echec
                                if BoolEchec==True:
                                      mouvement=input('Vous êtes en échec. A vous de jouer (exit permet de quitter) : ')
                                      ech.deplacer(mouvement[:2],mouvement[2:]) 
                            else:
                                print("\n\033[31mLe coup n'est pas possible. Réessayez\033[0m")
                                sleep(2)   
                        except:
                            print("\033[31mCommande non valide. Veuillez Recommencer21\033[0m")
                            sleep(2)
                else:
                    print("\033[31mCommande non valide. Veuillez Recommencer31\033[0m")
                    sleep(2)
            else:
                hist=ech.get_historique()
                #print("\nA l'IA de jouer")
                #Bibliotheque d'ouverture
                if ia.ouverture(hist)!= None:
                    try:
                        mouvement=str(ia.ouverture(hist))
                        print("\nL'IA joue le mouvement :",mouvement)
                        ech.deplacer(mouvement[:2],mouvement[2:])
                        tours+=1
                    except:
                        print("\033[31mCommande non valide. Veuillez Recommencer41\033[0m")
                        sleep(2)
                #Fin de la partie
                #Verifie si il y a echec
                elif ech.echec()==True:
                    print("L'IA est en echec")
                    break                             
                #Suite du jeu 
                else: 
                    try:
                        mouvement=ia.middlegame(hist,ech)
                        print("\nL'IA joue le mouvement :",mouvement)
                        ech.deplacer(mouvement[:2],mouvement[2:])
                        tours+=1
                    except:
                        print("\033[31mCommande non valide. Veuillez Recommencer51\033[0m")
                        break
                        sleep(2)
