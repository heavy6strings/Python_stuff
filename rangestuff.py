#list all multiples of 3, 5 while they're < 100
multiples = list(range(1,101,))
for x in multiples:
    if x % 3 == 0:
        print(x)
    elif x % 5 == 0:
        print(x)