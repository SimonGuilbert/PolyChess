# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:08:54 2019

@author: guillyd
"""

class Piece:
    
    def __init__(self,nom,couleur):
        '''
        Une piece a un nom et une couleur.
        cimetiere correspond aux pieces eliminees
        '''
        self.cimetiere = []
        self.nom = nom
        self.couleur = couleur
        
    tab120 = (
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
    -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
    -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
    -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
    -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
    -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
    -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
    -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
    )

    tab64 = (
    21, 22, 23, 24, 25, 26, 27, 28,
    31, 32, 33, 34, 35, 36, 37, 38,
    41, 42, 43, 44, 45, 46, 47, 48,
    51, 52, 53, 54, 55, 56, 57, 58,
    61, 62, 63, 64, 65, 66, 67, 68,
    71, 72, 73, 74, 75, 76, 77, 78,
    81, 82, 83, 84, 85, 86, 87, 88,
    91, 92, 93, 94, 95, 96, 97, 98
    )        
       
    
    def mvmt_pion(self):
        '''
        Le pion peut potentiellemnt avancer de une ou deux cases devant lui au debout puis seulement une
        ou manger une piece ennemie à gauche ou à droite en diagonale
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        ligne = echequier.get_ligne()
        #Recuperation de la position de pion
        position = self.echequier.get_position()
        #Numero du tour (initial=1) DOit etre recuperer
        nb_tours= 1
        #Initialisation de la liste des positions
        position_possible=[]
        # Pion Blanc
        if self.couleur == 'blanc':
            if nb_tours == 1:
                position_possible += [position-2*ligne,position-ligne,position-ligne+1,position-ligne-1]
            else:
                position_possible += [position-ligne,position-ligne+1,position-ligne-1]
        #Pion noir
        if self.couleur == 'noir':
            if nb_tours == 1:
                position_possible += [position+2*ligne,position+ligne,position+ligne+1,position+ligne-1]
            else:
                position_possible += [position+ligne,position+ligne+1,position+ligne-1]
        return position_possible    

    def mvmt_roi(self):
        '''
        Le roi peut potentiellemnt avancer d'une case autout de lui-meme
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        ligne = echequier.get_ligne()
        #Recuperation de la position de pion
        position = self.echequier.get_position()
        #Creation de la liste des positions possibles
        position_possible=[position-k*ligne-i for k in range(3) for i in range (3)]
        return position_possible
            
    def mvmt_cavalier(self):
        '''
        Le cavalier se deplace de deux cases devant, derriere ou sur les cotes puis une case a droite ou gauche
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        ligne = echequier.get_ligne()
        #Recuperation de la position de pion
        position = self.echequier.get_position()
        #Creation de la liste des positions possibles
        position_possible=[position-k*ligne-i for k in [-2,2] for i in [-1,1]] + [position-m*ligne-l for m in [-1,1] for l in [-2,2]]
        return position_possible
