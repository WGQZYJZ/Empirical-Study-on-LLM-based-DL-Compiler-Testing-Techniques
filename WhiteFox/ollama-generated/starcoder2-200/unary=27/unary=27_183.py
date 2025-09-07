t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = torch.cat([t3] * 5, dim=0)) # Concatenate the output of the convolution with 4 copies of itself in the dimension 0. The number of channels remains constant for all tensors.
