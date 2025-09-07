t1 = torch.addmm(input, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input tensor
t2 = torch.addmv(input_vector, mat3)  # Add mat3 * input_vector to t1 along axis 0
t3 = t1 * 1.5 # Multiply t2 by 1.5
