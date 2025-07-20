input = torch.randn(2, 3, 4)
output = torch.moveaxis(input, 2, 1)
output = torch.moveaxis(input, 1, (- 1))