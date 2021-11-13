def my_function(current_name):
    print("hello " + current_name)

# () run function
for i in range(10):
    my_function("Liran")

# הגדרה
def sqrt(my_number):
    result = my_number * my_number
    return result
# קריאה
my_result = sqrt(7)
print(my_result)


def f(n):
    if n == 1:
        return 1
    else:
        return (n-1)
print (f(4))

ages = ["44","41","10","6"]
names = ["liran" , "Efrat", "Ido" , "Yahli"]
for i in range(4):
    print ((names[i])+" is "+ (ages[i]) +" Years Old")


def get_word(number):
    result = ""
    if number == 0:
        result = "zero"
    elif number == 1:
        result = "one"
    elif number == 2:
        result = "two"
    elif number == 3:
        result = "three"
    else:
        return "input is incorrect"
    return result

age = print(result)
