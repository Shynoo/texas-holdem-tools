#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from decimal import Decimal

class GameRoom():
    
    def __init__(self):
        self.players=[]
        self.smallBlind=Decimal()
        self.bigBlind=Decimal()
        self.pot=[]

    def begin(self):
        pass

    def playerBet(self,player,betNum):
        pass

    def playerRaise(self,player,betNum):
        pass

    def playerCheck(self,player):
        pass
    
    def playerFold(self,player):
        pass

    def playerAllIn(self,player):
        pass


class GameManager():
    def __init__(self):
        pass