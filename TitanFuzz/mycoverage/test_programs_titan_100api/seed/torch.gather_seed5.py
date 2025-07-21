x = torch.tensor([[1, 2, 3], [4, 5, 6]])
index = torch.tensor([[1, 1, 1], [1, 1, 1]])
y = torch.gather(x, dim=1, index=index)