x = torch.arange(0, 9, dtype=torch.float32).view(3, 3)
y = torch.arange(9, 18, dtype=torch.float32).view(3, 3)
z = torch.vstack((x, y))