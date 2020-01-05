# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:08:54 2019

@author: guillyd
"""


#On suppose que la configuration de l'echiquier est 8x8
#On utilise ici que les index

class Piece:
    
    def __init__(self,nom='',couleur=''):
        '''
        Une piece a un nom et une couleur.
        cimetiere correspond aux pieces eliminees
        '''
        
        self.nom = nom
        self.couleur = couleur
        self.cimetiere = []
        
        
        self.tab120 = (
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

        self.tab64 = (
        21, 22, 23, 24, 25, 26, 27, 28,
        31, 32, 33, 34, 35, 36, 37, 38,
        41, 42,  43, 44, 45, 46, 47, 48,
        51, 52, 53, 54, 55, 56, 57, 58,
        61, 62, 63, 64, 65, 66, 67, 68,
        71, 72, 73, 74, 75, 76, 77, 78,
        81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98
        ) 
    #getter     
    def getNom(self):
        return self.nom
    def getCouleur(self):
        return self.couleur
    def getCimetiere(self):
        return self.cimetiere

    #setter
    def echiquier(self,Echiquier):
        self.echiquier=Echiquier
# =============================================================================
# Definition des mouvemements possibles
# =============================================================================
    def mvmt_pion(self,position):
        '''
        Le pion peut potentiellemnt avancer de une ou deux cases devant lui au debut puis seulement une
        ou manger une piece ennemie à gauche ou à droite en diagonale, tant que les cases sont vides
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        ligne = 8 

        #Numero du tour (initial=1) Doit etre recuperer
        nb_tours= 1
        #Initialisation de la liste des positions
        position_possible=[]
        # Pion Blanc
        if self.couleur == 'blanc':
            #Tour initial
            if nb_tours == 1:
                position_possible += [position-2*ligne,position-ligne,position-ligne+1,position-ligne-1]
            #Tours suivants
            else:
                for i in [-1,0,1]:
                    #Si les cases devant lui sont vides
                    if self.echiquier.estVIDE(position-ligne+i):
                        position_possible += [position-ligne+i]
        #Pion noir
        if self.couleur == 'noir':
            if nb_tours == 1:
                #Tour initial
                position_possible += [position+2*ligne,position+ligne,position+ligne+1,position+ligne-1]
            #Tours suivants
            else:
                for i in [-1,0,1]:
                    #Si les cases devant lui sont vides
                    if self.echiquier.estVIDE(position+ligne+i):
                        position_possible += [position+ligne+i]
        return position_possible    

    def mvmt_roi(self,position):
        '''
        Le roi peut potentiellemnt avancer d'une case autout de lui-meme, tant que les cases sont vides
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        ligne =8

        #Creation de la liste des positions possibles
        for k in range(3): #Indice vertical
            for i in range(3): #Indice horizontal
                #si les cases autour de lui sont vides
                if self.echiquier.estVIDE(position-k*ligne-i):
                    position_possible+=[position-k*ligne-i]
        return position_possible
            
    def mvmt_cavalier(self,position):
        '''
        Le cavalier se deplace de deux cases devant, derriere ou sur les cotes puis une case a droite ou gauche, tant que les cases sont vides
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        ligne =8
        #Creation de la liste des positions possibles
        for k in [-2,2]: #Indice vertical
            for i in [-1,1]: #Indice horizontal
                # Si les cases sont vides
                if self.echiquier.estVIDE(position-k*ligne-i):
                    position_possible+=[position-k*ligne-i]
        for k in [-1,1]: #Indice vertical
            for i in [-2,2]: #Indice horizontal
                # Si les cases sont vides
                if self.echiquier.estVIDE(position-k*ligne-i):
                    position_possible+=[position-k*ligne-i]
        return position_possible
    
    def mvmt_tour(self,position):
        '''
        La tour se déplace d'autant de cases voulue devant, derriere, a droite ou a gauche, tant que les cases sont vides
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        len_ligne = 8
        #Calcule numero de ligne sur lequel est la tour
        ligne=position//len_ligne+1
        #Initialisation de la liste des positions possibles
        position_possibles=[]
        #Ajout des cases a l'horizontale
        for i in range(1,len_ligne+1):
            # Si les cases sont vides
            if self.echiquier.estVIDE((ligne-1)*len_ligne+i):
                position_possibles += [(ligne-1)*len_ligne+i]
        #Ajout des cases a la verticale
        for k in range(1,ligne-1):
            # Si les cases sont vides
            if self.echiquier.estVIDE(position-k*len_ligne):
                position_possibles += [position-k*len_ligne]
        for k in range(ligne+1,len_ligne+1):
            # Si les cases sont vides
            if self.echiquier.estVIDE(position+k*len_ligne):
                position_possibles += [position+k*len_ligne]
        return position_possibles
        
    def mvmt_fou(self,position):
        '''
        Le fou se déplace d'autant de cases voulue en diagonale, tant que les cases sont vides
        Retourne la liste des positions possibles
        '''
        #Recuperation de la longeur de la ligne
        len_ligne = 8
        #Calcule numero de ligne sur lequel est le fou
        ligne=position//len_ligne+1
        #Calcul numero de la colonne sur lequel est le fou
        colonne=position%len_ligne
        #Initialisation de la liste des positions possibles
        position_possibles=[]
        #Ajout des cases sur la diagonale de la position vers le coin en haut droit
        i=colonne
        #Tant que l'on a pas atteint de bord droit
        while i <len_ligne:
            #Au max on peut se deplacer de 8 cases sur la vertical
            for k in range(len_ligne):
                #Si les cases sont vides
                if self.echiquier.estVIDE(position-ligne*k+i):
                    position_posibles+=[position-ligne*k+i]
                #Deplacement sur la colonne suivante a droite
                i=i+1
        #Ajout des cases sur la diagonale de la position vers le coin en bas droit
        i=colonne
        #Tant que l'on a pas atteint de bord droit
        while i<len_ligne:
            #Au max on peut se deplacer de 8 cases sur la vertical
            for k in range(len_ligne):
                    #Si les cases sont vides
                    if self.echiquier.estVIDE(position+ligne*k+i):
                        position_posibles+=[position+ligne*k+i]
                    #Deplacement sur la colonne suivante a droite
                    i=i+1
        #Ajout des cases sur la diagonale de la position vers le coin en haut gauche
        i=colonne
        #Tant que l'on a pas atteint de bord gauche
        while i>-1:
            #Au max on peut se deplacer de 8 cases sur la vertical
            for k in range(len_ligne):
                    #Si les cases sont vides
                    if self.echiquier.estVIDE(position-ligne*k-i):
                        position_posibles+=[position-ligne*k-i]
                    #Deplacement sur la colonne suivante a gauche
                    i=i-1
        #Ajout des cases sur la diagonale de la position vers le coin en bas gauche
        i=colonne
        #Tant que l'on a pas atteint de bord gauche
        while i>-1:
            #Au max on peut se deplacer de 8 cases sur la vertical
            for k in range(len_ligne):
                    #Si les cases sont vides
                    if self.echiquier.estVIDE(position+ligne*k-i):
                        position_posibles+=[position+ligne*k-i]
                    #Deplacement sur la colonne suivante a gauche
                    i=i-1
        return position_possibles
