input = torch.randn(1, 64, 8)
output = torch.nn.AdaptiveMaxPool1d(3)(input)