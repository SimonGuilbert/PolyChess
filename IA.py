# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:21:41 2020

@author: guillyd
"""
import chess
import chess.polyglot
from random import randint
from Echiquier import Echiquier8x8
class IA :
    '''
    Classe gerant l'intellignece artificielle
    Attention : necesitte le module chess (commande: pip install python-chess)
    '''
#    def __init__(self):
#        ech=Echiquier8x8()
#    
#    def impEchiquier(self,Echiquier):
#        self.echiquier=Echiquier    
    
    def ouverture(self,hist):
        '''
        Donne les coup d'ouverture posible a l'IA
        '''
        board = chess.Board()
        for k in hist:
            mouvement=k[0]+k[1]
            move=chess.Move.from_uci(mouvement)
            board.push(move)
        
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
                #print('move',Move)
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
            
    def evaluation(self,ech):
        #ech=Echiquier8x8()
        score_blanc=0
        score_noir=0
        for piece in ech.get_echiquier():
            if piece.getCouleur() == 'blanc':
                score_blanc+=piece.getvaleur()
            elif piece.getCouleur() == 'noir':
                score_noir+=piece.getvaleur()
        return (score_blanc,score_noir)
            
    def middlegame(self,hist,ech):
        '''
        IA pour le milieu de la partie cad apres l'ouverture et avant la fin de la partie
        '''
        i=0
        evalua=self.evaluation(ech)
        meilleur_coup=[]
        meme_coup=[]
        k=0
        for piece in ech.get_echiquier():
            if piece.getCouleur()=='noir':    
                position_possibles=[]
                if piece.getNom() =='PION':
                    position_possibles+=piece.mvmt_pion(i)
                elif piece.getNom() =='FOU':
                    position_possibles+=piece.mvmt_fou(i)
                elif piece.getNom() =='TOURS':
                    position_possibles+=piece.mvmt_tour(i)
                elif piece.getNom() == 'CAVALIER':
                    position_possibles+=piece.mvmt_cavalier(i)
                elif piece.getNom() == 'DAME':
                    position_possibles+=piece.mvmt_dame(i)
                elif piece.getNom() == 'ROI':
                    position_possibles+=piece.mvmt_roi(i)
                #print(piece.getNom(),position_possibles)
                if position_possibles != []:
                    for move in position_possibles:   
                        board=Echiquier8x8()
                        for h in hist:
                            board.deplacer(h[0],h[1])    
                        dep=board.conversionEnCoord(i)
                        arr=board.conversionEnCoord(move)
                        board.tourJoueur=str(piece.getCouleur())
                        board.deplacer(dep,arr)
                        #print('s',self.evaluation(board))
                        if self.evaluation(board)[0]<evalua[0]:
                            meilleur_coup+=[[piece,i,move]]
                            #print('helo')
                        elif self.evaluation(board)[0]==evalua[0]:
                            #print('bouh')
                            meme_coup+=[[piece,i,move]]
            i+=1
        if len(meilleur_coup)==1:
            depla=str(ech.conversionEnCoord(meilleur_coup[k][1]))+str(ech.conversionEnCoord(meilleur_coup[k][2]))
            return(depla)
        else:
            max_rand=len(meme_coup)-1
            k=randint(0,(max_rand)) 
            depla=str(ech.conversionEnCoord(meme_coup[k][1]))+str(ech.conversionEnCoord(meme_coup[k][2]))
            return(depla)
            
        
 

# =============================================================================
# TEST           
# =============================================================================
#board = chess.Board()
#move=chess.Move.from_uci("c2c4")
#board.push(move)
#move=chess.Move.from_uci("g8f6")
#board.push(move)
#move=chess.Move.from_uci("d2d4")
#board.push(move)
#move=chess.Move.from_uci("e7e6")
#board.push(move)
#move=chess.Move.from_uci("g1f3")
#board.push(move)
#move=chess.Move.from_uci("d7d5")
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
    
            