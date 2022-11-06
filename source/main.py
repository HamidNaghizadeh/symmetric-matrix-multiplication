import numpy as np
A = np.random.randn(4, 4)  # Creating a random 4x4 matrix
B = np.random.randn(4, 4)
S1 = (A + np.matrix.transpose(A))/2  # Creating symmetric matrix S1 from A with Additive algorithm
S2 = (B + np.matrix.transpose(B))/2  # Creating symmetric matrix S2 from B with Additive algorithm

addition = S1 + S2
standard_multiplication = S1 @ S2
hadamard_multiplication = np.multiply(S1, S2)

# A symmetric matrix minus its transpose should be all zeros

print('addition : \n', addition - np.transpose(addition))
print('\n')
print('Standard Multiplication : \n ', standard_multiplication - np.transpose(standard_multiplication))
print('\n')
print('Hadamard Multiplaction : \n', hadamard_multiplication - np.transpose(hadamard_multiplication))

# Addition and Hadamard Multiplication result is symmetric but Standard Multiplication isn't symmetric
