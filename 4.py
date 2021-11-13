names = ["yaniv", "tom", "liran", "ben"]
other_names = ["yaniv", "tom", "liran", "ben"]
a = 5
d = 5

if a == d:
    print("a eqauls d")

if names is other_names:
    print("names is other names")

if type(names) is list:
    print("name is list")

if names == other_names:
    print("names is the same")

print(type(names))
print(list)

my_empty_list = [1]
if len(my_empty_list) + 3 <= 5:
    print("hello")

numbers_of_sandwich = input("How much sandwiches you eat ?")
numbers_of_coffee = input("How much coffee you drink ?")

from colorama import Fore
from termcolor import colored,cprint

text1 = colored('You are hungry', 'red', attrs=['reverse', 'blink'])
text2 = colored('You are not hungry','green', attrs=['reverse', 'blink'])
i_am_hungry = (int(numbers_of_coffee) >= 1) and (int(numbers_of_sandwich) >= 2)
if i_am_hungry == True:
    print(text2)
#    print(Fore.GREEN + "You are not hungry")
else:
    print(text1)
#   print(Fore.RED + 'You are hungry')

