#kwargs(keyword arguments)
# ** kwargs(double star operator)

#kwargs as a parameter
#instead of kwargs we can put any name here but ** mandatory
# def func(**kwargs):
#     print(kwargs)
    
# func(first_name="rohit",last_name="Alam")
#it gather things as dictionary

# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
        
# func(first_name="rohit",last_name="Alam")

def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

#dictionary unpacking
d={'name':'harshit','age':24}
func('rohit',**d)#**d likhna say dictionary unpacked jayegi
func("boys",first_name="rohit",last_name="Alam")