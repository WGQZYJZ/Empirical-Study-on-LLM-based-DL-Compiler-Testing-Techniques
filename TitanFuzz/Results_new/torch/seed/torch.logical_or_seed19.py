input = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
other = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
output = torch.logical_or(input, other)