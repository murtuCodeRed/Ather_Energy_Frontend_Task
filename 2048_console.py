import random

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