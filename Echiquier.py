# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:43:15 2019

@author: Jonathan Molieres
"""

from time import sleep #permet d'attendre la lecture au joueur en cas d'une erreur de coups 
from piece import Piece



# =============================================================================
# Classe de l'echiquier avec les regles associees 
# =============================================================================
class Echiquier8x8:
    '''classe qui represente l'echiquier de norme 8 x 8 '''
    # Constructor
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
            
            
        for i  in range(len( self.echiquier)):    
            
            positionPossible=[]
            # verfication du coup joue par rapport a tous les coups possibles de la piece
            if self.echiquier[i].getNom()=='TOUR':
                positionPossible+=self.echiquier[i].mvmt_tour(i)
            if self.echiquier[i].getNom()=='pion':
                 positionPossible+=self.echiquier[i].mvmt_pion(i)
            if self.echiquier[i].getNom()=='CAVALIER':
                positionPossible+=self.echiquier[i].mvmt_cavalier(i)
            if self.echiquier[i].getNom()=='ROI':
                positionPossible+=self.echiquier[i].mvmt_roi(i)
            if self.echiquier[i].getNom()=='FOU':
                positionPossible+=self.echiquier[i].mvmt_fou(i)
            if self.echiquier[i].getNom()=='DAME':
                positionPossible+=self.echiquier[i].mvmt_dame(i)
        self.echiquier[i].position=positionPossible
        
        
        # Matrice d'affichage
        self.jeux=['--' for i in range(8*8) ] 
        # Variable qui determine les tours de jeux
        self.tourJoueur='blanc'
        # Variable qui repertorie tout les coups joues
        
        self.historique=[]
        self.cimetiereBlanc=[]
        self.cimetiereNoir=[]
        
    def conversionEnIndex(self,position): 
        '''passer de coordonnees en index'''
        return self.coordonnees.index(position)
#    def pieceDeIndex(self,piece):
#        '''passer de la piece  a l'index'''
#        return self.echiquier.index(piece)
    
    def changementDeCouleur(self):
        print(self.tourJoueur)
        if self.tourJoueur=='blanc':
            self.tourJoueur='noir'
        else:
            self.tourJoueur= 'blanc'
        print(self.tourJoueur)
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
        
    def __str__(self):
        ''' fonction d'affichage du jeux d'echec '''
        
        self.matriceJeux()  
        affichage='   a  b  c  d  e  f  g  h'+'\n'
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
        affichage+='   a  b  c  d  e  f  g  h'
        print(affichage)
    
    def estVide(self,iPos):
        ''' verifie si il existe une piece a l'indice iPos'''
        return self.echiquier[iPos].getNom() =='' 
    def get_echiquier(self):
        return self.echiquier
        
    def affichageHistorique(self):
        affHist=str()
      
        for k in self.historique:
            affHist+=str(k[0])+str(k[1])
            affHist+=' | '
        print(affHist)
        

    def deplacer(self,posInitial,posNouvelle):
        
        iPosInitial=self.conversionEnIndex(posInitial)
        iPosNouvelle=self.conversionEnIndex(posNouvelle)
        if self.regleSimple(iPosInitial,iPosNouvelle) and self.tourJoueur==self.echiquier[iPosInitial].getCouleur():
            
            self.echiquier[iPosNouvelle]=self.echiquier[iPosInitial]
            self.echiquier[iPosInitial]=Piece()
            self.historique.append([posInitial,posNouvelle])
            positionPossible=[]
            if self.echiquier[iPosNouvelle].getNom()=='TOUR':
                positionPossible=self.echiquier[iPosNouvelle].mvmt_tour(iPosNouvelle)
            elif self.echiquier[iPosNouvelle].getNom()=='PION':
                 positionPossible+=self.echiquier[iPosNouvelle].mvmt_pion(iPosNouvelle)
                 if posNouvelle in [i for i in range(8)] or posNouvelle in [i for i in range(56,64)]:#verifiaction si il y a promotion
                    self.promotion(posNouvelle) 
            elif self.echiquier[iPosNouvelle].getNom()=='CAVALIER':
                positionPossible=self.echiquier[iPosNouvelle].mvmt_cavalier(iPosNouvelle)
            elif self.echiquier[iPosNouvelle].getNom()=='ROI':
                positionPossible=self.echiquier[iPosNouvelle].mvmt_roi(iPosNouvelle)
            elif self.echiquier[iPosNouvelle].getNom()=='FOU':
                positionPossible=self.echiquier[iPosNouvelle].mvmt_fou(iPosNouvelle)
            elif self.echiquier[iPosNouvelle].getNom()=='DAME':
                positionPossible=self.echiquier[iPosNouvelle].mvmt_dame(iPosNouvelle)
            self.echiquier[iPosNouvelle].position=positionPossible

            if not self.estVide(iPosNouvelle):
                if self.echiquier[iPosNouvelle].getNom()[1]=='b':
                    self.cimetiereBlanc.append(self.echiquier[iPosNouvelle])
                else:
                    self.cimetiereNoir.append(self.echiquier[iPosNouvelle])
            self.changementDeCouleur()
        else:
            
            print("\n\033[31mLe coup n'est pas possible. Réessayez\033[0m")

            sleep(2)

# =============================================================================
# Mise en place des regles : 
# =============================================================================
    def regleSimple(self,iPosInitial,iPosNouvelle):
        '''definie les coups licites sur les deplacements possibles des pieces '''
        piece=self.echiquier[iPosInitial]
        
        #on ne peut pas manger ses propres pieces
        
        if self.echiquier[iPosNouvelle].getCouleur()==self.echiquier[iPosInitial].getCouleur():
            return False
        
        # verfication du coup joue par rapport a tous les coups possibles de la piece
        if piece.getNom()=='TOUR':
            return iPosNouvelle in piece.mvmt_tour(iPosInitial)
        if piece.getNom()=='PION':
            return iPosNouvelle in piece.mvmt_pion(iPosInitial)
        if piece.getNom()=='CAVALIER':
            return iPosNouvelle in piece.mvmt_cavalier(iPosInitial)
        if piece.getNom()=='ROI':
            return iPosNouvelle in piece.mvmt_roi(iPosInitial)
        if piece.getNom()=='FOU':
            return iPosNouvelle in piece.mvmt_fou(iPosInitial)
        if piece.getNom()=='DAME':
            return iPosNouvelle in piece.mvmt_dame(iPosInitial)
        if self.estVide(iPosInitial):
            return False
        return True
    
    def coupsPossibleBlanc(self):
        #Permet de recuperer la liste de tout les coups possible du joueur avec les pieces blanc 
        LcoupsPossibleBlanc=[]
        for i in self.echiquier:
            if i.getCouleur()=='blanc':
                LcoupsPossibleBlanc+=i.position
        return LcoupsPossibleBlanc

    def coupsPossibleNoir(self):
        #Permet de recuperer la liste de tout les coups possible du joueur avec les pieces noir 

        coupsPossibleNoir=[]
        for i in self.echiquier:
            if i.getCouleur()=='noir':
                coupsPossibleNoir+=i.position
        return coupsPossibleNoir

# =============================================================================
# Echec Et echec et mat
# =============================================================================
#    def changementDeEchiquier(self):
#        
#    def echecEtMat(self):
#        tablebase = chess.syzygy.open_tablebase("data/syzygy/regular")
#        with chess.syzygy.open_tablebase("data/syzygy/regular") as tablebase:
#            board = chess.Board("8/2K5/4B/3N4/8/8/4k3/8 b - - 0 1")
#           
#            print(tablebase.probe_wdl(board))
            
    def echec(self):
        
        if self.tourJoueur=='blanc':
            ListeCoupsRoiNoir=[]
            for piece in self.echiquier:
                if piece.getCouleur()=='noir' and piece.getNom()=='ROI':
                    ListeCoupsRoiNoir=piece.position
                    break
                print(ListeCoupsRoiNoir)
            if ListeCoupsRoiNoir!=[]:
                ListeBlanc=self.coupsPossibleBlanc()
                for i in ListeBlanc:
                    if i in ListeCoupsRoiNoir:
                        ListeCoupsRoiNoir.remove(i)
                    return len(ListeCoupsRoiNoir)
        else:
            ListeCoupsRoiBlanc=[]
            for piece in self.echiquier:
                if piece.getCouleur()=='blanc' and piece.getNom()=='ROI':
                    ListeCoupsRoiBlanc=piece.position
            ListeNoir=self.coupsPossibleNoir()
            if ListeCoupsRoiBlanc!=[]:
                for i in ListeNoir:
                    if i in ListeCoupsRoiBlanc:
                        ListeCoupsRoiBlanc.remove(i)
                return len(ListeCoupsRoiBlanc)
        return -1


# =============================================================================
# Coups spéciaux
# =============================================================================
    def promotion(self,position):
        
        promo= input('Promotion!! Veuillez choisir une piece.')
        self.echiquier[position]=Piece(promo.upper(), self.tourJoueur)    
        
        
    
    def roque(self,positionTour):
        iPositionTour=self.conversionEnIndex(positionTour)
        if self.tourJoueur == 'blanc' and self.estVide(61) and self.estVide(62) and iPositionTour==63:
            
            self.echiquier[62]=self.echiquier[60]
            self.echiquier[61]=self.echiquier[63]
            self.echiquier[63]=Piece()
            self.echiquier[60]=Piece()
        elif self.tourJoueur == 'blanc' and self.estVide(59) and self.estVide(58) and self.estVide(57) and iPositionTour==56:
            
            self.echiquier[59]=self.echiquier[56]
            self.echiquier[63]=self.echiquier[60]
            self.echiquier[60]=Piece()
            self.echiquier[56]=Piece()
            
        elif self.tourJoueur == 'noir' and self.estVide(6) and self.estVide(5) and iPositionTour==7:
            
            self.echiquier[5]=self.echiquier[7]
            self.echiquier[6]=self.echiquier[4]
            self.echiquier[7]=Piece()
            self.echiquier[4]=Piece()
        
        elif self.tourJoueur == 'noir' and self.estVide(1) and self.estVide(2) and self.estVide(3) and iPositionTour==0:
            self.echiquier[3]=self.echiquier[0]
            self.echiquier[2]=self.echiquier[4]
            self.echiquier[4]=Piece()
            self.echiquier[0]=Piece()
        else :
            print("\033[31mCommande non valide. Veuillez Recommencer\033[0m")
        
        
        
        

        
        