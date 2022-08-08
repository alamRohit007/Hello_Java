#any, all function
numbers1=[2,4,6,8,10]
numbers2=[1,2,3,4,5,6]

# #for telling number even or odd
# evens1=[]
# for num in numbers1:
#     evens1.append(num%2==0)
    
# print(evens1)

# #use of all is it returns True when all value inside is True else False
# #use of any it returns True if any one element in list is True

# print(all([True,True,True,True])) #True
# print(any([True,False,False]))

#if you want to check all numbers are even or not

print(all([num%2==0 for num in numbers1])) #gives True if all True
print(any([num%2==0 for num in numbers2]))# gives True if any is  one True