t1  =  conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2  =  t1 * 0.5 + t1  # The output of the convolution is multiplied by 0.5, then added to itself to get another output of the convolution
