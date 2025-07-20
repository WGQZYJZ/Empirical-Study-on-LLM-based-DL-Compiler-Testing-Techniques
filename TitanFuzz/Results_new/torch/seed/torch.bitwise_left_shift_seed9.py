input = torch.tensor([[(- 1), 2, 3], [4, 5, 6]], dtype=torch.int32)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
output = torch.bitwise_left_shift(input, other)