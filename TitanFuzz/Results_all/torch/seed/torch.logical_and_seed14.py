input = torch.tensor([[True, True], [False, False]])
other = torch.tensor([[True, False], [False, False]])
torch.logical_and(input, other)