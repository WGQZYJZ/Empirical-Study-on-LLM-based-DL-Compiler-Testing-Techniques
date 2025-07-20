x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
y = torch.vsplit(x, 2)
x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
y = torch.chunk(x, 2, dim=1)