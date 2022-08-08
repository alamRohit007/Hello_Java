#list comprehension in nested list

#example --> [[1,2,3],[1,2,3],[1,2,3]]

l=[[1,2,3],[1,2,3],[1,2,3]]
newList=[[i for i in range(1,4,1)] for j in range(3)]
print(newList)