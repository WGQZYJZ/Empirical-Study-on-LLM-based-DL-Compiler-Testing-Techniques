t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5            # Multiply the output of the convolution by a constant
t3 = t2 + 1              # Add another constant value to the output of the multiplication
t1 = conv(input_tensor)   # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5             # Multiply the output of the convolution by a constant
t3 = torch.softmax(t1, dim=1)  # Apply softmax to the output of the multiplication as well as a keyword argument "dim"
