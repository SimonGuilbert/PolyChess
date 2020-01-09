# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:21:41 2020

@author: guillyd
"""
import chess
import chess.polyglot
from random import randint

class IA :
    
        def impEchiquier(self,Echiquier):
            '''
            Importer l'echiquier
            '''
            self.echiquier=Echiquier    
    
        def ouverture(self):
            '''
            Donne les coup d'ouverture posible a l'IA
            '''
            board = chess.Board()
            hist=self.echiquier.historique
            for k in hist:
                if format(k)==str:
                    move=chess.Move.from_uci(k)
                    board.push(move)
                    print(board)
            
            with chess.polyglot.open_reader("data/polyglot/performance.bin") as reader:   
                Move=[]
                Weight=[]
                Learn=[]
                maxi=0
                i=0
                ind_max=0
                for entry in reader.find_all(board):
                    #print(entry.move,entry.weight,entry.learn)
                    Move+=[entry.move]
                    Weight+=[entry.weight]
                    Learn+=[entry.learn]
                if Move==[]:
                    return(None)
                elif len(Move)==len(Weight):
                    for w in Weight:
                        if w>maxi:
                            maxi=w
                            ind_max=i
                        elif w==maxi:
                            if Learn[ind_max]<Learn[i]:
                                maxi=w
                                ind_max=i
                        i+=1
                return(Move[ind_max])
                
        def evaluation(self):
            echi=self.echiquier.get_echiquier()
            score_blanc=0
            score_noir=0
            for piece in echi:
                if piece.getCouleur == 'blanc':
                    score_blanc+=piece.valeur()
                elif piece.getCouleur == 'noir':
                    score_noir+=piece.valeur()
            return (score_blanc,score_noir)
                
        def middlegame(self):
            '''
            IA pour le milieu de la partie cad apres l'ouverture et avant la fin de la partie
            '''
            i=0
            evalua=self.evaluation()
            position_possibles=[]
            meilleur_coup=[]
            for piece in self.echiquier.get_echiquier():
                if piece.getNom =='PION':
                    position_possibles+=piece.mvmt_pion(i)
                elif piece.getNom =='FOU':
                    position_possibles+=piece.mvmt_fou(i)
                elif piece.getNom =='TOURS':
                    position_possibles+=piece.mvmt_tour(i)
                elif piece.getNom == 'CAVALIER':
                    position_possibles+=piece.mvmt_cavalier(i)
                elif piece.getNom == 'DAME':
                    position_possibles+=piece.mvmt_dame(i)
                elif piece.getNom == 'ROI':
                    position_possibles+=piece.mvmt_roi(i)
                if position_possibles != []:
                    for move in position_possibles:
                        new=self.echiquier.deplacer(i,move)
                        if new.evaluation()[1]>=evalua[1]:
                            meilleur_coup+=[piece,i,move]
                i+=1
            if len(meilleur_coup)==1:
                return(meilleur_coup[0])
            else:
                k=randint(0,len(meilleur_coup))
                return(meilleur_coup[k])
            
 

# =============================================================================
# TEST           
# =============================================================================
#board = chess.Board()
#move=chess.Move.from_uci("c2c4")
#board.push(move)
#print(board)
#
#with chess.polyglot.open_reader("data/polyglot/performance.bin") as reader:   
#    Move=[]
#    Weight=[]
#    Learn=[]
#    maxi=0
#    i=0
#    ind_max=0
#    for entry in reader.find_all(board):
#        #print(entry.move,entry.weight,entry.learn)
#        Move+=[entry.move]
#        Weight+=[entry.weight]
#        Learn+=[entry.learn]
#    if Move==[]:
#        print(None)
#    elif len(Move)==len(Weight):
#        for w in Weight:
#            if w>maxi:
#                maxi=w
#                ind_max=i
#            elif w==maxi:
#                if Learn[ind_max]<Learn[i]:
#                    maxi=w
#                    ind_max=i
#            i+=1    
#    print(Move[ind_max])
    
            