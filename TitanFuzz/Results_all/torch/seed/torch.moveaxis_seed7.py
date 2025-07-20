input = torch.randn(3, 4, 5)
output = torch.moveaxis(input, 0, 1)
output = torch.moveaxis(input, 1, 2)
output = torch.moveaxis(input, 0, (- 1))