numbers=[1,2,3,4]

# def square(a):
#     return a**2

# squares=list(map(square,numbers))# function,list
# print(squares)

#another short form

squares=list(map(lambda a:a**2,numbers))
print(squares)

cube= [i**3 for i in numbers]
print(cube)

names=['abc','abcd','abcdef']
length=list(map(len,names)) #gives the length of element of list and creates a list
#map is iterable we can run a loop on it
print(length)