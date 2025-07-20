x = torch.randn(5, 3)
y = torch.clamp(x, min=(- 0.5), max=0.5)