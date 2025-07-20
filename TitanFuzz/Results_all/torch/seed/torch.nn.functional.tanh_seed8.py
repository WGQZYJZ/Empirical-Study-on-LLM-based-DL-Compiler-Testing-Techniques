input_data = torch.randn(1, 1, 3, 3)
output_data = torch.nn.functional.tanh(input_data)