def isTidy(num):
    digits = []

    num = num
    while num > 0:
        digits.insert(0, num % 10)
        num = int(num // 10)

    #print (num,digits)

    min_digit = 0
    for i, digit in enumerate(digits):
        if (digit < min_digit):
            #print(i)
            next_num = 0
            for j in range(len(digits)):
                #print ('before:', next_num, j, i, digits[j])
                if j < i:
                    next_num = next_num * 10 + digits[j]
                else:
                    next_num = next_num * 10
                #print ('after: ', next_num)
            next_num = next_num - 1
            #print (next_num, next_num - 1)
            #if (next_num > num):
            #    next_num = Decimal(num) - Decimal(1)
            return next_num
        else:
            min_digit = digit

    return -1 #it's tidy already


def nextTidy(N):
    while (N > 0):
        #print(N)
        nextNum = isTidy(N)
        if (nextNum == -1):
            return N
        else:
            N = nextNum
    return None

#print (374687403419331879, '\n', nextTidy(374687403419331879))
t = int(input())  # read a line with a single integer
for i in range(t):
    num = int(input())
    #print(num)

    print ('Case #{}: {}'.format( i + 1, nextTidy(num)))