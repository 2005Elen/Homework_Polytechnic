#task 1
import random
def generator_random_matrix(row, col):
    a = [[random.randint(1, 100) for j in range(col)] for i in range(row)]
    return a

m = int(input())
n = int(input())
matrix = generator_random_matrix(m, n)
print(matrix)

#task 2
def get_column_sum(matrix, index):
    summa = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == index - 1:
                summa += matrix[i][j]
    return summa

index_col = int(input())
print(get_column_sum(matrix, index_col))

#task 3
def get_row_average(matrix, index):
    s = sum(matrix[index-1])
    average = s / len(matrix)
    return average

index_row = int(input())
print(get_row_average(matrix, index_row))


