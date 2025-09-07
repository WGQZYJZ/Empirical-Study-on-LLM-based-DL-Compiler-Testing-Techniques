t1 = conv(input_tensor)# Apply pointwise convolution with kernel size 1 to the input tensor
t2 = conv_transpose(input_tensor, output_size, stride=stride)# Apply transposed convolutional layer to the output of the convolution. The parameters for this layer are the size of the output and the amount by which the output will be divided by each dimension (stride) 
