#1 -2
try:
    a = 1 / 0
    print(a)
except ZeroDivisionError as e:
    print("could not divide by zero")

#3. Code worked print finally
try:
    x = 1
finally:
    print("finally")

#4. Handle all exaption with Exept:

#5. The information provided causes us to be notified to ignore the issue

#6.
# Except IOError - handles I/O (input/output) exceptions
# Except ZeroDivisionError - handles divison by zero

#7.
my_file = open("words.txt", 'a')
my_file.close()

#8.
my_file.write("Liran"+"\n")
my_file.close()
#9.
my_file = open("words.txt", 'r')
for line in my_file.readlines():
    print(line)
my_file.close()

#10.
my_file2 = open("words2.txt",'w',encoding='utf-8')
my_file2.write("לירן יצחק")
my_file2.close()

my_file2 = open("words2.txt",'r',encoding='utf-8')
print(my_file2.read())
my_file2.close()

#11.Create image file with text

from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (400,400), color = (73,109,137))
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 42)
d = ImageDraw.Draw(img)
d.text((60,170), "Study DevOps", font=font,  fill=(255,255,0))
img.save('pil_txt.png')