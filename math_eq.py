'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
'''
import math
c = 50
h = 30
out_lst = list()
inp = (input("Enter values "))

values = inp.split(",")
print (values)
for i in values:
    q= round(math.sqrt(((2*c*float(i))/h)))
    out_lst.append(q)
print(out_lst)