t1 = torch.ones_like(input_tensor) # Get an identity matrix similar to that of the input tensor (used to add it with the output of a convolution)
t2 = conv(input_tensor) * t1 # Apply pointwise multiplication on each channel of the input tensor by an identity tensor, which is then added 
