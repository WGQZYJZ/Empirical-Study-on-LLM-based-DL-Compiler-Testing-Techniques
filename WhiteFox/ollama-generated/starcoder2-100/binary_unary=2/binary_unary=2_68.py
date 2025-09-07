t1  = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2  = t1  * 0.5   # Multiply the output of the convolution by a constant 0.5
t3  = relu(t2)    # Apply the ReLU (Rectified Linear Unit) activation function to the result
