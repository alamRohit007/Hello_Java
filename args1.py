#make flexible functions

#*operator
#*args

# def total(a,b):
#     return a+b
# print(total(4,5)) #
#*args it helps to put multiple values inside multiple values
#always put *args
def all_total(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
            
        
    
print(all_total(1,2,3))
#instead of args we can type anything it is not compulsion
#it creates a tuple of inputs
# now in the above code i can pass as many number while calling the function