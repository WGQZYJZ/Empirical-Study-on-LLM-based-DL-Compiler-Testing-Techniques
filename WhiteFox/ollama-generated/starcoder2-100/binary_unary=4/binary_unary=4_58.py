t1 = conv(input_tensor, bias=None) # Apply pointwise convolution to the input tensor without a bias term. 
t2 = t1 * 0.5 # Multiply the output of the convolution by 0.5.
t3 = t1 + 1 # Add 1 to the output of the convolution. The result is the value of the ReLU activation function.

