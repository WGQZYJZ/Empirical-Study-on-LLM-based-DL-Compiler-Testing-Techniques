input_data = torch.arange(12, dtype=torch.float32).reshape(3, 4)
output_data = torch.amin(input_data, 1, False)