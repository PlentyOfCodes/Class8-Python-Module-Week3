
"""
Write a Python function that prints out 
the first n rows of Pascal's triangle. 
Note : Pascal's triangle is an arithmetic 
and geometric figure first imagined by Blaise Pascal."""
def pascal_triangle_row(n):
    #base case
    if n==1:
        return [1]
    #recursive case
    else:
        base_list=[0]+pascal_triangle_row(n-1)+[0]
        pascal_list=[base_list[j] + base_list[j+1] for j in range (len(base_list)-1)]
        return pascal_list


def firs_n_row_of_pascal_triangle(n):
    for i in range (1,n): print(pascal_triangle_row(i))

firs_n_row_of_pascal_triangle(10)

