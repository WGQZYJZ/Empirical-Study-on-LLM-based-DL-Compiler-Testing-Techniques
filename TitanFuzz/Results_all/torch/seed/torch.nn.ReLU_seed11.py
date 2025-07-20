input = torch.randn(1, 1, 2, 2)
output = torch.nn.ReLU(inplace=False)(input)