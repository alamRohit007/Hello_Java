#input --> ['rohit','alam']
#output --> ['Rohit' , 'Alam']

# def change(*args):
#     k=[(i[0].upper()+i[1:]) for i in args]
#     return k
# num=['rohit','alam']
# print(change(*num))

#input -->['rohit','alam']
#output -->['Tihor','Mala']
#userwillenter -->print(func(names,reverse_str=True))

def func(l,**kwargs):
    if(kwargs.get('reverse_str')==True):#with get method we can access any key
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
    
print(func(['rohit','alam'],reverse_str=True))