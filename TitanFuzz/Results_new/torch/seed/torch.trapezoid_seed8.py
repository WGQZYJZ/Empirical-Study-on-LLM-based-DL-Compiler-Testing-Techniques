y = torch.randn(2, 3, 4, 5)
y = torch.trapezoid(y)
y = torch.randn(2, 3, 4, 5)
y = torch.trapezoid(y, dx=0.5)
y = torch.randn(2, 3, 4, 5)
y = torch.trapezoid(y, dx=0.5, dim=2)
y = torch.randn(2, 3, 4, 5)
y = torch.trapezoid(y, dx=0.5, dim=(- 2))
y = torch.randn(2, 3, 4, 5)
y = torch.trapezoid(y, dx=0.5, dim=(- 1))
y = torch.randn(2, 3, 4, 5)
y = torch.trapezoid(y, dx=0.5, dim=1)