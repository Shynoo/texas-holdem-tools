#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from card import Card,SevenCard,HandsCard
import random

class Deck():
    
    numList=[2,3,4,5,6,7,8,9,10,11,12,13,14]
    tagList=['d','h','c','s']
    initCardList=[]

    for num in numList:
        for tag in tagList:
            initCardList.append(Card(num,tag))

    def __init__(self):
        self.inDeck=Deck.initCardList.copy()
        self.showList=[]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.inDeck)
        self.showList=[]

    def dealOne(self,index=0):
        assert len(self.inDeck)>0
        r=self.inDeck[index]
        self.inDeck.remove(r)
        return r

    def dealAndShow(self,index=0):
        assert len(self.inDeck)>0
        r=self.inDeck[index]
        self.showList.append(r)
        self.inDeck.remove(r)
        return r

    def removeCards(self,cards):
        for card in cards:
            self.inDeck.remove(card)

    def removeCardsFromPlayers(self,players):
        for player in players:
            self.removeCards(player.hands)
