t1  = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2  = t1 * 0.5  # Multiply the output of the convolution by 0.5
t3  = torch.expm1(t2)  # Apply the expm1 function to the output of the multiplication operation by 0.5
