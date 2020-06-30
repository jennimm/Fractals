import turtle

def KochSnowflake(snowflake, length, shorterLength, angle, iterations):
    if iterations == 0:
        snowflake.forward(length)
        
    else:
        iterations -= 1
        length = length / shorterLength

        KochSnowflake(snowflake, length, shorterLength, angle, iterations)
        snowflake.left(angle)
        KochSnowflake(snowflake, length, shorterLength, angle, iterations)
        snowflake.right(angle*2)
        KochSnowflake(snowflake, length, shorterLength, angle, iterations)
        snowflake.left(angle)
        KochSnowflake(snowflake, length, shorterLength, angle, iterations)

snowflake = turtle.Turtle
for i in range(3):
    KochSnowflake(snowflake, 300, 5, 50, 4)
    snowflake.right(120)
