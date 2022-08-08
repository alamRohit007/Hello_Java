# with open('p.txt','r') as f:
#     a=f.read()
#     print(a)
# with open('p.txt','w') as s:
#     s.write('hello brother')

# with open('p.txt','r') as f:
#     a=f.read()
#     print(a)
for i in range(1,11,1):
    with open('p.txt','w') as s:
        s.write(f"{10} x {i} = {10*i}\n")
    
with open('p.txt','r') as f:
    a=f.read()
    print(a)
        
        