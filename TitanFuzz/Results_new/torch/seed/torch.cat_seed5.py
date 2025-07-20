x = torch.rand(5, 3)
y = torch.rand(5, 3)
z = torch.cat([x, y], dim=0)
x = torch.rand(5, 3)
y = torch.rand(5, 3)
z = torch.stack([x, y], dim=0)
x = torch.rand