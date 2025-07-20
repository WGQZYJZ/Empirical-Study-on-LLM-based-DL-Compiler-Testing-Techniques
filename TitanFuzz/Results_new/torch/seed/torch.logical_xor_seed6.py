input = torch.tensor([[True, False], [True, True], [False, False]])
other = torch.tensor([[True, False], [False, True], [False, False]])
output = torch.logical_xor(input, other)