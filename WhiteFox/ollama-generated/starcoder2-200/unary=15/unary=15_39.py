t1 = conv(input_tensor)# Apply pointwise convolution with kernel size 1 to the input tensor
t2 = tanh(conv(conv(tanh(t1)))) # Apply a three-layered hierarchical operation using tanh functions.
t1 = conv(input_tensor)# Apply a pointwise convolution to the input tensor
t2 = tanh(conv(t1)) # Apply a ReLU activation function after applying another pointwise convolution.
