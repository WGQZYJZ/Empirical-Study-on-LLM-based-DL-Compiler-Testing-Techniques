input = torch.randint(0, 2, (3, 3), dtype=torch.bool)
other = torch.tensor([[True, True, True], [True, True, True], [True, True, True]], dtype=torch.bool)
out = torch.bitwise_or(input, other)