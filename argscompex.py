def power(n,*args):
    k=[i**n for i in args]
    return k
k1=[2,3,4]
print(power(2,*k1))