input = torch.randn(10000)
torch.histc(input, bins=100, min=0, max=0, out=None)