input_data = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
output_data = torch.bitwise_left_shift(input_data, 1)