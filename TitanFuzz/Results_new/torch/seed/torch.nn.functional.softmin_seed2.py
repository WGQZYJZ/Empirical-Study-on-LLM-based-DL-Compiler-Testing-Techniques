x = torch.randn(3, 4)
y = torch.nn.functional.softmin(x, dim=0)