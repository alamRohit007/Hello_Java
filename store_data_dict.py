#take input from users and store in dictionary and take fav movies in form of list and print the data in different lines

user_data={}

name=input('Enter your name:')

age=int(input('Enter your age:'))

movies=input('Enter your movies sep by comma:').split(',')

user_data['name']=name
user_data['age']=age
user_data['movies']=movies
for i,v in user_data.items():
    print(f"{i} : {v}")
