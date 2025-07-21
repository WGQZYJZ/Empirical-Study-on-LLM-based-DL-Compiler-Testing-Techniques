y = torch.randn(5, 3, 3)
out = torch.cumulative_trapezoid(y, dx=1)