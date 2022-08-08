def multiply_nums(num,*args):
    multiply = 1
    for i in args:
        multiply *=i
    return multiply

print(multiply_nums(2,3,4)) # now the answer is 12 , because 2 went inisde num only 3 and 4 multiplied together
    
    
    