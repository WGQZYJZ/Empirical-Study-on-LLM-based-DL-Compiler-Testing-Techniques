t1 = torch.full([arg1], value, dtype=dtype, layout=layout, device=device, pin_memory=False) # Create a tensor filled with the scalar value `value`, with the specified dtype, layout, and device
t2  = t1[::stride]  # Extract elements from tensor t1 at indices corresponding to the values of one-dimensional index array (arange(start, end, step))
t1  = torch.empty([arg1, arg2], dtype=dtype, layout=layout, device=device, pin_memory=False) # Create an empty tensor with the specified shape and dtype, with the specified layout, and device
t2  = t1[::stride]  # Extract elements from tensor t1 at indices corresponding to the values of one-dimensional index array (arange(start, end, step))
t1 = torch.ones([arg1], dtype=dtype, layout=layout, device=device, pin_memory=False) # Create a tensor with all elements set to 1, with the specified shape and dtype, with the specified layout, and device
t2  = t1[::stride]  # Extract elements from tensor t1 at indices corresponding to the values of one-dimensional index array (arange(start, end, step))
t1 = torch.ones([arg1], dtype=dtype, layout=layout, device=device) # Create a tensor with all elements set to 1, with the specified shape and dtype, with the specified layout, and device
t2  = t1[::stride]  # Extract elements from tensor t1 at indices corresponding to the values of one-dimensional index array (arange(start, end, step))
