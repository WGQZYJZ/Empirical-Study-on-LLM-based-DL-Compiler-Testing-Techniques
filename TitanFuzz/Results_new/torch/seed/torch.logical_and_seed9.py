input = torch.tensor([[1, 0, 1, 1], [1, 0, 1, 1]])
other = torch.tensor([[1, 1, 1, 0], [0, 0, 1, 1]])
out = torch.logical_and(input, other)