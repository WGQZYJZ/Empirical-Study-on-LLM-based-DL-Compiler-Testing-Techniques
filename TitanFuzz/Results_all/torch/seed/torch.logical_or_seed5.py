x = torch.tensor([[True, True], [True, False]], dtype=torch.bool)
y = torch.tensor([[False, True], [True, False]], dtype=torch.bool)
out = torch.logical_or(x, y)