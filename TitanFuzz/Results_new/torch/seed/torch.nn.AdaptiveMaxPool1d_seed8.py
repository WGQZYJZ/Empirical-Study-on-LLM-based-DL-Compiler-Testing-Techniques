input_data = torch.randn(1, 1, 7)
output_data = torch.nn.AdaptiveMaxPool1d(3)(input_data)