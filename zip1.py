#zip function
user_id=['user1','user2','user3']
names=['harshit ','mohit',]
sir=['alam','mulani','sharma','bhawal']

#output --> ('user1','harshit'),('user2','mohit')...
print(list(zip(user_id,names)))
print(list(zip(user_id,names,sir)))
#print(dict(list(zip(user_id,names))))