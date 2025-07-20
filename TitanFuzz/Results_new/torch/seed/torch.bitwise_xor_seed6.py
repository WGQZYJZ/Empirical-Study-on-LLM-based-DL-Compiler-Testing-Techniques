input = torch.tensor([[0, 1, 0], [1, 0, 1]], dtype=torch.bool)
other = torch.tensor([[0, 1, 1], [1, 0, 0]], dtype=torch.bool)
output = torch.bitwise_xor(input, other)