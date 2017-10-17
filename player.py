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

    """
        以下行为委托 RoundGame类 完成
    """

    def bet(self,game,cashNum):
        betNum=Decimal(cashNum)
        if self.currentMoney<betNum:
            return False
        self.currentMoney-=Decimal(str(betNum))
        game.playerBet(self,betNum)

    def fold(self,game):
        assert type(game)==RoundGame
        game.playerFold(self)
    
    def check(self,game):
        game.playerCheck(self)
