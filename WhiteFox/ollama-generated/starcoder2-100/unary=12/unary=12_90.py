t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = tanh(t1 * 3.0 - 4.5) + 1 # Multiply the output of the convolution by a constant 3, then subtract a constant 4.5 from it, apply the hyperbolic tangent function to the result, and add 1 to the result
