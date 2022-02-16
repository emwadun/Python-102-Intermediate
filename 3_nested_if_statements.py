#This is when there is if statement inside another if statement
#

l = 10
u = 12
x = 17

if l > u:
    if l > x:
        print("l value is big")
    else:
        print("x value if big")
elif u > x:
    print("u value is big")
else:
    print("x is big")    # --> This will be one that will since all above conditions won't be satisfied.


