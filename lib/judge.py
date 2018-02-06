#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import random

#function which checks one puzzle is connected with neibors or not
#param : board(), index(integer)
def judge(board, idx):
    BOARD_YOKO = len(board[0])

#case when board idx starts from 0. shou represents tate, amari represents yoko
    trgt_tate = idx // BOARD_YOKO
    trgt_yoko = idx % BOARD_YOKO 
    print "target tate,yoko = %d,%d" % (trgt_tate, trgt_yoko) 

