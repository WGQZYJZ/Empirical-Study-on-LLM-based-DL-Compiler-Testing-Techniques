t1  = torch.nn.Conv2d(3, 8, kernel_size) # Apply a convolution operation to an input with a given number of channels and a given kernel size.
t2  = conv(input).view(-1, 64*8)  # Reshape the output of t1 in a way that there are no 3d dimensions left.
t3  = torch.softmax(t2, dim=1) + 0.7  # Apply SoftMax to the output of t2 and add a constant.
