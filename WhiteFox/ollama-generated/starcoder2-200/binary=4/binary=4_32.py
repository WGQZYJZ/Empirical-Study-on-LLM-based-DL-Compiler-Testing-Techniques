t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 3 to the input tensor.
t2 = linear(t1) # Apply a linear transformation to the output of the convolution.
t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 5 to the input tensor.
t2 = torch.nn.Linear(7 * 7, 300)(t1) # Apply a linear transformation (with a number of output features equal to 300) to the output of the convolution. This pattern is commonly used in convolutional neural networks.
