from PIL import Image
print('?ךל םיארוק ךיא')
name = input()
print ('?ךילע הבוהאה היחה המ ' + name + ' םולש')
animal =input()
if animal=='לותח': Image.open('cat.jpg').show()
if animal=='רגוא': Image.open('hamster.jpg').show()
if animal=='ףוק': Image.open('monkey.jpg').show()