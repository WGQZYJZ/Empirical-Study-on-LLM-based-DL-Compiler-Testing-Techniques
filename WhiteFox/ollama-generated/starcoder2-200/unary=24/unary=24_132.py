 t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 2 to the input tensor
 t2 = torch.relu6(t1, inplace=True)  # Compute a ReLU6 function on each element of t1 using an inplace operation, which means that the output replaces the input without creating any new variable.
