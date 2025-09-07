t1 = torch.nn.functional.linear(input_tensor)  # Apply linear transformation to the input tensor.
t2 = t1.permute(...)  # Permute the output tensor from the linear transformation with the permuted index.
t1  = torch.nn.Linear(...).forward(input_tensor) # Apply linear transformation to the input tensor with a permuted index.
t2  = t1.permute(...)
