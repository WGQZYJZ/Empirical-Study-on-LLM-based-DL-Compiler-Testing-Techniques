input = torch.randn(1, 3, 10)
output = torch.nn.AdaptiveAvgPool1d(3)(input)