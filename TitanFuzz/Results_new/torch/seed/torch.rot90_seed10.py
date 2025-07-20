input = torch.randn(3, 4, 5)
output = torch.rot90(input, 1, dims=(1, 2))