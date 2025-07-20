x = torch.arange(1, 5)
y = torch.arange(1, 5)
out = torch.cumulative_trapezoid(y, x)