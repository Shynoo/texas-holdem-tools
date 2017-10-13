#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from decimal import Decimal


class Player():

    def __init__(self):
        self.hands=[]
        self.cardsValue=0
        self.winRate=0
        self.currentMoney=Decimal()

