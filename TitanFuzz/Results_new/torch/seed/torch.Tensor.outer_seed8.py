x = torch.arange(1, 6, dtype=torch.float)
y = torch.arange(1, 6, dtype=torch.float)
z = torch.Tensor.outer(x, y)