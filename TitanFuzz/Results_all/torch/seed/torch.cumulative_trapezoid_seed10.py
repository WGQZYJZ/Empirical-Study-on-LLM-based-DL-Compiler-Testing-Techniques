y = torch.randn(2, 3, 4)
x = torch.randn(2, 3, 4)
res = torch.cumulative_trapezoid(y, x)