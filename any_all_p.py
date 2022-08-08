#any all function real times uses in args
#if you want to check if anything entered by user in agrs is string but we are looking for numbers

def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return 'Enter proper value'

print(my_sum(1,2,3,4,'s'))