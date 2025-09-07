t1  = linear(input_tensor) # Apply a linear transformation to the input tensor.
t2  = t1.reshape(10, -1, 64).permute(-1, 1, 0)  # Reshape and transpose the output of the linear transformation. 
t3  = torch.nn.functional.linear(t2, weight=weight_tensor)  # Apply a linear transformation to the transposed and reshaped output. The weights must be provided as an argument.
