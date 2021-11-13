import requests

try:
    my_varible = int(input("enter first umber:"))
    my_other_var = int(input("enter second number:"))
    result = my_varible / my_other_var
    print(result)
except ZeroDivisionError as e:
    print("could not divide by zero")
except ValueError as e:
    print("enter a normal number")
except BaseException as e:
    print(e.args)

# try:
#     requests.get("htpps://github.com")
# except BaseException as e:
#     print("something when wrong , check this: " + str(e.args))
# print("hello after mess")

#
# def get_user_age():
#     input_from_user = int(input("enter your positive age:"))
#     if input_from_user < 0:
#         raise ValueError("age can not be negative")
#
# try:
#     get_user_age()
# except ValueError as e:
#     print(e.args)
