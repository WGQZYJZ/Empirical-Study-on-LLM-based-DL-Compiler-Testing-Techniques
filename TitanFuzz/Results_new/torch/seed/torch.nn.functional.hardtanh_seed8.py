input_data = torch.randn(4, 5)
output = torch.nn.functional.hardtanh(input_data)
output = torch.nn.functional.hardtanh(input_data, min_val=0, max_val=1)