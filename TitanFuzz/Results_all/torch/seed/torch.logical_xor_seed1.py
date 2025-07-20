input = torch.tensor([[1, 0], [1, 1], [0, 0], [0, 1]], dtype=torch.bool)
other = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.bool)
result = torch.logical_xor(input, other)