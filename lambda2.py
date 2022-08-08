# def isEven(a):
#     return a%2==0 # True or False

# print(isEven(5))

# isEven2 = lambda a :a%2==0
# print(isEven2(6))

# def last_char(s):
#     return s[-1]

# last_char1= lambda s :s[-1]
# print(last_char1("rohit"))

# if/else with lambda

# def func(s):
#     if( len(s)>5):
#         return True
#     return False

# print(func('rohiat'))

# func1 = lambda s: True if len(s)>5 else False
# print(func1('rohita'))

func2 = lambda s: len(s)>5
print(func2('rohita'))