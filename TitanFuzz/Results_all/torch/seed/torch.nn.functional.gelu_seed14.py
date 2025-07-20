input_data = torch.randn(1, 1, 32, 32)
output = torch.nn.functional.gelu(input_data)