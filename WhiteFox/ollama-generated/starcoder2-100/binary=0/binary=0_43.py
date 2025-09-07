t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 / 0.5  # Divide the output of the convolution by 0.5
t3 = t1 + other  # Add another tensor to the output of the convolution
