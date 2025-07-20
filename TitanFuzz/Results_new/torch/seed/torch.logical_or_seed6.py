a = torch.tensor([False, True, False, True])
b = torch.tensor([False, False, True, True])
c = torch.logical_or(a, b)
d = (a | b)