#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from deck import Deck
from card import Card,SevenCard
from player import Player
import random
import cProfile

import mongo.mongo

def _generateProbabilityGroupResult(cardList):
    totalResult=[]
    length=len(cardList)
    for n1 in range(0,length):
        for n2 in range(n1+1,length):
            tempList=([cardList[n1],cardList[n2]])
            totalResult.append(tempList)
    return totalResult

def _generateRandomGroupResult(cardList,totalNum,dealNum):
    res=[]
    if dealNum==0:
        return
    for i in range(0,totalNum):
        ls=random.sample(cardList,dealNum)
        res.append(ls)
    return res

def caculcateWinRateBy(deck,players,totalNum=2500):
    showList=deck.showList.copy()
    cardList=deck.inDeck.copy()
    winNum=[0 for i in players]

    totalResult=[]

    if len(showList)>=3:
        totalResult=_generateProbabilityGroupResult(cardList)
    else:
        dealNum=5-len(showList)
        totalResult=_generateRandomGroupResult(cardList,totalNum,dealNum)

    for cards in totalResult:
        cards.extend(showList)
        pv=[0 for i in players]
        for index,player in enumerate(players):
            temp=SevenCard.fromCardArray(cards,player.hands)
            temp.caculateAll()
            if temp.value>pv[index]:
                pv[index] = temp.value

        m=max(pv)
        for index,val in enumerate(pv):
            if val==m:
                winNum[index]+=1

    totalPv=0
    for index,num in enumerate(winNum):
        totalPv+=num
    res=[]
    for index,num in enumerate(winNum):
        players[index].winRate=num/totalPv
        res.append(num/totalPv)
    return res


def testWinRate(handsList,showCards=''):
    assert len(handsList)>=2
    deck=Deck()
    ls=[]
    players=[]
    for s in handsList:
        p1=Player()
        p1.hands=Card.arrayFromString(s)
        players.append(p1)
    deck.removeCardsFromPlayers(players)
    sl=Card.arrayFromString(showCards)
    deck.showList.extend(sl)
    deck.removeCards(sl)
    winRateList=caculcateWinRateBy(deck,players)
    for player in players:
        print('%s %.1f'%(str(player.hands[0])+str(player.hands[1]),player.winRate*100)+'%',end='  ')



def main():
    # cProfile.run('testWinRate()')
    testWinRate(['AsKh','QdQs'],'QhTsJs')

if __name__ == '__main__':
    main()
    
