#with the help of list comprehension we can create  list in one line

# squares =[]

# for i in range(1,11):
#     squares.append(i**2)
# print(squares) #this code is without comprehension

# square2= [i**2 for i in range(1,11)]
# print(square2) #with list comprehension same first question

# negative =[]
# for i in range(1,11,1):
#     negative.append(-i)
# print(negative)

# a=[-i for i in range(1,11,1)]
# print(a) #list comprehension same as above

# names=['rohit','mohit','harshit']
# k=[]
# for name in names:
#     k.append(name[0])
# print(k)

name2=['rohit','mohit','harshit']
new_list2=[name[0] for name in name2]
print(new_list2)#list comprehension