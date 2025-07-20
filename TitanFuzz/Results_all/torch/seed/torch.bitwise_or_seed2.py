input = torch.tensor([[1, 0, 1], [1, 1, 0], [0, 1, 0]], dtype=torch.bool)
other = torch.tensor([[1, 1, 0], [0, 0, 1], [1, 1, 1]], dtype=torch.bool)
out = torch.bitwise_or(input, other)