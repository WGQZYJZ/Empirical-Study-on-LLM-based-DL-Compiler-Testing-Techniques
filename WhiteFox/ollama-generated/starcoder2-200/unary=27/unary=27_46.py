t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 2 to the input tensor. 
t3 = t1 * 0.5 # Multiply the output of the convolution by 0.5
t4 = torch.erf(t3) + 1 # Add 1 to the output of the convolution and then apply an error function on it. 
t2 = t1 / 2 # Divide the output of the convolution by 2
