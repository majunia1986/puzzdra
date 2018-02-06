#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import random

#sys.path.append("/Users/Iwasawa/Desktop/project/puzzle/lib")
sys.path.append("/home/iwsw/projects/puzzle/lib")

import eval
import judge

#define class
class Board:
    def __init__(self):
        self.test = []

#####
# 1. count the number of each colors, find the best board)
# 2. find the nearlest board
# 3.
# 4.
#####

BOARD_SIZE_TATE = 4
BOARD_SIZE_YOKO = 5
NUMBER_COLOR = 5

#create board whose size is BOARD_SIZE_TATE * BOARD_SIZE_YOKO
board = Board()
for i in range(BOARD_SIZE_TATE):
    tmp_yoko = []
    for j in range(BOARD_SIZE_YOKO):
        item = random.randint(1,NUMBER_COLOR)
        tmp_yoko.append(item)
    board.test.append(tmp_yoko)

#print init board
for i in range(len(board.test)):
    print board.test[i]
print "trio_num is %d" % eval.count_three_units(board)

# test for judge function
print board.test[1]
print board.test[1][0]
judge.judge(board.test,14)


# #try n times move
# n=10
# for i in range(n):
#     row = random.randint(0,BOARD_SIZE_TATE - 1)
#     column = random.randint(0,BOARD_SIZE_YOKO - 1)
#     eval.move_board(board, row, column)
#     for j in range(len(board.test)):
#         print board.test[j]
#     print "hoge trio_num is %d" % eval.count_three_units(board)
