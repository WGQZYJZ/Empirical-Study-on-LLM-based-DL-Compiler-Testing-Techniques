t1  = conv_0 (input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor for conv_0.
t2  = conv_1 (conv_0(input_tensor)) # Apply pointwise convolution with kernel size 1 to output of conv_0 on the input tensor.
