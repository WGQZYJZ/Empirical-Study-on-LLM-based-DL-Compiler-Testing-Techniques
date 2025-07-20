data = torch.randn(4, 4)
result = torch.clamp(data, min=(- 0.5), max=0.5)