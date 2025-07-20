input = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.int8)
other = torch.tensor([[1, 0], [1, 0], [1, 1], [0, 0]], dtype=torch.int8)
output = torch.bitwise_and(input, other)