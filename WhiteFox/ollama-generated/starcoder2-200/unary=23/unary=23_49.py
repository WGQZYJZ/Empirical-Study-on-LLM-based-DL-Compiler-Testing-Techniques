t1 = conv_transpose(input_tensor) # Apply pointwise transposed convolution to the input tensor
t2 = torch.tanh(t1) # Apply the hyperbolic tangent function to the output of the transposed convolution
v3  = t1  + v2  * t2   # Add the output of the transposed convolution by a scalar and the hyperbolic tangent function's output, both multiplied by each other. This pattern is indistinguishable from the following, where both terms are added to the initial input tensor: conv_transpose(input_tensor, 1)
