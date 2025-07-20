x = torch.arange(1, 5, dtype=torch.float)
y = torch.arange(1, 5, dtype=torch.float)
result = torch.cumulative_trapezoid(y, x=x)