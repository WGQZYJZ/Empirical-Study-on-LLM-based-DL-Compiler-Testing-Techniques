x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
result = torch.argsort(x, dim=(- 1), descending=False)