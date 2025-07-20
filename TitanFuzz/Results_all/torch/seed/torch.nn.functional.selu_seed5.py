input_data = torch.randn(1, 1, 3, 3)
output_data = torch.nn.functional.selu(input_data)