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
        # Matrice d'affichage
        self.jeux=['--' for i in range(8*8) ] 
        # Variable qui determine les tours de jeux
        self.tourJoueur='blanc'
        # Variable qui repertorie tout les coups joues
        
        self.historique=[]
        
        
    def conversionEnIndex(self,position): 
        '''passer de coordonnees en index'''
        return self.coordonnees.index(position)
#    def pieceDeIndex(self,piece):
#        '''passer de la piece  a l'index'''
#        return self.echiquier.index(piece)
    
    
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
        '''fonction d'affichage du jeux d'echec  '''
        
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
        
        
    def affichageHistorique(self):
        affHist=str()
      
        for k in self.historique:
            affHist+=str(k[0])+str(k[1])
            affHist+=' | '
        print(affHist)
        
#    def vide(self,index):
#        return self.echiquier[index].getCouleur()==''
    def deplacer(self,posInitial,posNouvelle):
        iPosInitial=self.conversionEnIndex(posInitial)
        iPosNouvelle=self.conversionEnIndex(posNouvelle)
        if self.regleSimple(iPosInitial,iPosNouvelle):
            
            self.echiquier[iPosNouvelle]=self.echiquier[iPosInitial]
            self.echiquier[iPosInitial]=Piece()
            self.historique.append([posInitial,posNouvelle])
         
        
        else:
            print("Le coup n'est pas possible")
            sleep(2)

# =============================================================================
# Mise en place des regles : 
# =============================================================================
    def regleSimple(self,iPosInitial,iPosNouvelle):
        '''definie les coups non licites simple '''
        piece=self.echiquier[iPosInitial]
        
        #on ne peut pas manger ses propres pieces
        
        if self.echiquier[iPosNouvelle].getCouleur()==self.echiquier[iPosInitial].getCouleur():
            return False
        
        # verfication du coup joue par rapport a tous les coups possibles de la piece
        if piece.getNom()=='TOUR':
            return iPosNouvelle in piece.mvmt_tour(iPosInitial)
        if piece.getNom()=='pion':
            return iPosNouvelle in piece.mvmt_pion(iPosInitial)
        if piece.getNom()=='CAVALIER':
            return iPosNouvelle in piece.mvmt_cavalier(iPosInitial)
        if piece.getNom()=='ROI':
            return iPosNouvelle in piece.mvmt_roi(iPosInitial)
     
        return True
            
#if __name__ == "__main__":  
#         
#    echiquier = Echiquier8x8()
#    
#    echiquier.__str__()
   
