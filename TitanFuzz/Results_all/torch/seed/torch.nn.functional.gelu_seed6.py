input_data = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.gelu(input_data)