t1 = torch.zeros([20, 5], dtype=torch.float32)  # Create a tensor with shape [20, 5] and data type float32. All entries are zero.
t2 = torch.arange(20, dtype=torch.int64) # Create a tensor containing even numbers from 0 to 19 (exclusive). Data type is int64. 
t3 = t1[t2[:, None], t2] # Perform selection of rows and columns in the input tensor by row indices and column indices, respectively.
