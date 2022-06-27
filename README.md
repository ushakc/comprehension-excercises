# comprehension-excercises

Github:
<li>Fork this repository</li>
<li>Clone the repository to your local computer</li>
<li>Create a new branch named in the following format: firstname-lastname-solution</li>
<li>Push the new branch back to your repository</li>
<li>Create a new pull request so I can review your answer</li>

-------------------------------------------------------------------------------------------------
Problem 1

This is a classic problem given in technical interviews. First solve the problem WITHOUT using list comprehension.

"Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number. For Multiples of five print "Buzz". Finally, for numbers which are multiples of both three and five print "FizzBuzz".

Include comments for each step of your script explaining the Pseudo code/what each line is doing.

After you have solved it, write a second version of your script using list comprehension.

-------------------------------------------------------------------------------------------------

for num in range(1,101): # looping through range of 1-100
    if(num % 3 == 0):  
        print('Fizz', end = ' ') # print 'Fizz' for multiples of 3
    elif(num % 5 == 0):
        print('Buzz', end =' ') #print 'Buzz' for multiples of 5
    else:
        print(num, end = ' ') # if it is not multiple of 3 or 5 then print number


num = ["Fizz" if i%3==0 else ("Buzz" if i%5 == 0  else i) for i in range(1,101)]
print(num)






