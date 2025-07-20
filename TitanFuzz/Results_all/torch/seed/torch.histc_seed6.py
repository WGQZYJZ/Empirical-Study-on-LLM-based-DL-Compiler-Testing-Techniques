input = torch.randn(100)
hist = torch.histc(input, bins=100, min=0, max=0)