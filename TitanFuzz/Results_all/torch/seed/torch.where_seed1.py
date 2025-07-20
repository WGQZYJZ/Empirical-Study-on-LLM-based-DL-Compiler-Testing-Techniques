x = torch.randn(5, 5)
y = torch.randn(5, 5)
z = torch.where((x > 0), x, y)