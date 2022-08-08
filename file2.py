f=open('p.txt','r') #by default it takes r --> read 
data=f.readline() #read first line
print(data)
data=f.readline() #read second line
print(data)
data=f.readline() #read third line
print(data)
data=f.readline() #read it's content
print(data)
f.close()