x = torch.randn(10, 10)
relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
y = relu(x)