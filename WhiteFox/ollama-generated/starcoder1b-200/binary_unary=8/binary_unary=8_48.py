t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * other  # Multiply by another tensor
t3 = t2 * 0.5 + t1  # Add the result of multiplying the output of the previous convolution and adding its input tensor
