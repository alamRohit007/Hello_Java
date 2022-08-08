#example
#l=['abc','tuv','xyz']
#reverse_of_l=['cba','vut','zyx'] # this is a output

def revList(s):
    reverseList=[k[::-1] for k in s]
    return reverseList
l=['abc','tuv','xyz']
print(revList(l))
    
    