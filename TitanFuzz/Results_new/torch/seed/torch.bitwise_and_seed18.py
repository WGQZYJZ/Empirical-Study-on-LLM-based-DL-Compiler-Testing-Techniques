input = torch.tensor([[True, True, False], [True, False, False]], dtype=torch.bool)
other = torch.tensor([[True, True, False], [True, False, True]], dtype=torch.bool)
torch.bitwise_and(input, other)