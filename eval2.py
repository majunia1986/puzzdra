#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import random

#function which makes board move to next state
#動かした場合のpairの数を数えてリターンする
def sym_move_board(board, row, column, direction):
    SIZE_YOKO = len(board.test[0])
    SIZE_TATE = len(board.test)

    move_row = row
    move_column = column

    cur_board = board

#動かす石の色を記憶
    tmp = board.test[move_row][move_column]

#今のボードのコンボ数を格納する変数
    num_of_trio = 0

#右と交換するの場合
    if(direction = "MIGI"):
#右端列の場合はスキップ
        if(move_column != SIZE_YOKO-1):
            board.test[move_row][move_column] = board.test[move_row][move_column + 1]
            board.test[move_row][move_column + 1] = tmp
            num_of_trio = count_three_units(board)
#下と交換するの場合
    elif(direction = "SHITA"):
        #最下行の場合はスキップ
        if(move_row != SIZE_TATE-1):
            board.test[move_row][move_column] = board.test[move_row + 1][move_column]
            board.test[move_row + 1][move_column] = tmp
            num_of_trio = count_three_units(board)
#左と交換するの場合
    elif(direction = "HIDARI"):
        #左端列の場合はスキップ
        if(move_column != 0):
            board.test[move_row][move_column] = board.test[move_row][move_column - 1]
            board.test[move_row][move_column - 1] = tmp
            num_of_trio = count_three_units(board)
#上と交換する場合
    elif(direction = "UE"):
        #最上行の場合はスキップ
        if(move_row != 0):
            board.test[move_row][move_column] = board.test[move_row - 1][move_column]
            board.test[move_row - 1][move_column] = tmp
            num_of_trio = count_three_units(board)
    else:
        print "error: move_direction is not UE, MIGI, SHITA, HIDARI. "

        return num_of_trio

def move_or_not(board, size_tate, size_yoko):
    cur_board = board
    cur_three_units_num = count_three_units(board, size_tate, size_yoko)
    new_board = move_board(board, size_tate, size_yoko)
    tmp_three_units_num = count_three_units(new_board, size_tate, size_yoko)

    print "cur : tmp = %d, %d\n" % (cur_three_units_num, tmp_three_units_num)

    if(cur_three_units_num < tmp_three_units_num):
        return cur_board
    else:
        return new_board
    
