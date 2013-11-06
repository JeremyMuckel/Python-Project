'''
Created on Nov 6, 2013


This is an exended comment
3 single quotes in a row (')

@author: Jeremy Muckel
'''

# this is a single line comment

def addTwo(a,b):
    return a+b

def addFixedToFive(a):
    fiv = 5
    return a+fiv

#displaying function output
print(addTwo(3,4))
print(addFixedToFive(1))

        

#string concatenation
print('the number five looks like: ' + str(5))
num = 88
print('num = ' + str(num))


#for and if/else
i = 0
for i in range(0,6):
    if i <= 3:
        print(str(i) + ' is smaller than four')
    else:
        print(str(i) + ' is four or larger')
        

#classes in PYTHON
class twoDimPoint:
    def __init__(self, x=0, y=0): #define constructor
        self.x = x
        self.y = y
    def __str__(self): #called if print is used in object
        return "parameter 1: " + str(self.x) + "\nparameter 2: " + str(self.y)
    def __add__(self): #called if addition is used in object
        p = twoDimPoint()
        p.x = self.x
        p.y = self.y
        return p
    

#creating objects
point1 = twoDimPoint(2,3)
point2 = twoDimPoint(4,5)
print (point1)
print (point1.x + point1.y)
#print (point1 + point2)



        