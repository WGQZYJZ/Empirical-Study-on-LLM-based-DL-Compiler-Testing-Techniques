input = torch.arange(0, 4, 1, dtype=torch.float32)
output = torch.cumsum(input, dim=0)