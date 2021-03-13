spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3: #when spam = 3, continue jumps to start and doesn't print 3
        continue
    print('spam is ' + str(spam))
