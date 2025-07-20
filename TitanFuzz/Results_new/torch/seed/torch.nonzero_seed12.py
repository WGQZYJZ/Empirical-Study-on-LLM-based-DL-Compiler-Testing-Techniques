x = torch.tensor([[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 1], [1, 0, 1, 1]])
result = torch.nonzero(x)
result = torch.nonzero(x, as_tuple=True)