t0  = torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=1, stride=1, padding=(0,0), dilation=((0,0),(0,0)), groups=1, bias=False)
t7a = torch.relu(t0(t5b))  # Apply the ReLU activation function to the output of the convolution on the left side
