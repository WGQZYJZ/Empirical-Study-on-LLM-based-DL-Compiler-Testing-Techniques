input = torch.randn(4, 3, 5)
output = torch.moveaxis(input, 0, 1)