input = torch.arange(0, 16, dtype=torch.float).view(4, 4)
output = torch.rot90(input, 1, (0, 1))