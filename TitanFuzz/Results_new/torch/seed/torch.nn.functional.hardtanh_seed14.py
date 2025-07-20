input_data = torch.randn(1, 1, 2, 2)
output_data = torch.nn.functional.hardtanh(input_data)