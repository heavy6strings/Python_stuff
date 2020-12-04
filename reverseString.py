
#ask the user for input. This will store the value on the 'phrase' variable
phrase = input('enter a phrase: ')
#this gets the length of the phrase that was just entered
phraseLength = len(phrase)

#tell the user the length of the sentence. the 'str' is because phraseLength is an integer. 
#integers cannot be concatenated to another string
#example: 5 + "asdf" does not work
#however, str(5) + "asdf" will return "5asdf"
print("The sentence you just entered is " + str(phraseLength) + " characters long.")


########## reverse the string ############

#x is set to the last character's index of the phrase
#the -1 is because arrays start at a 0 index. 
x = phraseLength - 1
#setting an empty array, which will be populated by the while loop below
reversedArray = []
while x >= 0:
    # start at the back side of the phrase variable and append each character to the 
    # reversedArray array in reverse of the given phrase
    reversedArray.append(phrase[x])
    x -= 1

#we are joining all the items in the reversed array and specifying '' as the character 
# we want between the character in the string ('' aka nothing)
reversedString = '--'.join(reversedArray)

#print out the reversed string with a little bit of info concatenated to show the user what 
#we're looking at
print("The reverse of the sentence is: " + reversedString)