# -*- coding=utf-8 -*-

from win_rate import testWinRate
from deck import Deck
from mongo import mongo
from player import Player
import random


def insertDate(dataList):
    ratedb=mongo.ratedb
    for data in dataList:
        r=ratedb.find_one({
            'hands':data['hands']
        })
        if not r:
            ratedb.insert_one(data)
        else:
            data['winNum']+=r['winNum']
            data['totalNum']+=r['totalNum']
            data['winRate']=data['winNum']/data['totalNum']
            ratedb.replace_one({'hands':data['hands']},data,True)


def winRateVsRandomHands(totalNum=1000):
    deck=Deck()
    players=[]
    for index in range(0,10):
        p=Player()
        p.hands.append(deck.dealOne())
        p.hands.append(deck.dealOne())
        players.append(p)
    ls2=random.sample(players,2)
    winNum=testWinRate(ls2,totalNum=totalNum)
    for index,p in enumerate(ls2):
        print('%s %.1f'%(p.simpleHandsString(),p.winRate*100)+'%',end='  ')
    print()
    dataList=[{
        'hands':ls2[0].simpleHandsString(),
        'winNum':winNum[0],
        'totalNum':totalNum,
    },{
        'hands':ls2[1].simpleHandsString(),
        'winNum':winNum[1],
        'totalNum':totalNum
    }]

    insertDate(dataList)


def main():
    while True:
        for i in range(0,1000):
            winRateVsRandomHands()

if __name__ == '__main__':
    main()