t1  = conv(input_tensor)  # Apply a 3x3 convolution with the input tensor
t2  = t1  -  other   # Subtract 'other' from the output of the convolution
t3  = t2 * 0.5       # Multiply the output of the convolution by 0.5, and then add another 0.5 to its result
