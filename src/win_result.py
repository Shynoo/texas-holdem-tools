#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from deck import Deck
from card import Card,SevenCard,HandsCard
from player import Player
import random

class WinResult():

    def __init__(self):
        self.result=[]
        self.playerNum=2
        self.players=[]
        self.handsList=[]
    
    def _randomGenerate(self,cardList,toDealNum):
        if toDealNum==0:
            return
        ls=random.sample(cardList,toDealNum)
        return ls

    def fromStrings(strlist):
        result=WinResult()
        for s in strlist:
            hands=HandsCard.fromString(s)
            result.handsList.append(hands)
        result.playerNum=len(result.handsList)
        return result

    def generateResultByRandom(self,randomNum=1000):
        result={}
        for i in range(0,randomNum):
            deck=Deck.fromHandsList(self.handsList)
        


        
