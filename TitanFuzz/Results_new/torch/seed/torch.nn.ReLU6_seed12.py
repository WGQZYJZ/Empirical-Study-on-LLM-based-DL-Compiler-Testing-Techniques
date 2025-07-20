input = torch.randn(1, 3, 3, 3)
out = torch.nn.ReLU6(inplace=False)(input)