input = torch.randn(4, 3, 10, 10)
output = torch.rot90(input, 1, (2, 3))