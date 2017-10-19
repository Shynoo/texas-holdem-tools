#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from deck import Deck
from card import Card,SevenCard,HandsCard
from player import Player
import random

class winResult():

    def __init__(self):
        self.result=[]
        self.playerNum=2
    
    def _randomGenerate(self,cardList,toDealNum):
        if toDealNum==0:
            return
        ls=random.sample(cardList,toDealNum)
        return ls

    def inRange(handsRange,totalNum=1000):
        for i in range(0,totalNum):
            deck=Deck()
                    