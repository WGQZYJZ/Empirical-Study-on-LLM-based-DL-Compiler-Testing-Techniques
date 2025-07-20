data = torch.arange(0, 24).reshape(4, 6)
result = torch.hsplit(data, 2)
result = torch.hsplit(data, 3)