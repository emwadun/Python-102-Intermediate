'''
A recursive function is a function that calls itself.
Recursive functions are used for:
    ->  sequence generation
    ->  make the code look clean and elegant
'''

def recursive_sum(v):
    if v <= 1:
        return v
    else:
        print(v)
        return v + recursive_sum(v-1)

print(v := recursive_sum(5))

# --> The above will return 15 i.e. 5 + 4 + 3 + 2 + 1