x = torch.randn(3, 3)
y = torch.randn(3, 3)
condition = torch.randn(3, 3)
z = torch.where((condition < 0), x, y)