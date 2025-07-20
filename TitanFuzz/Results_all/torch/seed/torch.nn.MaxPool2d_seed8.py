input = torch.randn(1, 1, 4, 4)
output = torch.nn.MaxPool2d(kernel_size=2, stride=2)(input)