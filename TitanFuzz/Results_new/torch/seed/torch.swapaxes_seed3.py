input = torch.randn(2, 3, 4)
output = torch.swapaxes(input, 0, 1)
output = torch.swapaxes(input, 1, 2)
output = torch.swapaxes(input, 0, 2)