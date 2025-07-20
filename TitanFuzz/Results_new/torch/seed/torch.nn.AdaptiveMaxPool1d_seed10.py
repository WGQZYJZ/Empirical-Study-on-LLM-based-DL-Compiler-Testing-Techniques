input_data = torch.tensor([[[1, 2], [3, 4], [5, 6], [7, 8]]], dtype=torch.float)
pool_output = torch.nn.AdaptiveMaxPool1d(output_size=3)(input_data)