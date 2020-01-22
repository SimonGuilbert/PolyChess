# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:32:45 2019
@author: Jonathan Molieres
"""

# import des classes
from Echiquier import Echiquier
from time import sleep
from IA import IA

#Fonction: 
def erreur():
    '''fonction pour l'affichage d'erreur pour les commandes'''
    print("\033[31mCommande non valide. Veuillez Recommencer1\033[0m")
    sleep(2)
    
def erreurCoup():
    '''fonction pour l'affichage d'erreur pour les coups'''
    print("\n\033[31mLe coup n'est pas possible. Réessayez\033[0m")
    sleep(2)
def fonctionEchec(BoolEchDeplacement,EchecEtMat):
    '''fonction qui gere le cas d'une echec'''
    if ech.VerificationEchecEtMat():
        return True,True
    while BoolEchDeplacement== False:
         mouvement=input('Vous êtes en échec. Aux '+str(ech.tourJoueur)+'s de jouer (\033[31mexit\033[0m permet de quitter) : ')
         # boucle dans les cas ou une personnes est en echec
         if mouvement  == 'historique':
            ech.affichageHistorique()
         
         elif len(mouvement)==4:
             if mouvement=='exit':
                 
                 EchecEtMat=True  
                 BoolEchDeplacement=True
             else: 
                 try:
                    #echiquier fictif pour tester les coups
                    echiquierTeste=Echiquier()
                    echiquierTeste.chgtEchiquier(ech.echiquier)
                    echiquierTeste.chtCouleur(ech.tourJoueur)
                    echiquierTeste.deplacer(mouvement[:2],mouvement[2:])
                    if not echiquierTeste.echec()[0]:
                        ech.deplacer(mouvement[:2],mouvement[2:])
                        ech.__str__()#Fonction d'affichage
                        BoolEchDeplacement=True
                        ech.changementDeCouleur()
                    else:
                        erreurCoup()
                 except:
                     erreurCoup()
         elif len(mouvement)==7:
             try: 
                #echiquier fictif pour tester les coups
                echiquierTeste=Echiquier()
                echiquierTeste.chgtEchiquier(ech.echiquier)
                echiquierTeste.chtCouleur(ech.tourJoueur)
                echiquierTeste.deplacer(mouvement[:2],mouvement[2:])
                if not echiquierTeste.echec()[0]:
                    ech.roque(mouvement[-2:])
                    ech.changementDeCouleur()
             except:
                 erreur()
         else:
            erreur()
    return BoolEchDeplacement,EchecEtMat
# =============================================================================
# Programme principale du jeux d'echec
# =============================================================================
print('=============================================================================')
print("                            Jeux d'echecs")
print('=============================================================================')
if  __name__=='__main__':
    Menu=True
    while Menu:
        print('=============================================================================')
        print("                                 Menu")
        print('=============================================================================')
        print("\nEntrer \033[31m1v1\033[0m pour jouer contre un humain et \033[31mia\033[0m pour jouer contre l'ordinateur. Pour quitter, entrer \033[31mexit\033[0m.")  
        choix = input("Choix du mode de jeu : ")
        ech=Echiquier()#créaction de l'échiquier en état initial
# =============================================================================
# Mode Joueur contre Joueur    
# =============================================================================
        if choix == "1v1" :
            # Au début de la partie, aucun roi n'est en échec donc echecEtMAt= False et echec =False
            EchecEtMat=False
            echec = False
            
                
            while EchecEtMat==False:
                
                ech.__str__()#Fonction d'affichage
                # table de fin de jeux (syzygy)                
                valeurEchec=ech.echecEtMat()    
                if valeurEchec in [1,2]:
                    print('les'+str(ech.tourJoueur)+'ont gagnée')
                if valeurEchec in [-1,-2]:
                    ech.changementDeCouleur()
                    print('les'+str(ech.tourJoueur)+'ont gagnée')
                    
                print("\nEntrer la case de départ du pion à déplacer puis la case d'arrivée. Par exemple \033[31ma7a6\033[0m "+
                      "permet de déplacer le pion de a7 en a6. \n\nPour roquer, il faut écrire le mot roque suivi "+
                      "de la position de la tour que l'on souhaite 'roquer'. Par exemple \033[31mroqueh1\033[0m")
                if echec == False :
                    mouvement=input('Aux '+str(ech.tourJoueur)+'s de jouer (\033[31mexit\033[0m permet de quitter) : ')
                    if mouvement  == 'historique':
                        ech.affichageHistorique()
                    elif len(mouvement)==7:
                         try: 
                             ech.roque(mouvement[-2:])
                             ech.changementDeCouleur()
                         except:
                             erreur()
                    elif len(mouvement)==4:
                         if mouvement=='exit': 
                             EchecEtMat=True
                         else:
                             try:
                                 #appelle des fonction de deplacement
                                 if ech.testeDeplacer(mouvement[:2],mouvement[2:]):
                                     ech.deplacer(mouvement[:2],mouvement[2:]) 
                                     BoolEchec=ech.echec()[0]
                                     print('deplacement fait')
                                     if BoolEchec==True:#verification de l'echec apres le deplacement 
                                         ech.__str__()#Fonction d'affichage
                                         BoolEchDeplacement=False
                                         [BoolEchDeplacement,EchecEtMat]=fonctionEchec(BoolEchDeplacement,EchecEtMat)
                                                 
                                 else:
                                     erreurCoup()
                             except:
                                 erreurCoup()
                    else:
                         erreur()
            #fin de jeux: Annonce du gagnant
            ech.changementDeCouleur()
            print('Les '+str(ech.tourJoueur)+'s ont gagné')


# =============================================================================
# Mode joueur contre IA                    
# =============================================================================
        elif choix == "ia" :
            # Au début de la partie, aucun roi n'est en échec donc echec = False
            tours=0
            echec = False
            ia=IA()
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
                        
        elif choix =='exit':
              Menu=False       
        else:  
            erreur()
             