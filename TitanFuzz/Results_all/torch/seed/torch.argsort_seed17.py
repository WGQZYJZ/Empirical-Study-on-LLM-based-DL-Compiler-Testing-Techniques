input = torch.randn(3, 5)
output = torch.argsort(input, dim=(- 1), descending=False)