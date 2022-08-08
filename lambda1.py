#lambda is anonymous function

#lambda expressions it is a function which don't have a name and we can define them in single line

def add(a,b):
    return a+b

add2= lambda a,b : a+b
print(add2(2,3))

#we don't use lambda like this but we use it with built in functions like map, reduce , filter
multiply = lambda a,b : a*b
print(multiply(2,3))
print(add) #isko aap print karoga too ya function dikhayega and uski memory location dekhayega
print(add2) # isko aap print karoga it will show only lambda because it is not a function