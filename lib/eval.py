#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import random

#function which counts two pairs
def count_three_units(board, tate_size, yoko_size):
    trio_num = 0

    #count trios in yoko
    for i in range(tate_size):
        for j in range(yoko_size - 2):
            if(board.test[i][j] == board.test[i][j+1] and board.test[i][j+1] == board.test[i][j+2]):
                trio_num += 1

    #count trios in tate
    for i in range(yoko_size):
        for j in range(tate_size - 2):
            if(board.test[j][i] == board.test[j+1][i] and board.test[j+1][i] == board.test[j+2][i]):
                trio_num += 1

    return trio_num

#function which makes board move to next state
def move_board(board):
    SIZE_YOKO = len(board.test[0])
    SIZE_TATE = len(board.test)

    move_row = random.randint(0,BOARD_SIZE_YOKO - 2)
    move_column = random.randint(0,BOARD_SIZE_TATE - 2)

#左上の場合
    if(move_row == 0 and move_column == 0):
        move_direction = random.choice(["MIGI","SHITA"])
#右上の場合
    elif(move_row == 0 and move_column == SIZE_YOKO-1):
        move_direction = random.choice(["SHITA","HIDARI"])
#右下の場合
    elif(move_row == SIZE_TATE-1 and move_column == SIZE_YOKO-1):
        print "hoge"
        move_direction = random.choice(["UE","HIDARI"])
#左下の場合
    elif(move_row == SIZE_TATE-1 and move_column == 0):
        move_direction = random.choice(["UE","MIGI"])
#最上行で角以外の場合
    elif(move_row == 0 and move_column != 0 and move_column != SIZE_YOKO-1):
        move_direction = random.choice(["MIGI","HIDARI","SHITA"])
#最下行で角以外の場合
    elif(move_row == SIZE_TATE-1 and move_column != 0 and move_column != SIZE_YOKO-1):
        move_direction = random.choice(["UE","MIGI","HIDARI"])
#最左列で角以外の場合
    elif(move_row != 0 and move_row != SIZE_TATE-2 and move_column == 0):
        move_direction = random.choice(["UE","MIGI","SHITA"])
#最右列で角以外の場合
    elif(move_row != 0 and move_row != SIZE_TATE-1 and move_column == SIZE_YOKO-1):
        move_direction = random.choice(["UE","SHITA","HIDARI"])
#それ以外（どの方向も動かせる）
    else:
        move_direction = random.choice(["UE","MIGI","SHITA","HIDARI"])

    print "swicth [%d][%d], %s" % (move_row, move_column, move_direction)

#ボードの配置を交換
    tmp = board.test[move_row][move_column]
    if(move_direction=="UE"):
        board.test[move_row][move_column] = board.test[move_row - 1][move_column]
        board.test[move_row - 1][move_column] = tmp
    elif(move_direction=="MIGI"):
        board.test[move_row][move_column] = board.test[move_row][move_column + 1]
        board.test[move_row][move_column + 1] = tmp
    elif(move_direction=="SHITA"):
        board.test[move_row][move_column] = board.test[move_row + 1][move_column]
        board.test[move_row + 1][move_column] = tmp
    elif(move_direction=="HIDARI"):
        board.test[move_row][move_column] = board.test[move_row][move_column - 1]
        board.test[move_row][move_column - 1] = tmp
    else:
        print "%s: error: move_direction is not UE, MIGI, SHITA, HIDARI. " % move_direction

    return board
