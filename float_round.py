x = 1
while x < 10:
    x += .001
    print(round(x,3))

#Without the 'round' argument the while loop goes into floating point insanity
#I think that in the instance of the 'print' function 'round' becomes an argument....


