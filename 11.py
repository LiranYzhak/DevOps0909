import io
my_file = open("read_my_contents.txt", "r")
contents = my_file.readlines()
print(contents)

try:
    my_file.write("hello")
except io.UnsupportedOperation as e:
    print(e.args)

my_file.close()

my_file = open("names.txt", "w")
for i in range(3):
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
my_file.close()
print()
my_file = open("names.txt", "r")
for name in my_file.readlines():
    print(f"hello {name}", end="")
