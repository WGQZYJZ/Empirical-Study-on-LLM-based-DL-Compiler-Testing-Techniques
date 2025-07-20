x = torch.randn(1, 2, 3)
y = torch.clamp(x, min=(- 0.5), max=0.5)