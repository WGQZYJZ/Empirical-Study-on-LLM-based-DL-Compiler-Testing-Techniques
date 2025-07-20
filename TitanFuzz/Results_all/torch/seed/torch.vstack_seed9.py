x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.vstack((x, y))
z = torch.cat((x, y), dim=0)