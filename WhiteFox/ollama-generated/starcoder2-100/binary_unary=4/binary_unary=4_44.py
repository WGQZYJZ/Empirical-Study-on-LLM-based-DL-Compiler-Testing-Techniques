t1  = linear(input_tensor) # Apply a linear transformation to the input tensor
t2  = sigmoid(t1) # Apply the sigmoid activation function to the output of the linear transformation.
t3  = conv(t2) # Apply a pointwise convolution with kernel size 1 to the output of the sigmoid transformation
