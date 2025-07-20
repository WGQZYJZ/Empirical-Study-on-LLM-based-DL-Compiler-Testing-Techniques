input = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
output = torch.nanmedian(input)
output = torch.nanmedian(input, dim=0)