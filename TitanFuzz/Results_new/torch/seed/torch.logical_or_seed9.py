input = torch.tensor([[1, 0, 1], [0, 1, 0]], dtype=torch.bool)
other = torch.tensor([[0, 1, 0], [0, 0, 1]], dtype=torch.bool)
output = torch.logical_or(input, other)