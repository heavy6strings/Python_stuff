s = (input('Enter a string: ')).split()
wrd_counter = {}
for wrd in s:
    wrd_counter[wrd] = wrd_counter.get(wrd, 0) + 1

print(wrd_counter)