def save_names():
    name = input("enter name ")
    my_file = open("names.txt", "a")
    my_file.write(name +"\n")
    my_file.close

def show_names():
    my_file = open("names.txt", "r")
    for line in my_file.readlines():
        print(line)

save_names()
show_names()
