t1  = torch.cat([t2, t3], dim) # Concatenate the results along a specified dimension
t2  = mat * v5  # Multiply mat by the output of the concatenation and add to the input tensor
t1  = torch.cat([v6, t2], dim) # Concatenate the results along a specified dimension
t2  = mat * v5  # Multiply mat by the output of the concatenation and add to the input tensor
