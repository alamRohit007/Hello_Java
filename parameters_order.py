# def func(name="unkown",age=24):
#     print(name,age)
    
# func('rohit',14) #iss tarekasay bhe hum function call kar skta hai
#PADK
#parameters
#args
#default parameters
#kwargs

#maintain the order if you want to use args and kwargs together

def func(name,*args,last_name='Unkown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
    
func('rohit',1,2,3,a=1,b=2)
