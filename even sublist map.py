'''
Bonus 2
Write a Python program to filter a list of integers using Lambda.

Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list: [2, 4, 6, 8, 10]
Odd numbers from the said list: [1, 3, 5, 7, 9]'''

'''
names = ['Lassie', 'Colt', 'Rusty']

instructor = list(map(lambda name: f"Your instructor is {name}",
                filter(lambda value: len(value) < 5, names)))
print(instructor)'''

original_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sublist=list(filter(lambda x: x%2==0,original_list))
odd_sublist=list(filter(lambda x: x not in even_sublist,original_list))
print(even_sublist)
print(odd_sublist)