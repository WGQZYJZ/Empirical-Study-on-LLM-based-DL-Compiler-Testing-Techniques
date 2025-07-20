input = torch.randn(3, 4, 5)
output = torch.moveaxis(input, 2, 0)
output = torch.moveaxis(input, 0, 2)
output = torch.moveaxis(input, 1, 2)