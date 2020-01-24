# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:43:15 2019

@author: Jonathan Molieres
"""
from piece import Piece
import chess 
import chess.syzygy



# =============================================================================
# Classe de l'echiquier avec les regles associees 
# =============================================================================
class Echiquier:
    '''classe qui represente l'echiquier de norme 8 x 8 avec son moteur pour les coups '''
    # Constructeur
    def __init__(self):
        
        
        # Coordonnees de chaque case de l'echiquier
        self.coordonnees=[
        'a8','b8','c8','d8','e8','f8','g8','h8',
        'a7','b7','c7','d7','e7','f7','g7','h7',
        'a6','b6','c6','d6','e6','f6','g6','h6',
        'a5','b5','c5','d5','e5','f5','g5','h5',
        'a4','b4','c4','d4','e4','f4','g4','h4',
        'a3','b3','c3','d3','e3','f3','g3','h3',
        'a2','b2','c2','d2','e2','f2','g2','h2',
        'a1','b1','c1','d1','e1','f1','g1','h1',
        ]
        
        # Position initiale des pièces sur l'echiquier
        self.echiquier = [
        Piece('TOUR','noir'),Piece('CAVALIER','noir'),Piece('FOU','noir'),Piece('DAME','noir'),Piece('ROI','noir'),Piece('FOU','noir'),Piece('CAVALIER','noir'),Piece('TOUR','noir'),
        Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
        Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
        Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
        Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
        Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
        Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
        Piece('TOUR','blanc'),Piece('CAVALIER','blanc'),Piece('FOU','blanc'),Piece('DAME','blanc'),Piece('ROI','blanc'),Piece('FOU','blanc'),Piece('CAVALIER','blanc'),Piece('TOUR','blanc')
        ]

        for i in self.echiquier:
            i.impEchiquier(self)
        # Matrice d'affichage
        self.jeux=['--' for i in range(8*8) ] 
        # Variable qui determine les tours de jeux
        self.tourJoueur='blanc'
        # Variable qui repertorie tout les coups joues
        self.historique=[]
        self.cimetiereBlanc=[]
        self.cimetiereNoir=[]
        # Defini les mouvements possible pour chaque pion
        self.mvtPossible()
# =============================================================================
# getter
# =============================================================================
    def get_echiquier(self):
        '''retourne l'echiquier'''
        return self.echiquier
    def get_historique(self):
        '''retourne l'historique'''
        return self.historique
    def get_TourJoueur(self):
        '''retourne la couleur du joueur à jouer'''
        return self.tourJoueur
    
    def nbre(self):
        '''renvoie le nombre de piéce restant sur l'échiquier'''
        return 32 -(len(self.cimetiereBlanc)+len(self.cimetiereNoir))
# =============================================================================
# Fonction de conversion 
# =============================================================================
    def conversionEnIndex(self,position): 
        '''
        passer de coordonnees en index 
        ex: a8 =>0
        '''
        return self.coordonnees.index(position)  
    
    def conversionEnCoord(self,index):
        '''
        passer de index a coordonnes
        ex: 0 => a8
        '''
        return self.coordonnees[index]
    
    def changementDeCouleur(self):
        '''Fonction de changement de couleur'''
        if self.tourJoueur=='blanc':
            self.tourJoueur='noir'
        else:
            self.tourJoueur= 'blanc'
# =============================================================================
# Fonction de recherche 
# =============================================================================
    def estVide(self,iPos):
        ''' verifie si il existe une piece a l'indice iPos'''
        return self.echiquier[iPos].getNom() ==''
    
    def rechercheRoi(self,nom,couleur):
        '''renvoie l'indice du roi voulut'''
        for i  in range(len(self.echiquier)):
                if self.echiquier[i].getCouleur()==couleur and self.echiquier[i].getNom()==nom:
                    return i
# =============================================================================
# Fonction d'affichage        
# =============================================================================
    def matriceJeux(self):
        '''remplissage de la matrice d 'affichage'''
        for index in range(len(self.echiquier)):
            if self.echiquier[index].getNom()=='TOUR':
                self.jeux[index]='T'+ self.echiquier[index].getCouleur()[0]
            elif self.echiquier[index].getNom()=='PION':
                self.jeux[index]='P'+ self.echiquier[index].getCouleur()[0]
            elif self.echiquier[index].getNom()=='FOU':
                self.jeux[index]='F'+ self.echiquier[index].getCouleur()[0]
            elif self.echiquier[index].getNom()=='CAVALIER':
                self.jeux[index]='C'+ self.echiquier[index].getCouleur()[0]
            elif self.echiquier[index].getNom()=='DAME':
                self.jeux[index]='D'+ self.echiquier[index].getCouleur()[0]
            elif self.echiquier[index].getNom()=='ROI':
                self.jeux[index]='R'+ self.echiquier[index].getCouleur()[0]
            elif self.echiquier[index].getNom()=='':
                self.jeux[index]='--'
    def affichageCimetiere(self,cimetiere):
        AffCimetiere = ''
        for k in cimetiere:
            AffCimetiere += k.getNom()[0]+k.getCouleur()[0]+' '
            if len(AffCimetiere) == 78:
                AffCimetiere += '\n'
        return AffCimetiere
    
    def __str__(self):
        ''' fonction d'affichage du jeux d'echec '''
        affichage=''
        self.matriceJeux() 
        affichage+='\n'+'cimetière Blanc'+'\n'
        affichage+=self.affichageCimetiere(self.cimetiereBlanc)+'\n'
        affichage+='   a  b  c  d  e  f  g  h'+'\n'
        affichage+='  -----------------------'+'\n'
        compteur=8
        for index in range(len(self.jeux)):
            if affichage[-1]=='\n':
                affichage+=str(compteur)
        
            affichage+='|'+str(self.jeux[index])

            if self.coordonnees[index][0]=='h':
                affichage+='|'+str(compteur)+'\n'
                compteur-=1
        affichage+='  -----------------------'+'\n'
        affichage+='   a  b  c  d  e  f  g  h'+'\n'
        affichage+='cimetière Noir'+'\n'
        affichage+=self.affichageCimetiere(self.cimetiereNoir)+'\n'
        print(affichage)
        
    def affichageHistorique(self):
        '''Permet d'afficher l'historique'''
        affHist=str()
        for k in self.historique:
            affHist+=str(k[0])+str(k[1])
            affHist+=' | '
        print(affHist)
# =============================================================================
# Fonction de deplacement
# =============================================================================
    def deplacer(self,posInitial,posNouvelle):
        '''fonction qui permet de deplacer un pion si les regles sont valides'''
        iPosInitial=self.conversionEnIndex(posInitial)# conversion des coordonnees en index 
        iPosNouvelle=self.conversionEnIndex(posNouvelle)# conversion des coordonnees en index 
        #teste de du placement 
        if self.regleSimple(iPosInitial,iPosNouvelle) and self.tourJoueur==self.echiquier[iPosInitial].getCouleur():
            # Ajout au cimetiere si besion 
            if self.echiquier[iPosNouvelle].getNom()!='':
                if self.echiquier[iPosNouvelle].getCouleur()=='blanc':
                    self.cimetiereBlanc.append(self.echiquier[iPosNouvelle])
                else:
                    self.cimetiereNoir.append(self.echiquier[iPosNouvelle])
            # Deplacement des pieces
            self.echiquier[iPosNouvelle]=self.echiquier[iPosInitial]
            self.echiquier[iPosInitial]=Piece()
            # Ajout a l'historique
            self.historique.append([posInitial,posNouvelle])
            if self.echiquier[iPosNouvelle].getNom()=='PION':
                self.echiquier[iPosNouvelle].changementDeTour()
            
            self.changementDeCouleur()
            # defini les mouvements possibles pour chaque piece
            self.mvtPossible()
            
            
    def testeDeplacer(self,posInitial,posNouvelle):
        '''Verification des deplacements possibles '''
        iPosInitial=self.conversionEnIndex(posInitial)# conversion des coordonnees en index 
        iPosNouvelle=self.conversionEnIndex(posNouvelle)# conversion des coordonnees en index 
      
        return self.regleSimple(iPosInitial,iPosNouvelle) and self.tourJoueur==self.echiquier[iPosInitial].getCouleur()
            
# =============================================================================
# Fonctions de Verification des coups (moteur)
# =============================================================================
    def regleSimple(self,iPosInitial,iPosNouvelle):
        '''definie les coups licites sur les deplacements possibles des pieces  '''
        piece=self.echiquier[iPosInitial]
        # on ne peut pas manger ses propres pieces
        if self.echiquier[iPosNouvelle].getCouleur()==self.echiquier[iPosInitial].getCouleur():
            return False
        # verfication du coup joue par rapport a tous les coups possibles de la piece
        return iPosNouvelle in piece.Lposition
    
# =============================================================================
# Coups spéciaux
# =============================================================================
    def promotion(self,position):
        '''Fonction permetant la promotion d'un pion en demandant la piece voulue'''
        self.changementDeCouleur()
        # Demande du choix de la piece
        promo= input('Promotion! Veuillez choisir une piece(fou, dame, cavalier,tour):')
        promoUpp=promo.upper()
        if promoUpp in ['FOU','DAME','CAVALIER','TOUR']:#verification du caractere entrant
            #creation de la piece
            self.echiquier[position]=Piece(promoUpp,self.tourJoueur)   
            self.echiquier[position].impEchiquier(self)
        self.changementDeCouleur()
        
    def roque(self,positionTour):
        '''fonction permetant de roquer en testant les quatres positions possibles'''
        iPositionTour=self.conversionEnIndex(positionTour)
        if self.echiquier[60].getNom()=='ROI' and self.echiquier[60].getCouleur()=='blanc':
            if self.tourJoueur == 'blanc' and self.estVide(61) and self.estVide(62) and iPositionTour==63:
                # modification de l'echiquier pour le roque
                self.echiquier[62]=self.echiquier[60]
                self.echiquier[61]=self.echiquier[63]
                self.echiquier[63]=Piece()
                self.echiquier[60]=Piece()
            elif self.tourJoueur == 'blanc' and self.estVide(59) and self.estVide(58) and self.estVide(57) and iPositionTour==56:
                # modification de l'echiquier pour le roque
                self.echiquier[59]=self.echiquier[56]
                self.echiquier[58]=self.echiquier[60]
                self.echiquier[57]=Piece()
                self.echiquier[56]=Piece()
                self.echiquier[60]=Piece()
        if self.echiquier[4].getNom()=='ROI' and self.echiquier[4].getCouleur()=='noir':    
            if self.tourJoueur == 'noir' and self.estVide(6) and self.estVide(5) and iPositionTour==7:
                # modification de l'echiquier pour le roque
                self.echiquier[5]=self.echiquier[7]
                self.echiquier[6]=self.echiquier[4]
                self.echiquier[7]=Piece()
                self.echiquier[4]=Piece()
            
            elif self.tourJoueur == 'noir' and self.estVide(1) and self.estVide(2) and self.estVide(3) and iPositionTour==0:
                # modification de l'echiquier pour le roque
                self.echiquier[3]=self.echiquier[0]
                self.echiquier[2]=self.echiquier[4]
                self.echiquier[4]=Piece()
                self.echiquier[0]=Piece()
    def TesteRoque(self,positionTour):
        '''Fonction qui teste la possibilite de roquer'''
        iPositionTour=self.conversionEnIndex(positionTour)
        if self.echiquier[60].getNom()=='ROI' and self.echiquier[60].getCouleur()=='blanc':
            if self.tourJoueur == 'blanc' and self.estVide(61) and self.estVide(62) and iPositionTour==63:
                return (True,'blanc')
            elif self.tourJoueur == 'blanc' and self.estVide(59) and self.estVide(58) and self.estVide(57) and iPositionTour==56:
                return (True,'blanc')
        if self.echiquier[4].getNom()=='ROI' and self.echiquier[4].getCouleur()=='noir':     
            if self.tourJoueur == 'noir' and self.estVide(6) and self.estVide(5) and iPositionTour==7:
                return (True,'noir')
            elif self.tourJoueur == 'noir' and self.estVide(1) and self.estVide(2) and self.estVide(3) and iPositionTour==0:
                return (True,'noir') 
            
        return (False,None)
# =============================================================================
# Echec
# =============================================================================
    def echec(self):
        '''recherche de mise en echec. Renvoie un booleen et la couleur qui est en echec '''     
        IRoiNoir= self.rechercheRoi('ROI','noir')#position du roi noir
        ListeBlanc= self.coupsPossibleBlanc()#liste des coups possibles pour les blancs
        if IRoiNoir in ListeBlanc:
            return (True,'noir') #si le roi est mangeable alors on est en echec
        IRoiBlanc= self.rechercheRoi('ROI','blanc')#position du roi blanc
        ListeNoir= self.coupsPossibleNoir()#liste des coups possibles pour les noirs
        if IRoiBlanc in ListeNoir:
            return (True,'blanc')#si le roi est mangeable alors on est en echec
        return (False,None)
       
# =============================================================================
#  Echec Et Mat       
# =============================================================================
            
    def VerificationEchecEtMat(self):
        '''verification des Echec et Mat renvoie un booleen
            Pour chaque coup possible, on teste le cas de l'echec sur un echiquier 
        
        '''
        for i in range(len(self.echiquier)):
            for coup in self.echiquier[i].Lposition:
            
                board=Echiquier()
                for h in self.get_historique():
                    board.deplacer(h[0],h[1]) 
                board.deplacer(self.conversionEnCoord(i),self.conversionEnCoord(coup))
                if board.echec()!=(True,self.tourJoueur):
                    return False
                    
        return True
    
    def changementDeEchiquier(self):
        '''Permet de changement de forme d'echiquer entre ce qu'on a fait et la bibliothéque chess pour utiliser syzygy  '''
        strEchiquierFinal=''
        compteurSlash=0#pour savoir quand ajouter les slashs
        compteurVide=0
        
        for i in range(len(self.echiquier)):
            strEchiquier=''
            
            if compteurSlash==8:# un slash pour derterminer les sauts de ligne dans l'echiquier
                compteurSlash=0
        
                strEchiquier+=str(compteurVide)+'/'
                compteurVide=0
            # cas de la case vide 
            if self.echiquier[i].getNom()=='':
                compteurVide+=1
            #TOUR
            if self.echiquier[i].getNom()=='TOUR':
                if compteurVide!=0:
                    strEchiquier+=str(compteurVide)
                    compteurVide=0
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='R'
                    else:
                        strEchiquier+='r'
                else:
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='R'
                    else:
                        strEchiquier+='r'
            #DAME            
            if self.echiquier[i].getNom()=='DAME':
                if compteurVide!=0:
                    strEchiquier+=str(compteurVide)
                    compteurVide=0
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='Q'
                    else:
                        strEchiquier+='q'
                else:
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='Q'
                    else:
                        strEchiquier+='Q'      
            #FOU    
            if self.echiquier[i].getNom()=='FOU':
                if compteurVide!=0:
                    strEchiquier+=str(compteurVide)
                    compteurVide=0
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='B'
                    else:
                        strEchiquier+='b'
                else:
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='B'
                    else:
                        strEchiquier+='b'
            #ROI       
            if self.echiquier[i].getNom()=='ROI':
                
                if compteurVide!=0:
                    strEchiquier+=str(compteurVide)
                    compteurVide=0
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='K'
                    else:
                        strEchiquier+='k'
                else:
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='K'
                    else:
                        strEchiquier+='k'        
            
            #PION
            if self.echiquier[i].getNom()=='PION':
                if compteurVide!=0:
                    strEchiquier+=str(compteurVide)
                    compteurVide=0
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='P'
                    else:
                        strEchiquier+='p'
                else:
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='P'
                    else:
                        strEchiquier+='p'
                        
            #CAVALIER
            if self.echiquier[i].getNom()=='CAVALIER':
                if compteurVide!=0:
                    strEchiquier+=str(compteurVide)
                    compteurVide=0
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='N'
                    else:
                        strEchiquier+='n'
                else:
                    if self.echiquier[i].getCouleur()=='blanc':
                        strEchiquier+='N'
                    else:
                        strEchiquier+='n'
            compteurSlash+=1            
            strEchiquierFinal+=strEchiquier
            strEchiquier=''
        #ajout de la couleur du joueur ( w=white and b= black )
        if self.tourJoueur=='blanc':
            strEchiquierFinal+=' w'
        else:
            strEchiquierFinal+=' b'
        return strEchiquierFinal
        
               
    def echecEtMat(self):
        '''Avec la table de fin de jeux'''
        if self.nbre() in [i for i in range(4)]:#sysygy commence seulement si il y a pas de plus de 3 pieces sur le terrain
            strEchiquier=self.changementDeEchiquier()#conversion de l'echiquier
            #utilisation de la librairie
            tablebase = chess.syzygy.open_tablebase("regular")
            with chess.syzygy.open_tablebase("regular") as tablebase:
                board = chess.Board(strEchiquier)
                valeur=tablebase.probe_wdl(board)
                return valeur
        else:
            return 0
# =============================================================================
# Mise a jour des deplacements possibles
# =============================================================================  
    def mvtPossible(self):
        '''fonction pour actualiser tout les coups possibles des pieces en modifiant la variable de la classe piece'''
        for i  in range(len(self.echiquier)):
            # verfication du coup joue par rapport a tous les coups possibles de la piece
            # en l'assignant a la Liste de la piece
            if self.echiquier[i].getNom()=='TOUR':
                self.echiquier[i].MAJPosition(self.echiquier[i].mvmt_tour(i))
            if self.echiquier[i].getNom()=='PION':
                self.echiquier[i].MAJPosition(self.echiquier[i].mvmt_pion(i))
            if self.echiquier[i].getNom()=='CAVALIER':
                self.echiquier[i].MAJPosition(self.echiquier[i].mvmt_cavalier(i))
            if self.echiquier[i].getNom()=='ROI':
                self.echiquier[i].MAJPosition(self.echiquier[i].mvmt_roi(i))
            if self.echiquier[i].getNom()=='FOU':
                self.echiquier[i].MAJPosition(self.echiquier[i].mvmt_fou(i))
            if self.echiquier[i].getNom()=='DAME':
                self.echiquier[i].MAJPosition(self.echiquier[i].mvmt_dame(i))
                
# =============================================================================
# reécuperation des listes des coups possibles
# =============================================================================
    def coupsPossibleBlanc(self):
        '''Permet de recuperer la liste de tout les coups possible du joueur avec les pieces blancs '''
        LcoupsPossibleBlanc=[]
        for i in self.echiquier:
            if i.getCouleur()=='blanc':
                LcoupsPossibleBlanc+=i.Lposition
        return LcoupsPossibleBlanc

    def coupsPossibleNoir(self):
        '''Permet de recuperer la liste de tout les coups possible du joueur avec les pieces noirs'''
        coupsPossibleNoir=[]
        for i in self.echiquier:
            if i.getCouleur()=='noir':
                coupsPossibleNoir+=i.Lposition
        return coupsPossibleNoir


