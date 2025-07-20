input = torch.rand(3, 4)
result = torch.argsort(input, dim=(- 1), descending=False)