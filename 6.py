print(list(range(2, 10, 1)))
names = ["ariel", "adi", "eran", "adir"]
string_to_print = "Hello world!"


# print names 0 - 4 from index
# i = index

for i in range(4):
    print(names[i])
# more option
for i in range(len(names)):
    print(names[i])

# print name after name
for name in names:
    print(name)

a = 0

# כל עוד תנאי מתקיים = while
# if = תנאי פעם אחת
# break = exit from loop
# continue = bypass interaction

a = 0
while a < 10:
    print("a is not yet 10")
    a = a + 1
    if a == 5:
        break
a = 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print(a)
else:
    print("finished successfully")
    


for i in range (1, 30):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)








