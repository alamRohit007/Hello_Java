# m=2
# for i in range(1,4,1):
#     for j in range(1,i+1,1):
#         for k in range(1,m+1,1):
#             print(' ',end='')
#         m=m-1
#         print('*',end='')
#     print()
        
        
for i in range(1,4,1):
    for j in range(1,4,1):
        if(i==j):
            print(' ',end='')
        else:
            print('*',end='')
    print()
        