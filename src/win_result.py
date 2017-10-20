#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from deck import Deck
from card import Card,SevenCard,HandsCard
from player import Player
import random

class Board():

    def __init__(self):
        self.result=[]
        self.playerNum=2
        self.handsList=[]
        self.deck=None
        self.resultValue=None
    
    def _randomGenerate(cardList,toDealNum=5):
        if toDealNum==0:
            return
        ls=random.sample(cardList,toDealNum)
        return ls

    def fromStrings(strlist):
        result=Board()
        hs=set()
        for s in strlist:
            hands=HandsCard.fromString(s)
            if hands[0] in hs or hands[1] in hs:
                raise 'Error'
            hs.add(hands[0])
            hs.add(hands[1])
            result.handsList.append(hands)
        result.playerNum=len(result.handsList)
        return result

    def makeFakeResult(self,toDealNum):
        sevs=[]
        for h in self.handsList:
            showList=Board._randomGenerate(self.deck.inDeck,toDealNum=toDealNum)
            showList.extend(self.deck.showList)
            showList.extend(h)
            sev=Board.caculateValueFromCards(showList)
            sevs.append(sev)
        return sevs

    def makeBoardResultModel(sev):
        res=[]
        tempelete={
            'level':sev.level,
            'name':sev.levelText,
            'winNum':0,
            'totalNum':0,
        }
        return res

    def caculateValueFromCards(cardList):
        assert len(cardList)>=5 and len(cardList)<=7
        temp=SevenCard.fromHands(cardList)
        temp.caculateAll()
        return temp

    def generateResultByRandom(self,randomNum=1000,toDealNum=5):
        result={}
        for i in range(0,randomNum):
            Board._randomGenerate(self.deck.inDeck)




