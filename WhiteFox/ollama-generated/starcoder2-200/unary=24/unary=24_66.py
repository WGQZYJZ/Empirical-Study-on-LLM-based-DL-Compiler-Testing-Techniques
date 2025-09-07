t1  =  conv(input_tensor) # Apply pointwise convolution with kernel size 3 to the input tensor
t2  =  maxpooling()        # Max pooling layer
t3  =  relu()              # ReLU activation function
t4  =  t2(t1)               # Pass the output of the conv as input to a maxpooling operation
