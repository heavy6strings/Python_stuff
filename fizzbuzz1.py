for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i," - FizzBuzz")
    elif (i % 3 == 0):
        print(i," - Fist")
    elif (i % 5 == 0):
        print(i," - Puss")
    else:
        print(i)