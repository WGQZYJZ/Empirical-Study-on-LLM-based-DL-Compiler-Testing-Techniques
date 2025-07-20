input = torch.arange(0, 16, dtype=torch.float32).view(4, 4)
output = torch.as_strided(input, (2, 4), (2, 4))