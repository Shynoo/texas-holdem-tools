#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from decimal import Decimal

class Player():

    def __init__(self):
        self.hands=[]
        self.handsValue=0
        self.winRate=0
        self.currentMoney=Decimal()
        self.name=''

    
    def __str__(self):
        return self.name+" "+str(self.hands[0])+str(self.hands[1])+" money:"+str(self.currentMoney)

    def sortHands(self):
        self.hands.sort(key=lambda card:card.num)


