input = torch.randn(10, 10)
torch.clip(input, min=(- 0.5), max=0.5)