input = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.tensor([[False, True], [False, False], [True, True], [True, False]])
output = torch.logical_xor(input, other)