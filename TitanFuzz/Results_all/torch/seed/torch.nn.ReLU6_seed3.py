input = torch.randn(1, 1, 3, 3)
relu6 = torch.nn.ReLU6(inplace=False)
output = relu6(input)