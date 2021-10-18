import random
size=4

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
    for i in range(size - dir): mat = rotate(mat)
    return mat

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
    x = random.randint(0, size-1)
    y = random.randint(0, size-1)
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

def check(mat):
    for i in range(0,size):
        for j in range(0,size):
            if mat[i][j]==".":
                continue
            if mat[i][j]==2048:
                return 0
    return 1

def game():
    print("\n\t\t\t\t\t2048")

    mat = []
    for i in range(0,size):
        a=[]
        for j in range(0,size):
            a.append(".")
        mat.append(list(a))
    
    mat[0][0]="1024"
    mat[0][1]="1024"

    direction = {'L': 0, 'B': 1, 'R': 2, 'T': 3, 'X': 4}

    printmat(mat)
    loseStatus = 0
    winStatus=0
    move.score = 0 # Score of the user
    while True:
        tmp = input("\nTo continue, Press L for left, R for right, T for top, B for bottom or\nPress X to end the game.\n")
        if tmp in ["R", "r", "L", "l", "T", "t", "B", "b", "X", "x"]:
            dir = direction[tmp.upper()]
            if dir == 4:
                print("\nFinal score: " + str(move.score))
                break
            else:
                mat = move(mat, dir)
                mat, loseStatus = addNumber(mat)
                winStatus=check(mat)
                printmat(mat)
                
                if winStatus:
                    print("\nYou have won!!!!")
                    print ("Final score: " + str(move.score))
                    break          
                if loseStatus:
                    print ("\nGame Over")
                    print ("Final score: " + str(move.score))
                    break
                print ("\nCurrent score: " + str(move.score))
        else:
            print ("\nInvalid direction, please provide valid movement direction (L, B, R, T).")
    return 0

game() 