def multiplyNums(*args):
    mul=1
    print(args)
    for i in args:
        mul *=i
    return mul

num=[2,3,4]

#if you want 
print(multiplyNums(*num))# put * sign when passing list as an argument