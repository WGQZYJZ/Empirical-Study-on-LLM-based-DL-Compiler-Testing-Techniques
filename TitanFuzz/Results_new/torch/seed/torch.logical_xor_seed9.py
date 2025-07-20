input = torch.tensor([[True, False], [False, True]])
other = torch.tensor([[True, False], [True, False]])
torch.logical_xor(input, other)