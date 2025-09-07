t0 = torch.nn.Conv2d(32*8, 1, kernel_size=(7, 7), stride=2)(input_tensor) # Apply 3D convolution with kernel size (7, 7) and stride of 2 to the input tensor
t0 = torch.nn.Conv2d(5, 9, kernel_size=(3, 3), stride=2)(input_tensor) # Apply 2D convolution with kernel size (3, 3) and stride of 2 to the input tensor
