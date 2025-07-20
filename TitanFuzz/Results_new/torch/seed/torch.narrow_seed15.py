input = torch.randn(4, 8)
output = torch.narrow(input, 0, 1, 3)