input = torch.tensor([[1, 2, 3], [0, 0, 0], [4, 5, 6], [0, 0, 0]])
result = torch.nonzero(input)
result = torch.nonzero(input, as_tuple=True)