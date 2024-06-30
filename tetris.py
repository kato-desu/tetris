from art import * #アスキーアートを実装してくれる
from enum import Enum

#縦横のセル数を定義
FIELD_WIDTH = 10
FIELD_HEGHT = 20


#降ってくるブロックの定義
class Block():
    def __init__(self, name, shape):
        self.__name = name
        self.__shape = shape

    def get_shape(self):
        return self.__shape



#フィールド作り
for i in range(FIELD_HEGHT):
    print('|', end ='')
    for i in range(FIELD_WIDTH):
        print('　', end ='')
    print('|')

print(' ', end ='')
for i in range(FIELD_WIDTH):
    print('ー', end = '')
print(' ')


#位置を設定
cell = [[],[]]


#ブロックを定義
I = Block("i", "🔲　　　\n🔲　　　\n🔲　　　\n🔲　　　")
J = Block("j", "　　　　\n　🔲　　\n　🔲　　\n🔲🔲　　")
L = Block("l", "　　　　\n🔲　　　\n🔲　　　\n🔲🔲　　")
O = Block("o", "　　　　\n　　　　\n🔲🔲　　\n🔲🔲　　")
S = Block("s", "　　　　\n　　　　\n　🔲🔲　\n🔲🔲　　")
T = Block("t", "　　　　\n　　　　\n🔲🔲🔲　\n　🔲　　")
Z = Block("z", "　　　　\n　　　　\n🔲🔲　　\n　🔲🔲　")

print(T.get_shape())
print(Z.get_shape())














#tprint("TETRIS")