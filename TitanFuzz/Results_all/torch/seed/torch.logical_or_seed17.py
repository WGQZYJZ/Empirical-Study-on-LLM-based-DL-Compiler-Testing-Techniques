input = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.bool)
other = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.bool)
output = torch.logical_or(input, other)