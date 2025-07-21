t1 = torch.mm(mat1, mat2)  # Perform matrix multiplication between the first pair of matrices
t2 = torch.mm(mat3, mat4)  # Perform matrix multiplication between the second pair of matrices
t3 = t1 + t2  # Add the results of the two matrix multiplications
