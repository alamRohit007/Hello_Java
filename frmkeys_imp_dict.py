# fromkeys method
#it is used to create dictionary

# d={'name':'unkown',
#    'age':'unkown',
#    }

#d=dict.fromkeys(['name','age','height'],'unkown') #i
#print(d)

#if you put a string at place of list then it will break every character and make unkown a value for it
#you can also put a tuple keys
#you can also put range function over there and all the range values will be having a key by name unkown
#the above code will make three keys with same value 'unkown' in all of them


#get method(very useful)

d={'name':'unkown','age':'unkown'}
print(d['name'])

#instead of using straight method in 20 line we can use get method

print(d.get('name')) # WORKS SAME AS 20 LINE BUT GIVES NONE IF NOTHING IS THERE AS name key

'''
if 'name' in d:
    print('present')
else:
    print('not present')
    
if d.get('name):
    print('present')
else:
    print('not present')

'''
#if you want to clear dictionary use clear method
#d.clear()

#copy method

d1=d.copy()# it will copy d in d1
