x = torch.rand(3, 3)
y = torch.sum(x, dim=1)
y = torch.sum(x, dim=1, keepdim=True)