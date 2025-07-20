input = torch.randn(1, 3, 10)
output = torch.nn.AdaptiveMaxPool1d(3)(input)