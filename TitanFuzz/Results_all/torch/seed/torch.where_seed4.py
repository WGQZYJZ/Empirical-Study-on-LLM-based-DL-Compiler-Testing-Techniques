x = torch.randn(3, 3)
y = torch.randn(3, 3)
condition = (torch.randn(3, 3) > 0)
z = torch.where(condition, x, y)