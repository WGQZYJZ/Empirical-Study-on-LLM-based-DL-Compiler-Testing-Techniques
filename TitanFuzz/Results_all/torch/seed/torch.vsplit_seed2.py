x = torch.arange(16, dtype=torch.float32).reshape(2, 8)
y = torch.vsplit(x, 2)