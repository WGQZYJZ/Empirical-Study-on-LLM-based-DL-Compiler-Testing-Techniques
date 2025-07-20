x = torch.arange(0, 16, dtype=torch.float32)
out1 = torch.hsplit(x, 4)
out2 = torch.hsplit(x, [3, 7])