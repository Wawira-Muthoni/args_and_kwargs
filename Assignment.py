#Write a function that accepts any number of integers as positional arguments 
# and any number of a student's attributes as keyword arguments and prints
#  the result of multiplying all of the integers with a 
# customized greeting based on the keyword arguments.
#Name the function multiply_and_greet.




import re


def multiply_and_greet(*args,**kwargs):
    keys = kwargs.keys()
    product = 1
    for a in args:
        product*=number
        return product
    if "age" in keys:
        return f"Hello {kwargs['name']} from {kwargs['age']}" 
    elif "country" in keys:
        return f"Hello {kwargs['name']} from {kwargs['country']}"
    elif "name" in keys:
        return f"Hello {kwargs['name']}"  
    else: 
        return f"Hello students"           

#     if "age" in keys:
#         print f"Hello {kwargs['name']} from {kwargs['age']}"
# elif "country" in keys:
#     print f"Hello {kwargs['name']} from {kwargs['country']}" 
# elif  "name" in keys:
#     print f"Hello {kwargs[name]}" 
#     else:
#         return f"Hello Student"         
     



