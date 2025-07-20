input = torch.tensor([[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]], dtype=torch.bool)
other = torch.tensor([[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]], dtype=torch.bool)
result = torch.bitwise_or(input, other)