input = torch.randn(3, 4, 5)
output = torch.moveaxis(input, 0, (- 1))