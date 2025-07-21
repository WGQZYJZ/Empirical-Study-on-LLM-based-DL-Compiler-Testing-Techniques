t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 + 3  # Add 3 to the output of the convolution
t3 = torch.clamp_min(t2, 0)  # Clamp the minimum value of t2 to 0
t4 = torch.clamp_max(t3, 6)  # Clamp the maximum value of t3 to 6
t5 = t4 / 6  # Divide the result by 6
