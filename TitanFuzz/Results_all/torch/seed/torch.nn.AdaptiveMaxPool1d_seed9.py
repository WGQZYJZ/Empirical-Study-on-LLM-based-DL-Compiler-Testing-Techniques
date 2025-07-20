input_data = torch.randint(1, 10, (3, 3, 4), dtype=torch.float32)
output_size = 2
output_data = torch.nn.AdaptiveMaxPool1d(output_size)(input_data)
input_data = torch.randint(1, 10, (3, 3, 4, 4), dtype=torch.float32)