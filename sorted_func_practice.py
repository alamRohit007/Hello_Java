fruit1=['grapes','mango','apple']
#sort
#fruits.sort()
#print(fruits)# it will sort in ascending order


fruit2=('grapes','mango','apple')
print(sorted(fruit2))

#sort method is not there in tuples

#but sorted function works in tuples but returns list because tuples are immutable

fruit3={'grapes','mango','apple'}

print(sorted(fruit3))# will do for set also
print(type(fruit3))

guitars=[
    {'model':'yamaha f310','price':118400},
    {'model':'yamaha f233','price':928400},
    {'model':'yamaha f31330','price':78400},
    {'model':'yamaha f33210','price':824400},
    
]

k=sorted(guitars,key=lambda item:item['price'])
r=sorted(guitars,key=lambda item:item['price'],reverse=True)# will make the thing in descending order
print(k)