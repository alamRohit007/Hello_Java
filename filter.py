def is_even(a):
    return a%2==0

numbers=[3,4,2,1,5,6,9,8,10]

print(list(filter(is_even, numbers)))

print(list(filter((lambda x: x%2==0),numbers)))