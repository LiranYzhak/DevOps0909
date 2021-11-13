# def my_input():
#     a = int(input("enter number"))
#     b = int(input("enter number"))
#     return a, b

my_file2 = open("words2.txt",'w',encoding='utf-8')
my_file2.write("לירן יצחק")
my_file2.close()

my_file2 = open("words2.txt",'r',encoding='utf-8')
print(my_file2.read())
my_file2.close()