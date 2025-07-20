x = torch.tensor([[True, False], [False, False]])
y = torch.all(x, dim=0)
z = torch.all(x, dim=1)
w = torch.all(x, dim=1, keepdim=True)