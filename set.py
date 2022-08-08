#Sets are unordered
#Sets are unindexed
#No way to change items in sets
#Set can not duplicate values


a ={1,3,4,5}
print(a)
#set is a collection of non repetitive elements
#Important a={} will create empty dictionary not set

#Empty set creation
b=set()#Empty set creation
print(type(b))

b.add(4)
b.add(3)
b.add(2)
#b.add([4,5,6])#You can't put list in set but you can put  tuples because you can't change it
b.add((5,6,7,2)) #you can add only tuples because they can't get changed
print(b)