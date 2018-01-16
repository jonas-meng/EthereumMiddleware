#!/bin/env python
# -*- coding: utf-8 -*-

import json
import copy

def median_of_medians(A, i):
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)/2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)/2]
    else:
        pivot = median_of_medians(medians, len(medians)/2)

    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high,i-k-1)
    else:
        return pivot


class Block:
    def __init__(self, prevhash, hash, number, transfers, balances):
        self.prevhash = prevhash
        self.hash = hash
        self.number = number
        self.transfers = transfers
        self.balances = balances

    def update_balances(self, balances):
        self.balances = copy.deepcopy(balances)
        for trx in self.transfers:
            self.perm_trx(trx.get('amount'), trx.get('receiver'), trx.get('sender'))
    
    def perm_trx(self, amount, receiver, sender):
        self.balances[receiver] += amount
        self.balances[sender] -= amount

    def get_median(self):
        return median_of_medians(self.balances.values(), len(self.balances)/2)


class Middleware:
    def __init__(self):
        self.head = None
        self.blocks = dict()

    def add_new_block(self, block):
        self.blocks[block.hash] = block

        if block.number == 0:
            self.head = block
        else:
            block.update_balances(self.blocks[block.prevhash].balances)
            if block.number > self.head.number:
                self.head.number = block
        
    def get_median(self):
        return self.head.get_median()


if __name__ == "__main__":  
    file_address = './mock_transaction.json'
    middleware = Middleware()
    account = []
    with open(file_address) as data:
        for block in json.loads(data.read()):
            middleware.add_new_block(
                Block(block.get('prevhash'), 
                    block.get('hash'), 
                    block.get('number'), 
                    block.get('transfers'), 
                    block.get('balances')))
    print('median of current all balances is {0}'.format(middleware.get_median()))