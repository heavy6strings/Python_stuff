s = (input('Enter a string: ')).split()
#I do not understant the split function. I do know that while a string is inmutable it can be split
#Then added into the blank dictionary wrd_counter
wrd_counter = {}
for wrd in s:
    wrd_counter[wrd] = wrd_counter.get(wrd, 0) + 1
#It would seem wrd is a python thing that can be used....
#prob not tho....
print(wrd_counter)