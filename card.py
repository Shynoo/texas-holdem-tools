#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import threading
import cProfile

class Card():
    
    table={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
    # 双向字典
    # reversedTable=bidict(table)

    def __init__(self,num,tag):
        self.num=num
        self.tag=tag

    def comparetor(this,that):
        if this.num>that.num:
            return 1
        if this.num<that.num:
            return -1
        return 0

    def __str__(self):
        return str(self.num)+self.tag
        
    def __str__(self):
        return str(self.num)+self.tag

    def __eq__(self,that):
        if self.num==that.num and self.tag==that.tag:
            return True
        return False

    def arrayFromString(s):
        arr=[]
        if len(s)%2!=0:
            raise 'card length Error'
        for i in range(0,len(s),2):
            arr.append(Card(Card.table[s[i]],s[i+1]))
        return arr


class SevenCard():
    def __init__(self,arr=[]):
        self.arr=arr
        self.maxValue=0
        self.value=0

    def __str__(self):
        res=''
        for card in self.arr:
            res+=card.__str__()+' '
        # TODO 
        # res+=self.value
        return res

    def fromString(s1,s2=''):
        s1=(s1+s2).strip()

        arr=Card.arrayFromString(s1)
        res=SevenCard()
        res.arr=sorted(arr,key=lambda x:x.num)
        
        return res

    def fromCardArray(arr,hands=[]):
        ls=arr.copy()
        ls.extend(hands)
        assert len(ls)>=5 and len(ls)<=7
        res=SevenCard()
        res.arr=ls
        res.arr.sort(key=lambda card:card.num)
        return res

    def generateNumNum(self,cards):
        nums={x:0 for x in range(1,15)}
        for card in cards:
            nums[card.num]+=1
            if card.num==14:
                nums[1]+=1
        return nums

    def generateTagNum(self,cards):
        tags={'h':0,'d':0,'c':0,'s':0}
        for card in cards:
            tags[card.tag]+=1
        return tags

    # 同花顺-9 同花-6
    def tryResolveStraightFlushAndFlush(self,cards,tagNum):
        tag=None
        for t in tagNum:
            if tagNum[t]>=5:
                tag=t
                break
        if tag==None:
            return False
        ls=cards.copy()
        for card in ls:
            if card.tag!=tag:
                ls.remove(card)
        r=self.testStraight(ls,self.generateNumNum(ls))

        if r:
            lev,mValue=r
            self.value=self.caculateValueFromTuple((9,mValue))
            return self.value
        
        self.value=self.caculateValueFromTuple((6,ls[-1].num,ls[-2].num,ls[-3].num,ls[-4].num,ls[-5].num))
        return self.value

    # 顺子-5
    def testStraight(self,cards,numNum):
        nums={x:0 for x in range(1,15)}
        for card in cards:
            nums[card.num]+=1
            if card.num==14:
                nums[1]+=1

        for i in range(14,5-1,-1):
            muNum=0
            for j in range(0,5):
                if nums[i-j]>=1:
                    muNum+=1
            if muNum==5:
                return (5,i)
        return False

    def tryResolveStraight(self,cards,numNum):
        r=self.testStraight(cards,numNum)
        if r:
            self.value=self.caculateValueFromTuple(r)
            return self.value
        return False

    def tryResolveFour(self,cards,numNum):
        f=0
        for num in range(14,1,-1):
            if numNum[num]>=4:
                f=num
                break
        if f==0:
            return False
        for num in range(14,1,-1):
            if numNum[num]>=1 and num!=f :
                self.value=self.caculateValueFromTuple((8,f,num))
                return self.value

    # 7
    def tryResolveFullHouse(self,cards,numNum):
        f,h=0,0
        for num in range(14,1,-1):
            if numNum[num]>=3:
                if f==0:
                    f=num
                else:
                    h=num
            if numNum[num]>=2:
                if num!=f and num>h:
                    h=num

        if f>0 and h>0:
            self.value=self.caculateValueFromTuple((7,f,h))
            return self.value
        return False

    # 4
    def tryResolveSet(self,cards,numNum):
        f,h1,h2=0,0,0
        for num in range(14,1,-1):
            if numNum[num]>=3:
                f=num
                break
        if f==0:
            return False
        for num in range(14,1,-1):
            if numNum[num]>=1:
                if num!=f:
                    if h1==0:
                        h1=num
                    else:
                        h2=num
                        break
        t=(4,f,h1,h2)
        self.value=self.caculateValueFromTuple(t)
        return self.value

     # 
    def tryResolvePair(self,cards,numNum):
        p1,p2,t=0,0,0
        ticker=[]
        for num in range(14,1,-1):
            if numNum[num]==2:
                if p1==0:
                    p1=num
                else:
                    p2=num
                    break
        if p1==0:
            return False
        
        if p1!=0 and p2==0:
            for num in range(14,1,-1):
                if len(ticker)==3:
                    break
                if numNum[num]==1:
                    ticker.append(num)
            tup=(2,p1,ticker[0],ticker[1],ticker[2])
            self.value=self.caculateValueFromTuple(tup)
            return self.value

        if p1!=0 and p2!=0:
            for num in range(14,1,-1):
                if numNum[num]==1:
                    t=num
                    break
            tup=(3,p1,p2,t)
            self.value=self.caculateValueFromTuple(tup)
            return self.value

    def tryResolveHigh(self,cards):
        t=(1,cards[-1].num,cards[-2].num,cards[-3].num,cards[-4].num,cards[-5].num)
        self.value=self.caculateValueFromTuple(t)
        return self.value

    def caculateValueFromTuple(self,tuple):
        value=[]
        v=[0,0,0,0,0,0]
        for index,num in enumerate(tuple):
            v[index]=num
        s='%02d%02d%02d%02d%02d%02d'%(v[0],v[1],v[2],v[3],v[4],v[5])
        val=int(s)
        return val

    def resolveMaxValue(self):

        cards=self.arr
        numNum=self.generateNumNum(cards)
        tagNum=self.generateTagNum(cards)

        if self.tryResolveStraightFlushAndFlush(cards,tagNum):
            self.maxValue=self.value
            return self.value
        if self.tryResolveFour(cards,numNum):
            self.maxValue=self.value
            return self.value
        if self.tryResolveFullHouse(cards,numNum):
            self.maxValue=self.value
            return self.value
        if self.tryResolveStraight(cards,numNum):
            self.maxValue=self.value
            return self.value
        if self.tryResolveSet(cards,numNum):
            self.maxValue=self.value
            return self.value
        if self.tryResolvePair(cards,numNum):
            self.maxValue=self.value
            return self.value
        if self.tryResolveHigh(cards):
            self.maxValue=self.value
            return self.value


    def multiThreadCaculateMaxValue(self):
        ls=self.allPosibleGroupOf7Cards()
        t1 = threading.Thread(target=self.caculateMaxValueWithList,args=(ls[0:20],))
        t2 = threading.Thread(target=self.caculateMaxValueWithList,args=(ls[20:],))

        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return self.maxValue


def test7Card():
    ls5=['AdKdQdJdTd','4dAd5d2d3d','AdAsAhAcTd','2d2h2s8d8h','KdTd8d2d3d','2d3c4dAd5d','AdAcAh4d6d','AdAcKdKcQd','2d2c3d5d6c','Ad9c4c7dKd']
    fs=[]
    for s in ls5:
        seven=SevenCard.fromString(s+'4c')
        seven.resolveMaxValue()
        fs.append(seven)
    ls2=sorted(fs,key=lambda seven: seven.value)
    for s in ls2:
        print(s,s.value)

def main():
    test7Card()

if __name__ == '__main__':
    main()
    
