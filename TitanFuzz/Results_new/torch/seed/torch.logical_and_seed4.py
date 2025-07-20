input = torch.tensor([[True, False, True], [True, True, True]], dtype=torch.bool)
other = torch.tensor([[True, False, True], [False, True, False]], dtype=torch.bool)
output = torch.logical_and(input, other)