input_data = torch.randn(2, 3)
torch.nn.functional.hardtanh_(input_data, min_val=(- 1.0), max_val=1.0)