x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[1, 1, 1], [1, 1, 1]])
z = torch.sub(x, y)
z = torch.sub(x, y, out=torch.empty(x.shape))
z = torch.sub(x, y, alpha=2)
z = torch.sub(x, y, alpha=2, out=torch.empty(x.shape))