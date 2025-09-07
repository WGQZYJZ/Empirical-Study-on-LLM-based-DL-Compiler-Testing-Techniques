t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor.
t2 = t1 * 0.5           # Multiply the output of the convolution by 0.5.
t3 = maxpool(t2, 1)     # Apply 1x1 max pooling operation on the output of the convolution.
t1 = conv(input_tensor)        # Applying pointwise convolution on an input tensor.
t2 = tanh(t1)                  # Applying tanh activation function to output of the convolution.
t3 = maxpool(t2, 4)            # Calculating max-pooing operation with kernel size 4 from the output of the convolution.
