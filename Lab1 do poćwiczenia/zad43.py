import numpy as np
import math

x = np.array([3, 8, 9, 10, 12])
y = np.array([8, 7, 7, 5, 6])

#a
print("Suma ",x+y)
print("Iloczyn ",x*y)

#b
print(np.einsum('i,i',x,y))

#c
def bare_numpy(v, u):
    z = v - u
    return np.sqrt(np.einsum('i,i->', z, z))
print(bare_numpy(x,y))

#d
x2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
y2 = np.array([
    [1,2,1],
    [2,4,6],
    [7,2,5]])

print(np.multiply(x2,y2))

#e
yyy = np.linspace(1,100,50)

#f
print(min(yyy))
print(max(yyy))
print(sum(yyy)/len(yyy))

def odchylenie(dan):
    avg=sum(yyy)/len(yyy)
    for number in sorted(dan):
        print (number, math.fabs(avg - number))

print(odchylenie(yyy))

#g
for index, i in enumerate(yyy):
    yyy[index] = i - min(yyy)/max(yyy)-min(yyy)

print(yyy)