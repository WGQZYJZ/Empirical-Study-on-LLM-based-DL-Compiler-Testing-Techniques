y = torch.rand(2, 3, 4, 5)
x = torch.arange(5, dtype=torch.float)
output = torch.trapezoid(y, x)