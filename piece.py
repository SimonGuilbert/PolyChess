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
