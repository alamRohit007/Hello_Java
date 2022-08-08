user_info={
    'name':'harshit',
    'age':24,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale']
}

#how to add data

# user_info['fav_songs']=['song1','song2']
# print(user_info)

#how to delete using pop method
#pop method
# k=user_info.pop('fav_tunes')# put key name inside pop function
# #it is important to pass atleast one thing


# print(k) #pop methods return the list
# print(user_info) 


#popitem METHOD
#It will randomly remove random data
#popitem return tuple after randomly removing an item
popped_item=user_info.popitem()
print(user_info)
print(type(popped_item)) 