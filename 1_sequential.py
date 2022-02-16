#sequential execution of code
#if we coment out declared variable a, we will get !NameError: name 'a' is not defined
#since it is required in the execution

a = 40 
b = 20
c = a - b

print("Subtraction is :", c)