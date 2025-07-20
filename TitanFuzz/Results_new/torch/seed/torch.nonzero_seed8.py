x = torch.tensor([[1, 0, 0, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 0], [1, 0, 1, 1, 1]])
y = torch.nonzero(x)
y = torch.nonzero(x, as_tuple=True)