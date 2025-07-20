input = torch.randn(1, 16, 50)
pool = torch.nn.AdaptiveMaxPool1d(5)
output = pool(input)