t1  = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2  = tanh(t1) # Apply the hyperbolic tangent function to the output of the convolution
