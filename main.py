# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:32:45 2019
@author: Jonathan Molieres
"""

# import des classes
from Echiquier import Echiquier
from time import sleep
from IA import IA
# =============================================================================
# Fonction: 
# =============================================================================
def finPartie():
    '''fonction d'affichage en fin de partie'''          
    print('\n\n*****************************************************************************\n\n')
    print('                            Les ' + str(ech.tourJoueur) + 's ont gagné')
    print('\n\n*****************************************************************************\n\n\n')
    sleep(1.5)
    print('\n\n*****************************************************************************\n\n')
    print('                       Prêt pour une nouvelle partie ?')
    print('\n\n*****************************************************************************\n\n\n\n')
    sleep(2)

def erreurCoup():
    '''fonction pour l'affichage d'erreur pour les coups'''
    print("\033[31mCommande non valide. Vérifiez que votre saisie est de la forme e7a6 puis réessayez\033[0m")
    sleep(2)

def fonctionEchec(BoolEchDeplacement, EchecEtMat,ech,iaBooleen=False):
    '''fonction qui gere le cas d'une echec et verification de l'echec et mat'''
    if ech.VerificationEchecEtMat():
        return True, True
    # Cas du mode de l'ia
    if iaBooleen==True and ech.tourJoueur=='noir':
        ech.changementDeCouleur()
        print('echec')
        return True,False
    # Cas du mode 1v1
    while BoolEchDeplacement == False:# sortie de la boucle si le deplacement demande est valide
        echiquierTeste = Echiquier()#echiquier non afficher pour tester les coups
        for h in ech.get_historique():
            echiquierTeste.deplacer(h[0],h[1]) 
       
        mouvement = input("Vous êtes en échec. Aux " + str(ech.tourJoueur) + "s de jouer (\033[31mexit\033[0m permet d'abandonner) : ")
        # boucle dans les cas ou une personnes est en echec
        if mouvement == 'historique':# Affichage de l'historique sur demande
            ech.affichageHistorique()
            ech.__str__()#reaffichage de l'echiquier apres l'historique
        elif len(mouvement) == 4:
            if mouvement == 'exit':# Verification de l'abandon 
                EchecEtMat = True # Permet la sortie des boucles while
                BoolEchDeplacement =True # Permet la sortie des boucles while
            else:
                # echiquier fictif pour tester les coups
                echiquierTeste.deplacer(mouvement[:2], mouvement[2:])
                if not echiquierTeste.echec()[0]:# Verification
                    # Affectation du deplacement valide
                    ech.deplacer(mouvement[:2], mouvement[2:])
                    BoolEchDeplacement = True
                    ech.changementDeCouleur()
                else:
                    # Appelle de la fonction d'erreur
                    erreurCoup()
                    ech.__str__()  # Fonction d'affichage
        elif len(mouvement) == 7: # Gestion du roque
            
            if ech.TesteRoque(mouvement[-2:])==(True,ech.tourJoueur):
                # affichage du roque apres validation
                ech.roque(mouvement[-2:])
                ech.changementDeCouleur()
            else:# Affichage d'erreur si le roque n'est pas possible
                print("\033[31mCommande non valide. Si vous voulez roquer, utilisez la forme roqueh1\033[0m")
                sleep(2)
        else:
            # Appelle de la fonction d'erreur
            erreurCoup()
            if BoolEchDeplacement== False:
                ech.__str__()  # Fonction d'affichage
    return BoolEchDeplacement, EchecEtMat

def jeuxJoueur(EchecEtMat,ech,iaBooleen=False):
    #Affichage des commandes
    print("\nEntrez la case de départ du pion à déplacer puis la case d'arrivée. Par \nexemple \033[31ma7a6\033[0m " +
            "permet de déplacer le pion de a7 en a6. \n\nPour roquer, il faut écrire le mot roque suivi " +
            "de la position de la tour que \nl'on souhaite 'roquer'. Par exemple \033[31mroqueh1\033[0m.\n\nPour "+
            "afficher l'historique de la partie, entrez \033[31mhistorique\033[0m.\n\nPour abandonner, entrez " +
            "\033[31mexit\033[0m.")
    BoolEchDeplacement=False
    if echec == False:
        mouvement = input("Aux " + str(ech.tourJoueur) + "s de jouer : ")
        if mouvement == 'historique':# Affichage de l'historique sur demande
            ech.affichageHistorique()
        elif len(mouvement) == 7:
            if ech.TesteRoque(mouvement[-2:])==(True,ech.tourJoueur):
                # affichage du roque apres validation
                ech.roque(mouvement[-2:])
                ech.changementDeCouleur()
            else:# Affichage d'erreur si le roque n'est pas possible
                print("\033[31mCommande non valide. Si vous voulez roquer, utilisez la forme roqueh1\033[0m")
                sleep(2)
        elif len(mouvement) == 4:
            if mouvement == 'exit':
                # Verification de l'abandon
                return True# Permet la sortie des boucles while
            else:
                try:
                    #echiquier fictif pour tester les coups
                    echiquierTeste = Echiquier()
                    for h in ech.get_historique():
                        echiquierTeste.deplacer(h[0],h[1])
                    echiquierTeste.deplacer(mouvement[:2], mouvement[2:])
                    PropreEchec=echiquierTeste.echec()
                    # appelle des fonction de deplacement
                    if ech.testeDeplacer(mouvement[:2], mouvement[2:]) and PropreEchec!=(True,ech.tourJoueur):
                        ech.deplacer(mouvement[:2], mouvement[2:])
                        if ech.conversionEnIndex(mouvement[2:]) in ([i for i in range(8)] or ech.conversionEnIndex(mouvement[2:]) in [i for i in range(56,64)]) and ech.echiquier[ech.conversionEnIndex(mouvement[2:])].getNom()=='PION':
                            ech.promotion(ech.conversionEnIndex(mouvement[2:]))
                            ech.mvtPossible()
                        BoolEchec = ech.echec()[0]
                        if BoolEchec == True:  # verification de l'echec apres le deplacement
                            ech.__str__()  # Fonction d'affichage
                            BoolEchDeplacement = False
                            [BoolEchDeplacement, EchecEtMat] = fonctionEchec(BoolEchDeplacement, EchecEtMat,ech,iaBooleen)
                            ech.changementDeCouleur()
                    else:
                        print("\033[31mCommande non valide : La pièce " + mouvement[:2] + " n'a pas le droit de se déplacer en " + mouvement[2:] + " \033[0m")
                        sleep(2)
                except:
                    # Appelle de la fonction d'erreur
                    erreurCoup()
        else:
            print("\033[31mCommande non valide. Vérifiez que votre saisie est de la forme e7a6 puis réessayez\033[0m")
            sleep(2)
# =============================================================================
# Programme principal du jeux d'echec
# =============================================================================

if __name__ == '__main__':
    # Afichage du titre du jeux
    print('=============================================================================')
    print("                            Jeux d'echecs")
    print('=============================================================================')
    Menu = True
    while Menu:
        # Affichage du Menu du jeux
        print('=============================================================================')
        print("                                 Menu")
        print('=============================================================================')
        print("\nEntrer \033[31m1v1\033[0m pour jouer contre un humain et \033[31mia\033[0m pour jouer contre l'ordinateur.\nPour quitter, entrer \033[31mexit\033[0m.")
        choix = input("Choix du mode de jeu : ")# Recuperation du choix du joueur
        ech = Echiquier()  # créaction de l'échiquier en état initial
# =============================================================================
# Mode Joueur contre Joueur
# =============================================================================
        if choix == "1v1":
            # Au début de la partie, aucun roi n'est en échec donc echecEtMAt= False et echec =False
            EchecEtMat = False
            echec = False

            while EchecEtMat == False or EchecEtMat== None:

                ech.__str__()  # Fonction d'affichage
                # table de fin de jeux (syzygy)
                valeurEchec = ech.echecEtMat()
                if valeurEchec in [1, 2]:
                    finPartie()
                if valeurEchec in [-1, -2]:
                    ech.changementDeCouleur()
                    finPartie()
                #lancement de l'interface homme machine
                EchecEtMat = jeuxJoueur(EchecEtMat,ech)
            # fin de jeux: Annonce du gagnant
            ech.changementDeCouleur()
            finPartie()


# =============================================================================
# Mode joueur contre IA
# =============================================================================
        elif choix == "ia":
            # Au début de la partie, aucun roi n'est en échec donc echecEtMAt= False et echec =False
            EchecEtMat = False
            echec = False
            ia = IA()
            iaBooleen=True#defini si le mode ia est choisi
            while EchecEtMat==False or EchecEtMat==None :
                # Affichage de l'echiquier
                ech.__str__()
                # Table de fin de jeux (syzygy)
                valeurEchec = ech.echecEtMat()
                if valeurEchec in [1, 2]:
                    print('les' + str(ech.tourJoueur) + 'ont gagnée')
                if valeurEchec in [-1, -2]:
                    ech.changementDeCouleur()
                    print('les' + str(ech.tourJoueur) + 'ont gagnée')
                    
                if ech.get_TourJoueur() == 'blanc':# Aux joueur de jouer
                    EchecEtMat = jeuxJoueur(EchecEtMat,ech,iaBooleen)

                else:# A L'IA de jouer
                    hist = ech.get_historique()# Recuperation de l'historique
                    # Bibliotheque d'ouverture
                    if ia.ouverture(hist) != None:# Mouvement d'ouverture de l'IA
                        mouvement = str(ia.ouverture(hist))
                        # Affichage du mouvement jouer par L'IA
                        print("\nL'IA joue le mouvement :", mouvement)
                        ech.deplacer(mouvement[:2], mouvement[2:])# Deplacement du mouvement choisi par L'IA
                    # Suite du jeu
                    elif ech.VerificationEchecEtMat()==False:# Mouvement de l'IA par la fonction d'évaluation
                        mouvement = ia.middlegame(hist, ech)
                        # Affichage du mouvement jouer par L'IA
                        print("\nL'IA joue le mouvement :", mouvement)
                        ech.deplacer(mouvement[:2], mouvement[2:])# Deplacement du mouvement choisi par L'IA
                    # Verification de l'echec et mat
                    EchecEtMat=ech.VerificationEchecEtMat()
            # fin de jeux: Annonce du gagnant
            ech.changementDeCouleur()
            finPartie()
            
        elif choix == 'exit':
            #sorti de la boucle 
            Menu = False
        else:
            # Affichage d'erreur
            print("\033[31mCommande non valide. Vous devez écrire 1v1, ia ou exit\033[0m")
            sleep(2)
