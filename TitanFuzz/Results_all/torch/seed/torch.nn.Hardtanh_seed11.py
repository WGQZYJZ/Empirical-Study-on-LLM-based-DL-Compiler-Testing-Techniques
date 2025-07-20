input_data = torch.randn(1, 3)
output_data = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(input_data)