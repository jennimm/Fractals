import turtle as t
import random
import math

#window = t.Screen()
snowflake = t.Turtle()
snowflake.left(45)
# for x in range(100):
#     for y in range(4):
#         snowflake.forward(50)
#         snowflake.right(45)
#         snowflake.forward(50)
#         snowflake.stamp()
#         snowflake.left(45)
#         snowflake.forward(30)
#         snowflake.right(60)
#     snowflake.right(59)

# p = 1
# q = 0.4

# for x in range(12):
#     for y in range(10):
#         p += 1.2 + 1.1*p + 1*(p**2) + 0.9*p*q + 0.8*q + 0.7*(q**2)
#         q += 0.6 + 0.5*p + 0.4*(p**2) + 0.3*p*q + 0.2*q + 0.1*(q**2)
#         print(p,q)
#         snowflake.right(p)
#         snowflake.forward(p)
#     snowflake.forward(q)
#     snowflake.right(q)

# for x in range(12):
#     for y in range(10):
#         p = 1.2 + 1.1*(x-1) + 1*((x-1)**2) + 0.9*(x-1)*(y-1) + 0.8*(y-1) + 0.7*((y-1)**2)
#         snowflake.forward(p)
#         snowflake.left(45)
#     q = 0.6 + 0.5*(x-1) + 0.4*((x-1)**2) + 0.3*(x-1)*(y-1) + 0.2*(y-1) + 0.1*((y-1)**2)
#     #snowflake.right(q)
#     snowflake.forward(q)

# run = True
# x = 0.1
# y = 0.1
# while run == True:
#     # snowflake.forward(x)
#     # snowflake.left(45)
#     # snowflake.forward(y)
#     # snowflake.right(45)
#     angle = (((y+1)-(1.4*(x**2))) - y) / ((0.3*x)- x)
#     angleFound = math.atan(angle)
#     snowflake.right(angleFound)
#     snowflake.forward(0.1)
#     snowflake.right(angleFound)
#     x, y = (y+1)-(1.4*(x**2)), 0.3*x
    
def drawTree(snowflake, branchLength, shorterLength, angle):
    if branchLength<5:
        return 
    else:
        snowflake.forward(branchLength)
        newLength = branchLength-shorterLength
        snowflake.right(angle)
        drawTree(snowflake, newLength, shorterLength, angle)
        snowflake.left(angle*2)
        drawTree(snowflake, newLength, shorterLength, angle)

        snowflake.right(angle)
        snowflake.backward(branchLength)
        #drawTree(snowflake, branchLength*0.5, angle)

        # snowflake.right(angle)
        # snowflake.forward(0.5*branchLength)
        #drawTree(branchLength*0.25, angle)
        
        #snowflake.forward()

drawTree(snowflake, 50, 5, 30)
