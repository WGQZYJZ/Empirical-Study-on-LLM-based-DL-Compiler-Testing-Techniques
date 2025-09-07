t1  = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2  = t1  -  other   # Subtract a tensor or scalar "other" from the output of the convolution
t3  = t2  + relu(t2)# Add the ReLU activation function on top of the result
