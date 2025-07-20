input = torch.randn(3, 4, 5)
result = torch.moveaxis(input, 0, (- 1))