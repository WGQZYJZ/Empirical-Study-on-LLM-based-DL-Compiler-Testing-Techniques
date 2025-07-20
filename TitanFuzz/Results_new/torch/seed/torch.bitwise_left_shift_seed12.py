input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.bitwise_left_shift(input_data, other)