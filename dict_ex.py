#define a function that takes number n
#return a dictionary of cube from 1 to n
#1:1 ,2:4, 3:9 ...

def cube_finder(n):
    k={}
    for i in range(1,n+1,1):
        k[i]=i**3
        
    return k

n=int(input('Enter a number:'))
print(cube_finder(n))

