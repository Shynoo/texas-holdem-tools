#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from pymongo import MongoClient

ip='localhost'
port=27017
client=MongoClient(ip,port)
db=client.poker

ratedb=db['hole_hands_win_rate']






rateTemplete={
    'hands':hands,
    'vs':vs,
    'winNum':0,
    'totalNum':0
}