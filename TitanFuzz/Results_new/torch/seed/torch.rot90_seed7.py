input = torch.arange(24).view(2, 3, 4)
output = torch.rot90(input, 1, dims=(1, 2))