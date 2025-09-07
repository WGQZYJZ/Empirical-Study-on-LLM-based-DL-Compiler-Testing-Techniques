t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = tanh(t1 + 0.5)  # Add 0.5 to each element of the output of the convolution and then apply the hyperbolic tangent function to the result
