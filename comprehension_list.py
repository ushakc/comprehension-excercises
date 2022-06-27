"""
for num in range(1,101): # looping through range of 1-100
    if num% 3 == 0 and num%5 == 0:
         print('Fizz Buzz', end = ' ') # both multiples of 3 and 5
    if(num % 3 == 0):  
        print('Fizz', end = ' ') # print 'Fizz' for multiples of 3
    elif(num % 5 == 0):
        print('Buzz', end =' ') #print 'Buzz' for multiples of 5
    else:
        print(num, end = ' ') # if it is not multiple of 3 or 5 then print number
"""


num = ["Fizz" if i%3==0 else ("Buzz" if i%5 == 0  else i) for i in range(1,101)]
for i in num:
    print(i)
