#l1=[1,3,5,7]
#l2=[2,4,6,8]

l=[(1,2),(3,4),(5,6),(7,8)]

# * operator with zip function to unpack the list into different list as it was before
#print(list(zip(*l)))
l1,l2=list(zip(*l))
print(l1)
print(l2)