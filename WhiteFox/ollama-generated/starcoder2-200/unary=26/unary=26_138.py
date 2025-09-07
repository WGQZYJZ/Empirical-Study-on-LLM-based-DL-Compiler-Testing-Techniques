t1  = conv2d(input_tensor) # Apply 2D convolution to input tensor. 
t2  = max(t1, 0) * negative_slope + t1  # Apply a Leaky ReLU operation using the negative slope and applying an additive bias term.
