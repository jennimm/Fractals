import turtle as t

window = t.Screen()
snowflake = t.Turtle()

snowflake.left(45)
for x in range(100):
    for y in range(4):
        snowflake.forward(50)
        snowflake.right(45)
        snowflake.forward(50)
        snowflake.stamp()
        snowflake.left(45)
        snowflake.forward(30)
        snowflake.right(60)
    snowflake.right(59)
