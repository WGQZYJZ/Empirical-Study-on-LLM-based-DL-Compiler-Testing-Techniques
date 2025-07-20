data = torch.tensor([[0, 1, 2], [3, 4, 5]])
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.scatter(data, 0, index, src)