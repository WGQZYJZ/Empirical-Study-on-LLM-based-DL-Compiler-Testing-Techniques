input = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.int64)
other = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.int64)
result = torch.bitwise_and(input, other)