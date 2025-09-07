t1 = conv_transpose(input_tensor) # Apply pointwise transposed convolution to the input tensor
t2 = torch.relu6(t1)# Apply the ReLU function with upper bound parameter to the output of the transposed convolution
t1 =  conv(input_tensor) # Apply pointwise convolution with kernel size 2 to the input tensor
t2 = t1 * 3   # Multiply the output of the convolution by a constant 3
