numbers=[1,2,3,4]
squares=map(lambda a:a**2,numbers)
print(squares)

for i in squares:
    print(i)

#the loop will work only one time on squares
for j in squares:
    print(j)
    
#for loops works
#step call iter function
#then next function

number_iter= iter(numbers)# iter function will take the number list
print(next(number_iter))#next function keep on taking the next value
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))