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