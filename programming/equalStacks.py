# Problem taken from hackerrank
# Equal Stacks
# https://www.hackerrank.com/challenges/equal-stacks

import sys

def checkStackHeight(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 == 0 or n2 == 0 or n3 == 0:
        return True, 0
    elif s1[n1-1] == s2[n2-1] and s2[n2-1] == s3[n3-1]:
        return True, s1[n1-1]
    else:
        return False, -1

def removeTopHigherStacks(stackMinTop, s1, s2, s3):
    if s1[len(s1)-1] > stackMinTop:
        s1.pop()
    if s2[len(s2)-1] > stackMinTop:
        s2.pop()
    if s3[len(s3)-1] > stackMinTop:
        s3.pop()

def convertToStack(si, hi):
    height_sum = 0
    for height in reversed(hi):
        height_sum += height
        si.append(height_sum)

def convertAllToStack(h1, h2, h3, s1, s2, s3):
    convertToStack(s1, h1)
    convertToStack(s2, h2)
    convertToStack(s3, h3)

def getEqualHeight(n, h1, h2, h3):
    s1, s2, s3 = list(), list(), list()
    convertAllToStack(h1, h2, h3, s1, s2, s3)
    while True:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        sameHeightFlag, height = checkStackHeight(s1, s2, s3)
        if sameHeightFlag:
            return height
        else:
            stackMinTop = min(s1[n1-1], s2[n2-1], s3[n3-1])
            removeTopHigherStacks(stackMinTop, s1, s2, s3)

if __name__ == "__main__":
    n = [5, 3, 4]
    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]
    eHeight = getEqualHeight(n, h1, h2, h3)
    print(eHeight)
