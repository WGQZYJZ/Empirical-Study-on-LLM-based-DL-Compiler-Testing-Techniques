t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = torch.clamp_min(t1, min_value) # Clamp the output of the convolution to have a minimum value of 'min_value'
t3 = torch.clamp_max(t2, max_value) # Clamp the result of the minimum clamp to have a maximum value of 'max_value'
