t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1  + 0.5 # Add 0.5 to the output of the convolution
t3 = t1 * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
t4 = torch.erf(t3) # Apply the error function to the output of the convolution
t5 = t2 + 1 # Add 1 to the output of the convolution
t6 = v2 * t1  # Multiply the output of the convolution by its first input
