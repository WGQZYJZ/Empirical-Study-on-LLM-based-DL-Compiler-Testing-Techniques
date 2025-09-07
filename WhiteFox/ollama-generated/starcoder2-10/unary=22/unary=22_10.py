t1 = linear(input_tensor)  # Apply a linear transformation to the input tensor.
t2 = tanh(t1)              # Apply hyperbolic tangent function to the output of the linear transformation.
t3 = dropout(t2, p=0.4)    # Dropout the output of the linear transformation with probability 0.4.
