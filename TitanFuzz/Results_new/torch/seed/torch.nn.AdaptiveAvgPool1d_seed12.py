input = torch.randn(1, 1, 8)
output = torch.nn.AdaptiveAvgPool1d(3)(input)