input_data = torch.randn(2, 3)
hard_tanh = torch.nn.Hardtanh()
output = hard_tanh(input_data)