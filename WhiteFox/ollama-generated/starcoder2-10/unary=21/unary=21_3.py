t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 2 to the input tensor
t2 = conv(conv_1(input_tensor))  # Apply pointwise convolution on a pointwise convolution layer, conv1.
