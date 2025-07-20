x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[1, 1], [1, 1]])
torch.mul(x, y)
torch.mul(x, y, out=x)