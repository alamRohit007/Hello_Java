#more about get , two same keys in dictionaries
#get returns none if key is not there it is used to find key only
user={'name':'Rohit', 'age':24}
print(user.get('names'))

#if you put key and then comma and put some sentence then it  will  replace None with that sentence

print(user.get('names','Not found'))# now it will replace none by not found because anyways names is not a key in dictionary

#inside a dictionary we can't put same keys
# user1={'name':'rohit' , 'age':24, 'age':34}
#print(user1) --> 'name:'rohit' , 'age':34 --> whatever comes later it will take it