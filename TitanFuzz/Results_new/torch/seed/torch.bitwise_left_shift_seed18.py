input_data = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.int8)
other_data = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.int8)
torch.bitwise_left_shift(input_data, other_data)