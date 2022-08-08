with open("p1.txt",'r') as f:
    a=f.read()
with open("p1.txt",'w') as f:
    a=f.write("hello dear friend")
print(a)