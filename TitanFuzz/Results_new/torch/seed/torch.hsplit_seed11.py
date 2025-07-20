x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
y = torch.hsplit(x, 2)