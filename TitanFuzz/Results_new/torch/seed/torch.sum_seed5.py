x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.sum(x, dim=0)
y = torch.sum(x, dim=1)
y = torch.sum(x, dim=1, keepdim=True)