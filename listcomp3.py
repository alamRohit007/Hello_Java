numbers=list(range(1,11))
#1,2,3,4,5,6,7,8,9,10
# print(numbers)
# even_nums=list(range(0,11,2))
# print(even_nums)

# nums=[]
# for i in numbers:
#     if i%2 == 0:
#         nums.append(i)
# print(nums)

evenNums=[i for i in numbers if i%2==0]
oddNums=[i for i in numbers if i%2!=0]
print(oddNums)
print(evenNums)

#one more way

# evenNum2=[i for i in range(1,11) if i%2==0]
# print(evenNum2) #here we are not even using numbers