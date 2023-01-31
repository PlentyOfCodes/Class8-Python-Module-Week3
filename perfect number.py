'''
Assignment 3
Write a Python function to check whether a number is perfect or not.

According to Wikipedia : In number theory, a perfect number is a positive integer
that is equal to the sum of its proper positive divisors, that is, 
the sum of its positive divisors excluding the number itself
(also known as its aliquot sum). Equivalently, a perfect number is a number 
that is half the sum of all of its positive divisors (including itself).

Example : The first perfect number is 6, 
because 1, 2, and 3 are its proper positive divisors, 
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal
to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
 This is followed by the perfect numbers 496 and 8128.'''

def perfect_number_check():
    given_number=int(input("Please write a positive number to check if it is a perfect number.\n"))
    divisors_list= [d for d in range(1,(given_number//2)+1) if given_number%d==0 ]
    print (f'{given_number} is a perfect number.' if sum(divisors_list)==given_number else f'{given_number} is not a perfect number.')

perfect_number_check()