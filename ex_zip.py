#INPUT --> [1,2,3],[4,5,6],[7,8,9]
#OUTPUT --> (1+2+3)/3,(4+5+6)/3,(7+8+9)/3
#try using lambda
# def average_finder(l1,l2):
#     average=[]
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))#program for two list
#     return average
# print(average_finder([1,2,3],(4,5,6)))

#args always take things in tuple

# def average_finder(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average

# print(average_finder([1,2,3],(4,5,6),(7,8,9)))


#same question using lambda and comprehension
lambda *args:
