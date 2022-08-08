#define a function
#input --> [True,False,[1,2,3],1,1.0,3]
#output --> ['1','1.0','3']

def listNew(f):
    k=[str(i) for i in f if (type(i) == int or type(i) == float)]
    print(k)
    
listNew([True, False, [1,2,3],1,1.0,3])

# l=[True, False, [1,2,3],1,1.0,3]
# for i in l:
#     if type(i) == int:
#         print("hi")