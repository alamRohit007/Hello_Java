#Finding max

l1=[1,3,5,7]
l2=[2,4,6,8]

new_list=[]

#we want output = [2,4,6,8]

for pair in zip(l1,l2):
    new_list.append(max(pair))
    
print(new_list[9])