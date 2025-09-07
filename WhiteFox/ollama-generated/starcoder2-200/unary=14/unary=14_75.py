t0 = conv_transpose(input_tensor) # Apply pointwise transposed convolution to the input tensor.
t1 = t0 * t2 # Multiply the output of the transposed convolution by the constant 3.584.
