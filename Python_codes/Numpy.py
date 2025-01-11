import numpy as np

# Define two 2x2 matrices using NumPy arrays
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix Addition
addition_result = np.add(matrix1, matrix2)

# Matrix Subtraction
subtraction_result = np.subtract(matrix1, matrix2)

# Matrix Multiplication (Element-wise)
multiplication_elementwise = np.multiply(matrix1, matrix2)

# Matrix Multiplication (Dot Product)
multiplication_dot = np.dot(matrix1, matrix2)

# Display results
print(f"Matrix 1:\n{matrix1}")

print(f"\nMatrix 2:\n{matrix2}")


print(f"\nMatrix Addition:\n{addition_result}")


print(f"\nMatrix Subtraction:\n{subtraction_result}")


print(f"\nElement-wise Matrix Multiplication:\n{multiplication_elementwise}")


print(f"\nDot Product Matrix Multiplication:\n{multiplication_dot}")

