x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.concat([x, y])
z = torch.concat([x, y], dim=1)