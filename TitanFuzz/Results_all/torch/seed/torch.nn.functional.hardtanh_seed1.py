input = torch.randn(3, 3)
output = torch.nn.functional.hardtanh(input, min_val=(- 1.0), max_val=1.0, inplace=False)