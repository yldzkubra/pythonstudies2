import sys
import math

l = int(input())
h = int(input())
t = input()

alphabet = [str(input()) for i in range(h)]

for i in range(h):
    for k in t:
        if   k>= 'a' and k <= 'z':
            x = ord(k) - ord('a')
        elif k >= 'A' and k <= 'Z':
            x = ord(k) - ord('A')
        else:
            x = ord('z') - ord('a') + 1
        for j in range(l):
            print(alphabet[i][x * l + j], end="")
            
    print("")


