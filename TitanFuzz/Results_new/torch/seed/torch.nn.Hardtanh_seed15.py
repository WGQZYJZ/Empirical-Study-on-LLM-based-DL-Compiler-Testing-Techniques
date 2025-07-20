input_data = torch.randn(2, 3)
hardtanh = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)
output = hardtanh(input_data)