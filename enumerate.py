#enumerate function we use with for loop to track

#how we can do this without enumerate function 

# names=['abc','abcdef','rohit']
# for i in range(len(names)):
#     print(i,'-->',names[i])
    
    
# #with enumerate function

# for pos,name in enumerate(names):
#     print(f"{pos} --> {name}")

#finding string in your list

def find_position(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1

print(find_position(['rohit','don','hello'], 'don'))