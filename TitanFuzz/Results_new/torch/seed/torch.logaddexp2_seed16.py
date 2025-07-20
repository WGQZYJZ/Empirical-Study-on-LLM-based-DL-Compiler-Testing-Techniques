input_data = torch.arange(1, 10, dtype=torch.float32)
output = torch.logaddexp2(input_data, input_data)