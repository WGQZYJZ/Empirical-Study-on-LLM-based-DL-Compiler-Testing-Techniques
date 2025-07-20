input = torch.tensor([[True, False], [False, False]])
other = torch.tensor([[False, False], [True, False]])
output = torch.logical_or(input, other)