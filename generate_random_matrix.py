import random
def generator_random_matrix(row, col):
    a = [[random.randint(1, 100) for j in range(col)] for i in range(row)]
    return a

m = int(input())
n = int(input())
print(generator_random_matrix(m, n))