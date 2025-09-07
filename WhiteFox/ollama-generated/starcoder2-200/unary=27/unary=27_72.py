t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor 
t2 = torch.nn.functional.interpolate(t1, scale_factor=(2), mode='nearest') # Interpolate the output of the convolution using nearest neighbor interpolation by a factor of 2 along each spatial dimension 
