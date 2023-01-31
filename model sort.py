'''
Bonus 1
Write a Python program to sort a list of dictionaries using Lambda.
 Original list of dictionaries :
  [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]'''

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

sorted_models_color = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries according to color :")
print(sorted_models_color)

sorted_models_make = sorted(models, key = lambda x: x['make'])
print("\nSorting the List of dictionaries according to make:")
print(sorted_models_make)

sorted_models_model = sorted(models, key = lambda x: int(x['model']))
print("\nSorting the List of dictionaries according to model:")
print(sorted_models_model)

