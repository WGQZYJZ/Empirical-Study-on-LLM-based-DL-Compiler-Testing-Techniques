input_data = torch.randn(5, 4)
output_data = torch.nn.functional.hardtanh_(input_data, min_val=(- 1.0), max_val=1.0)