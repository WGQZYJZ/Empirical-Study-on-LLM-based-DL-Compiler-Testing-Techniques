input_data = torch.rand(3, 3)
output = torch.nn.functional.hardtanh_(input_data)