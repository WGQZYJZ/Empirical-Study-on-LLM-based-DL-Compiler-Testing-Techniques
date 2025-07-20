x = torch.randint(0, 10, (2, 3, 4))
y = torch.flatten(x, start_dim=1, end_dim=(- 1))