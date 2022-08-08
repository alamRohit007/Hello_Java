user_info={
    'name':'Rohit',
    'age':24,
    'fav_movies':['coco','kimi'],
    'fav_tunes':['awakening','fairytale']
}
# if 'Rohit' in user_info.values():
#     print('Present')
# else:
#     print('Not present')

# for i in user_info.values():
#     print(i)

for key,value in user_info.items():
    print(f"The key is {key} and value is {value}")

user_info_values=user_info.values()
l1,l2,l3,l4=list(zip(*user_info_values))
print(l1)
print(l2)
print(l3)
print(l4)