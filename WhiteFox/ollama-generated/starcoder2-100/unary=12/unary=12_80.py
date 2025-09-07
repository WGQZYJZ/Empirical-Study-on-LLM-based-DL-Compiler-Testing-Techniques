t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 2 to the input tensor.
t2 = t1 * 0.75  # Multiply the output of the convolution by a constant 0.75.
t3 = maxpool(input_tensor) # Apply max pooling function to the input tensor.
