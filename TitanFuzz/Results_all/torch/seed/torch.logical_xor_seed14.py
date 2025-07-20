input = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
other = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
output = torch.logical_xor(input, other)