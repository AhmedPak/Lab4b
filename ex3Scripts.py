import sys

a = 2
b = 4
c = 6
d = 1
result = (a+b)*c
print(result)
if len(sys.argv) == 4:
    print("number of arguments: " +str(len(sys.argv)))
else: print("please enter 4 or more arguments")
def Binary (n):
    s = bin(n)
    s1 = s[2:]
    return s1
print(Binary(100))
