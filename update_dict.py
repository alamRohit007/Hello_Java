user_info={
    'name':'harshit',
    'age':24,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale']
}

more_info={'name':'Rohit Alam','State': 'Haryana', 'hobbies':['coding','reading','guitar']}
#in above it will update name only
user_info.update(more_info)
#user_info.update({}) --> here we are not adding any data
print(user_info)




