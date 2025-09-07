t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 3 to the input tensor 
t2 = t1 + t1  # Add another copy of the output of the convolution 
t3 = t2 * 0.5  # Multiply by another constant, 0.5
