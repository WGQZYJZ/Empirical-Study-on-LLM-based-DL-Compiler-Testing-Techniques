x = torch.randn(2, 3)
y = torch.clip(x, min=(- 0.5), max=0.5)