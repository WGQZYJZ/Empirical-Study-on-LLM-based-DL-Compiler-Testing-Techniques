x = torch.tensor([False, True, True, False])
y = torch.logical_not(x)
z = torch.logical_not(x, out=x)
w = x.logical_not()