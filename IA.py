# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:21:41 2020

@author: guillyd
"""
import chess
import chess.polyglot
from random import randint
from Echiquier import Echiquier
class IA :
    '''
    Classe gerant l'intellignece artificielle
    Attention : necesitte le module chess (commande: pip install python-chess)
    '''  
    
    def ouverture(self,hist):
        '''
        Donne le coup d'ouverture pour l'IA
        '''
        #Cree un echiquier initial
        board = chess.Board()
        #Ajoute les coups deja fait
        for k in hist:
            mouvement=k[0]+k[1]
            move=chess.Move.from_uci(mouvement)
            board.push(move)
        #Ouvre la bibliotheque de polyglot
        with chess.polyglot.open_reader("data/polyglot/performance.bin") as reader:
            #Initialisation des variables
            Move=[]
            Weight=[]
            Learn=[]
            maxi=0
            i=0
            ind_max=0
            #Recherche de tous les coups possibles
            for entry in reader.find_all(board):
                Move+=[entry.move]
                Weight+=[entry.weight]
                Learn+=[entry.learn]
            #Si il n'y a pas de coups possibles
            if Move==[]:
                return(None)
            #Verifie si les listes sont de meme taille
            elif len(Move)==len(Weight):
                for w in Weight:
                    #Si le poids est plus grand que celui enregistre
                    if w>maxi:
                        maxi=w
                        ind_max=i
                    elif w==maxi:
                        #Utilisation de la 3eme variables pour detremine le meilleur coup
                        if Learn[ind_max]<Learn[i]:
                            maxi=w
                            ind_max=i
                    i+=1
            return(Move[ind_max])
            
    def evaluation(self,echiquier):
        '''
        Permet d'evaluer une position de l'echiquier a partir des pieces presentes sur celui-ci  
        '''
        #Initialisation
        score_blanc=0
        score_noir=0
        #Parcours de toutes les pieces sur l'echiquier
        for piece in echiquier.get_echiquier():
            #Si la piece est blanche, on ajoute sa valeur au score des blancs
            if piece.getCouleur() == 'blanc':
                score_blanc+=piece.getvaleur()
            #Si la piece est noire, on ajoute sa valeur au score des noirs
            elif piece.getCouleur() == 'noir':
                score_noir+=piece.getvaleur()
        return (score_blanc,score_noir)
            
    def middlegame(self,hist,ech):
        '''
        Donne le coup a joue pour l'IA en milieu de partie (cad apres l'ouverture et avant la fin de la partie)
        '''
        #Initalisation
        index=0
        evalua=self.evaluation(ech)
        meilleur_coup=[]
        meme_coup=[]
        #Pour chaque piece de l'echiquier
        for piece in ech.get_echiquier():
            if piece.getCouleur()=='noir':    
                position_possibles=[]
                if piece.getNom() =='PION':
                    position_possibles+=piece.mvmt_pion(index)
                elif piece.getNom() =='FOU':
                    position_possibles+=piece.mvmt_fou(index)
                elif piece.getNom() =='TOURS':
                    position_possibles+=piece.mvmt_tour(index)
                elif piece.getNom() == 'CAVALIER':
                    position_possibles+=piece.mvmt_cavalier(index)
                elif piece.getNom() == 'DAME':
                    position_possibles+=piece.mvmt_dame(index)
                elif piece.getNom() == 'ROI':
                    position_possibles+=piece.mvmt_roi(index)
                #Si la piece peut bouger
                if position_possibles != []:
                    #Pour chacun des mouvements possibles de la piece
                    for move in position_possibles:   
                        #Creation d'un echiquier initial
                        board=Echiquier()
                        #Ajout des coups deja joues
                        for h in hist:
                            board.deplacer(h[0],h[1])  

                        #Verification de la possiblite du coup puis deplacemnt de la piece avec
                        #Conversion des index du mouvement en coordonnes
                        if board.testeDeplacer(board.conversionEnCoord(index),board.conversionEnCoord(move)):
                            board.deplacer(board.conversionEnCoord(index),board.conversionEnCoord(move)) 
                            #Difference entre les cas en echec ou non
                            if ech.echec()[0]==True:
                                #Comparaison de evaluation de l'echiquier actuel avec l'ancien
                                if self.evaluation(board)[0]<evalua[0] and board.echec()[0]==False:
                                    #Si l'evaluation est meilleur, on garde ce mouvement et faire sortir de l'echec
                                    meilleur_coup=[[piece,index,move]]
                                    evalua=self.evaluation(board)      
                                #Si aucun des coups est meilleur et ne fait pas changer l'evaluation et faire sortir de l'echec 
                                if self.evaluation(board)[0]==evalua[0] and board.echec()[0]==False:
                                    #alors on les ajoutent a meme_coup
                                    meme_coup+=[[piece,index,move]]
                            else:
                                if self.evaluation(board)[0]<evalua[0]:
                                    #Si l'evaluation est meilleur, on garde ce mouvement
                                    meilleur_coup=[[piece,index,move]]
                                    evalua=self.evaluation(board)
                                #Si aucun des coups est meilleur et ne fait pas changer l'evaluation 
                                if self.evaluation(board)[0]==evalua[0]:
                                    #alors on les ajoutent a meme_coup
                                    meme_coup+=[[piece,index,move]]
            index+=1
        #Si l'existe, deplacement selon le meilleurcoup     
        if len(meilleur_coup)==1:
            #Retour le coup sur forme de coordonnes
            return(str(ech.conversionEnCoord(meilleur_coup[0][1]))+str(ech.conversionEnCoord(meilleur_coup[0][2])))
        #Sinon tirage au sort dans meme_coup
        else:
            k=randint(0,(len(meme_coup)-1)) 
            return(str(ech.conversionEnCoord(meme_coup[k][1]))+str(ech.conversionEnCoord(meme_coup[k][2])))

            

            
