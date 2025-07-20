input = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=torch.int32)
other = torch.tensor([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype=torch.int32)
output = torch.bitwise_left_shift(input, other)