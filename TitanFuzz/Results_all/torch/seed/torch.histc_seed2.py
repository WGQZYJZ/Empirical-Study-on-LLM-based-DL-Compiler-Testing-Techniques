input = torch.randn(1000)
torch.histc(input, bins=100, min=0, max=0)