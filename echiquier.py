# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:58:02 2019

@author: guilbers
"""

class Echiquier8x8:
    # Constructor
    def __init__(self):
        pass

    # Coordonnees de chaque case de l'echiquier
    coordonnees = [
        'a8','b8','c8','d8','e8','f8','g8','h8',
        'a7','b7','c7','d7','e7','f7','g7','h7',
        'a6','b6','c6','d6','e6','f6','g6','h6',
        'a5','b5','c5','d5','e5','f5','g5','h5',
        'a4','b4','c4','d4','e4','f4','g4','h4',
        'a3','b3','c3','d3','e3','f3','g3','h3',
        'a2','b2','c2','d2','e2','f2','g2','h2',
        'a1','b1','c1','d1','e1','f1','g1','h1',
        ]    
    
    def debutPartie(self):
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
    
