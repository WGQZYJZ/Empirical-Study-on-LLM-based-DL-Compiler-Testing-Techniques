input = torch.tensor([[1, 2], [3, 4]], dtype=torch.int32)
other = torch.tensor([[1, 1], [1, 1]], dtype=torch.int32)
output = torch.bitwise_right_shift(input, other)