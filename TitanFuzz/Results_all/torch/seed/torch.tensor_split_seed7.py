input_data = torch.arange(start=0, end=24, dtype=torch.float32).reshape(2, 3, 4)
output_data = torch.tensor_split(input_data, [1, 2, 1], dim=0)