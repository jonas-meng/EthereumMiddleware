#!/bin/env python
# -*- coding: utf-8 -*-

import json
import copy


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
        if not self.balances.get(receiver):
            self.balances[receiver] += amount
        if not self.balances.get(sender):
            self.balances[sender] -= amount

    def get_median(self):
        return sorted(self.balances.values())[len(self.balances) / 2]


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
            if block.number >= self.head.number:
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