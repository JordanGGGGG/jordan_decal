#Problem 2
#2.1
Numbers = range(1, 21)
List_1 = list(Numbers)
print(List_1) 
#error message here: "& C:/Users/Jgome/anaconda3/python.exe c:/Users/Jgome/python_decal/jordan_decal/homework4/homework4.py 
# File "<stdin>", line 1 
#   & C:/Users/Jgome/anaconda3/python.exe c:/Users/Jgome/python_decal/jordan_decal/homework4/homework4.py  
#   ^
# SyntaxError: invalid syntax"
#I frequently run into this error in my python terminal and have no idea how to manually solve it. However I can still run my code as long as I use the run and debug feature in VScode.

#2.2
def squareList():
    return [i**2 for i in List_1] #I believe this returns the list I want because it is the bracket notation [] with my operation inside
List_2 = squareList()
print(List_2)

#2.3
first_fifteen_elements = List_2[0:15]
print(first_fifteen_elements)

#2.4
every_fifth_element = List_2[0:20:5]
print(every_fifth_element)

#2.5
fancy_function = List_2[::-3] #At first I tried using the index [0:20:-3] but that gave me an empty list. I then just left the first two numbers blank and it returned what I wanted.
print(fancy_function)

#Problem 3
#3.1

def create_2d_list():
    matrix = []
    num = 1
    for row in range(5):
        rowList = [num + i for i in range(5)]
        matrix.append(rowList)
        num += 5
    return matrix
print(create_2d_list())

#3.2
def modified_2d_list(matrix):
    for row in matrix:
        for j in range(len(row)):
            if row[j] % 3 == 0:
                row[j] = '?'
    return matrix

original_matrix = create_2d_list()
print("Original matrix:")
for row in original_matrix:
    print(row)

new_matrix = modified_2d_list(original_matrix)
print("new_matrix")
for row in new_matrix:
    print(row)

#3.3
def sum_non_question_elements():
    numbers = []
    for row in new_matrix:
        for j in range(len(row)):
            if row[j] != '?':
                numbers.append(row[j])
    total = sum(numbers)
    return total
print(sum_non_question_elements())



