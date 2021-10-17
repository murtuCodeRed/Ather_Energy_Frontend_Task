import random

# Rotates a 2D list clockwise
def rotate(mat):
    return list(map(list, zip(*mat[::-1])))

def move(mat, dir):
    for i in range(dir): mat = rotate(mat)
    for i in range(len(mat)):
        temp = []
        for j in mat[i]:
            if j != '.':
                temp.append(j)
        temp += ['.'] * mat[i].count('.') 
        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1] and temp[j] != '.' and temp[j + 1] != '.':
                temp[j] = str(2 * int(temp[j]))
                move.score += int(temp[j])
                temp[j + 1] = '.'
        mat[i] = []
        for j in temp:
            if j != '.':
                mat[i].append(j)
        mat[i] += ['.'] * temp.count('.')
    for i in range(4 - dir): mat = rotate(mat)

# Finds empty slot in the game mat
def findEmptySlot(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '.':
                return (i, j, 0)
    return (-1, -1, 1)

# Adds a random number to the mat
def addNumber(mat):
    num = random.randint(1, 2) * 2
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    lost = 0
    if mat[x][y] != '.':
        x, y, lost = findEmptySlot(mat)
    if not lost: mat[x][y] = str(num)
    return (mat, lost)

def printmat(mat):
    print("\n")
    for i in range(len(mat)):
        res = "\t\t"
        for j in range(len(mat[i])):
            for _ in range(5 - len(mat[i][j])): res += " "
            res += mat[i][j] + " "
        print(res)
        print("\n")
    return 0

def game():
    print("\n\t\t\t\t2048\n")

    mat=[['.', '2', '.', '.'],
        ['.', '4', '.', '2'],
        ['.', '.', '.', '.'],
        ['2', '.', '2', '4']]

    direction = {'L': 0, 'B': 1, 'R': 2, 'T': 3, 'X': 4}
    printmat(mat)

game()