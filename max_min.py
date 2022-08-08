#Today we will learn advance min and max

#numbers=[1,2,4,5,7]
#mx=max(numbers)
#mn=min(numbers)

#how to find out length names in list
# def func(item):
#     return len(item)


# names=['Harshit', 'Mohit', 'ab']
# print(max(names, key=func)) # print(max(names,key= lambda item: len(item)))
# print(min(names,key=func))

student1 = {
    'harshit': {'score':92,'age':21},
    'mohit':{'score':79, 'age':19},
    'rohit':{'score':711, 'age':33}
}
print(max(student1,key=lambda item:student1[item]['score']))


# student2= [
#     {'name':'harshit','score':90,'age':24},
#     {'name':'mohit','score':75, 'age':19},
#     {'name':'rohit','score':76, 'age':23}
# ]

# #Now we need to find out maximum according to score

# print(max(student2,key=lambda item:item.get('score'))['name'].title()) # it will give you a dictionary after using this

#if we only want to print name then


