from sympy import Matrix
from numpy import linalg as LA

A = Matrix([[1, 5, 9, 29], 
            [2, 0, 3, 26],
            [3, 7, 11, 39]])

Asympy = A.rref()

print(f'Solution for Matrix A with sympy: \n{Asympy}')

Aa = [[1, 5, 9], 
      [2, 0, 3],
      [3, 7, 11]]

Ab = [[29],
      [26],
      [39]]

print("")
print(f'Solution for Matrix A with numpy: \n{LA.solve(Aa, Ab)}')
print("-----------------------------------")

B = Matrix([[1, 1, 3, 4, 2],
            [-2, 2, 2, 0, -4],
            [1, 1, 2, 3, 1],
            [1, -1, -2, -1, 1]])

Bsympy = B.rref()

print(f'Solution for Matrix B with sympy: \n{Bsympy}')
#There is an infinite amount of solutions: the "Lösningsmängd" = {(1-t, -2, 1 - s, 0), t,s = R } ???????????