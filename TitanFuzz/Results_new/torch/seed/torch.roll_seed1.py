input = torch.arange(12).reshape(3, 4)
output = torch.roll(input, 1, dims=1)