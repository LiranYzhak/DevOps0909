





#A.
x = 40
y = 30
if x > y:
    print("BIG")
else:
    print("small")

#B.
for number in range(5):
    print(number)

#C.
season = input("choose number between 1-4:")
season = int(season)
if season == 1:
    print("Summer")
elif season == 2:
    print("Winter")
elif season == 3:
    print("Fall")
elif season == 4:
    print("Spring")

#D.
#1 10 Times loop run
#2 The last number is 10

#E.
my_age = 44
my_last_name_first_letter = "Y"
shekels_dollar_currency = 0.31
flew_abroad = True
my_apartment_number = 10

#1
print("My age is: ", my_age)
print("My last name first letter is: ", my_last_name_first_letter)
print("Current shkel to dollar currency is: ", shekels_dollar_currency )
print("My appartment number is: ",my_apartment_number)

#2
print(my_age + shekels_dollar_currency)

#F.
phone_number = input("What is your phone number? ")
print("phone number ",phone_number)

#G.
def printHello():
    print("hello")
printHello()

def calculate():
    print(5+3.2)
calculate()

#H.
#my method (input)
your_name = input("Type your name: ")
print("Your name is :",your_name)
your_number = input("choose number: ")
print(int(your_number) // 2)

# call function
def print_name(name):
    name = "Liran"


def divide_number(num):
    print(num/2)


#I.
#1
number_one = input()
number_two = input()
total = (int(number_one)+int(number_two))
#2
word_one = input()
word_two = input()
spcaed_string = (word_one + " " + word_two)

#K.
paund = "#"
for i in range


#L.

#M.
#1. gets a number from the user
user_number = input("Enter number with 2 digits: ")
#2. sum of the digits
first_digit = (int(user_number) // 10)
second_digit = (int(user_number) % 10)
sum_of_the_digits = (first_digit + second_digit)
print(sum_of_the_digits)