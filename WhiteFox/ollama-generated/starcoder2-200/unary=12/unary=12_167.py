t1  = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor, this is a "down-sample" operation
t2  = F.maxpool2d(t1) # Apply the max pooling operation on the output of the down sample
