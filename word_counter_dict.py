#word counter
#harshit
#rules in dictionary two keys are not same in dictionary

# def count(a)://made by me
#     c=0
#     d={}
#     for i in a:
#         for j in a:
#             if(i==j):
#                 c=c+1
#         d[i]=c
#         c=0
#     return d  
        
    
def count(a):
    c={}
    for char in a:
        c[char]=a.count(char)
    return c

n=input('Enter your name:')
print(count(n))