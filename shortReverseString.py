
#ask the user for input. This will store the value on the 'phrase' variable
phrase = input('enter a phrase: ')
print("The sentence you just entered is " + str(len(phrase)) + " characters long.")
print("The reverse of the phrase is: " + phrase[::-1])
