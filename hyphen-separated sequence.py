"""
Assignment 2
Write a Python program that accepts 
a hyphen-separated sequence of words as input 
and prints the words in a hyphen-separated sequence 
after sorting them alphabetically.

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
"""
word_list=[word for word in input("Please write your hyphen-separated sequence of words ").split('-')]
print('-'.join(sorted(word_list)))
