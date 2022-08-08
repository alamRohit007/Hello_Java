
#1 for loop
#2 while loop

#For loop

#Why loops? 

#print("hello")

#1 --> starting point
#6 --> ending point 
#1 --> increment

# 3 --> 1+2+3 = 6
# 4 --> 1+2+3+4 = 10
# 5 --> 1+2+3+4+5 =15

n=int(input("Enter a number:"))
s=0
for i in range(0,n+1,1):
    if(i%2==0):
        s=s-i
    else:
        s=s+i 

print("The new sum is",s)
            
#3--> 1-2+3 = 2
#4--> 1-2+3-4 = -2
#5--> 1-2+3-4+5= 3
#2--> 1-2 =-1