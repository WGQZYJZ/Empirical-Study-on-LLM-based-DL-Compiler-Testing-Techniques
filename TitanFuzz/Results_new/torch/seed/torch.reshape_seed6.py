input = torch.randn(2, 3)
output = torch.reshape(input, (6, 1))
output = torch.reshape(input, (3, 2))
output = torch.reshape(input, (1, 6))