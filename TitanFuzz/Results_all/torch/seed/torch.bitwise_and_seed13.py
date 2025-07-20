input = torch.tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 0]], dtype=torch.bool)
other = torch.tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 0]], dtype=torch.bool)
result = torch.bitwise_and(input, other)