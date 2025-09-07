
t1 = conv2d_transpose(input_tensor) # Apply pointwise transposed convolution to the input tensor 
t2 = batchnorm(t1, dim=0) # Batch normalizing each channel independently.
