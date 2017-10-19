#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from pymongo import MongoClient

ip='localhost'
port=27017
client=MongoClient(ip,port)
db=client.poker

ratedb=db['hole_hands_win_rate']


dbnameTemplete='card%d_player%d_with_%s_range'

def generateDB(toDealNum=5,playerNum=2,rangee='100%'):
    name=dbnameTemplete%(toDealNum,playerNum,rangee)
    return db[name]

def getSortedData(db,key='winRate',des=-1):
    res=db.find({}).sort([(key,des)])
    return res

c5t9r100db=db['card5_player9_with_100%_range']
c3t9r100db=db['card3_player9_with_100%_range']
c4t9r100db=db['card4_player9_with_100%_range']