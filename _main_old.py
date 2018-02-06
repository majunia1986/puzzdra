import sys
import re
import random

#define class
class Board:
    def __init__(self):
        self.test = ""

#####
# 1. count the number of each colors, find the best board)
# 2. find the nearlest board
# 3.
# 4.
#####

BOARD_SIZE_TATE = 5
BOARD_SIZE_YOKO = 6
NUMBER_COLOR = 6

#create BOARD_SIZE_TATE * BOARD_SIZE_YOKO board
board = Board()
for i in range(BOARD_SIZE_TATE):
    for j in range(BOARD_SIZE_YOKO):
        item = random.randint(1,NUMBER_COLOR)
        board.test += '%d ' % item
    if (i != 4):
        board.test += "\n"

#make ui better by changing number to alphabet
COLOR_1 = '1'
COLOR_2 = '2'
COLOR_3 = '3'
COLOR_4 = '4'
COLOR_5 = '5'
COLOR_6 = '6'
board.test = re.sub("1",COLOR_1,board.test)
board.test = re.sub("2",COLOR_2,board.test)
board.test = re.sub("3",COLOR_3,board.test)
board.test = re.sub("4",COLOR_4,board.test)
board.test = re.sub("5",COLOR_5,board.test)
board.test = re.sub("6",COLOR_6,board.test)

#count numbers of each alphabet
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0
cnt_6 = 0

for i in range(len(board.test)):
    tmp = board.test[i]
    if(tmp==COLOR_1):
        cnt_1 += 1
    elif(tmp==COLOR_2):
        cnt_2 += 1
    elif(tmp==COLOR_3):
        cnt_3 += 1
    elif(tmp==COLOR_4):
        cnt_4 += 1
    elif(tmp==COLOR_5):
        cnt_5 += 1
    elif(tmp==COLOR_6):
        cnt_6 += 1

#print the initial board
print "%s" % board.test
print "%s:%d\t%s:%d\t%s:%d\t%s:%d\t%s:%d\t%s:%d" % (COLOR_1, cnt_1, COLOR_2, cnt_2, COLOR_3, cnt_3, COLOR_4, cnt_4, COLOR_5, cnt_5, COLOR_6, cnt_6)

