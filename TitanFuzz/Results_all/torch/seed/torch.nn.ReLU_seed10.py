input = torch.randn(1, 3, 3, 3)
relu = torch.nn.ReLU(inplace=False)
output = relu(input)