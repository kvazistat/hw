import sys
from random import *
import collections

def create(n):  # create matrix 4x4
    a = []
    row1 = [0] * n
    row2 = [0] * n
    row3 = [0] * n
    row4 = [0] * n
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'empty']
    # or b = range(n), if we need to create bigger field
    # b.append('empty')

    for i in range(n):
        x = choice(b)
        z = b.index(x)
        row1[i] = x
        b.remove(b[z])

    for w in range(n):
        x = choice(b)
        z = b.index(x)
        row2[w] = x
        b.remove(b[z])

    for k in range(n):
        x = choice(b)
        z = b.index(x)
        row3[k] = x
        b.remove(b[z])

    for e in range(n):
        x = choice(b)
        z = b.index(x)
        row4[e] = x
        b.remove(b[z])

    a.append(row1)
    a.append(row2)
    a.append(row3)
    a.append(row4)

    for i in range(n):
        print(a[i])

    return a

def up(matrix, x, y):  # up move
    b = matrix[x - 1][y]
    matrix[x][y] = b
    matrix[x - 1][y] = 'empty'
    for i in range(4):
        print(matrix[i])
    return matrix

def down(matrix, x, y):  # down move
    b = matrix[x + 1][y]
    matrix[x][y] = b
    matrix[x + 1][y] = 'empty'
    for i in range(4):
        print(matrix[i])
    return matrix

def left(matrix, x, y):  # left move
    b = matrix[x][y - 1]
    matrix[x][y] = b
    matrix[x][y - 1] = 'empty'
    for i in range(4):
        print(matrix[i])
    return matrix

def right(matrix, x, y):  # right move
    b = matrix[x][y + 1]
    matrix[x][y] = b
    matrix[x][y + 1] = 'empty'
    for i in range(4):
        print(matrix[i])
    return matrix

def index(matrix):
    x, y = 0, 0  # x, y - empty field coordinates
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'empty':
                x = i
                y = j
                break
    return x, y

def errmsg():
    print('you can not move empty field up cause it is out of game field')

n = 4 #задаем размерность игрового поля
win_matrix = [['1', '2', '3', '4'], #эталонное игровое поле, получиш которое игра заканчивается
              ['5', '6', '7', '8'],
              ['9', '10', '11', '12'],
              ['13', '14', '15', 'empty']]

print("Hello! Welcome to a game 'Fifteens'")
print("If your field be like this, you win. Enjoy!")
for i in range(n):
        print(win_matrix[i])
input("Please, type anything if you ready!\n")

a = create(n) #создаем рандомное поле

while (not a == win_matrix): #ввод и контроль ввода
    move = input()
    x, y = index(a)
    if move == 'up':
        if (x - 1 >= 0):
            a = up(a, x, y)
        else:
            errmsg()
        continue
    if move == 'down':
        if (x + 1 <= 3):
            a = down(a, x, y)
        else:
            errmsg()
        continue
    if move == 'left':
        if (y - 1 >= 0):
            a = left(a, x, y)
        else:
            errmsg()
        continue
    if move == 'right':
        if (y + 1 <= 3):
            a = right(a, x, y)
        else:
            errmsg()
        continue
    else:
        print('wrong command')