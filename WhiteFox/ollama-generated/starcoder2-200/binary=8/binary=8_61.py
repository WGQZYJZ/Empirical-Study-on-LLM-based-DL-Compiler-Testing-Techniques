t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * other        # Multiply another tensor to the output of the convolution
other = torch.randn(*t1.shape)   # Use the shape of an existing tensor as the shape for a new tensor and then create this new tensor using a random initializer function
