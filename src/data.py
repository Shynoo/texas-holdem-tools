# -*- coding=utf-8 -*-

from win_rate import testWinRate
from deck import Deck
from mongo import mongo
from player import Player
import random
from card import Card


def insertDate(db,dataList):
    ratedb=db
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



def winRateVsRandomHands(playerNum=2,toDealNum=None,totalNum=1000):
    deck=Deck()
    players=[]
    for index in range(0,playerNum):
        p=Player()
        p.hands.append(deck.dealOne())
        p.hands.append(deck.dealOne())
        players.append(p)
    ls2=players
    winNum=testWinRate(ls2,totalNum=totalNum,toDealNum=toDealNum)
    for index,p in enumerate(ls2):
        print('%s %.1f'%(p.simpleHandsString(),p.winRate*100)+'%',end='  ')
    print()
    dataList=[]
    for index,p in enumerate(players):
        dataList.append({
            'hands':ls2[index].simpleHandsString(),
            'winNum':winNum[index],
            'totalNum':totalNum,
        })

    insertDate(mongo.generateDB(toDealNum=toDealNum,playerNum=playerNum,range='100%'),dataList)

def topHandsResult(k=0.25):
    if type(k)==float:
        k=int(169*k)
    ratedb=mongo.ratedb
    res=ratedb.find({}).sort([('winRate',-1)])
    handsResult=set()
    for i in range(0,k):
        hands=Card.arrayFromString(res[i]['hands'])
        handsResult.add(hands)
        if __name__ == '__main__':
            print(res[i]['hands'],end=' ')
    return handsResult

def alwaysInsertData():
    while True:
        for i in range(0,1000):
            winRateVsRandomHands(toDealNum=4)

def main():
    # topHandsResult(k=0.5)
    alwaysInsertData()

if __name__ == '__main__':
    main()