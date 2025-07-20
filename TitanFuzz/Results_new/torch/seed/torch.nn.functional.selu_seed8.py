input_data = torch.randn(1, 2, 3)
output_data = torch.nn.functional.selu(input_data)