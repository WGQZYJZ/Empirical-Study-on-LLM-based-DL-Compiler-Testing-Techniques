x = torch.arange(16, dtype=torch.float32).view(4, 4)
y = torch.hsplit(x, 2)