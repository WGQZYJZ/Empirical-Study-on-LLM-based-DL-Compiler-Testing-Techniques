x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.stack((x, y))
z = torch.stack((x, y), dim=1)