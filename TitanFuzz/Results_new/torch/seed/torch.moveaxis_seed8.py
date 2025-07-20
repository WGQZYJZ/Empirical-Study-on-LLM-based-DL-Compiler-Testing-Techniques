input = torch.rand(2, 3, 4)
output = torch.moveaxis(input, 0, 1)