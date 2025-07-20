a = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
b = torch.tensor([[False, True], [True, False]], dtype=torch.bool)
c = torch.logical_or(a, b)