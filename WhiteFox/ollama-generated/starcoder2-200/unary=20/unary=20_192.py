t0  = conv_transpose(input_tensor) # Apply pointwise transposed convolution to the input tensor.
t1  = t0 + 1                       # Add one to the output of the transposed convolution.
t2  = t0 - 37                      # Subtract 37 from the output of the transposed convolution.
