#list comprehension using if-else

#Input-->[1,2,3,4,5,6]
#Output-->[-1,4,-3,8,-5,12]

num=[1,2,3,4,5,6]
newList=[]

newList=[i*2 if (i%2==0) else -i for i in num]
print(newList)