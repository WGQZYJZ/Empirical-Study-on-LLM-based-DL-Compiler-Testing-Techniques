t1  = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2  = t1 + other # Add 'other' from the output of the convolution
t3 = sigmoid(t1) - 0.5 # Apply the sigmoid function and subtract 0.5 from the output of the convolution
