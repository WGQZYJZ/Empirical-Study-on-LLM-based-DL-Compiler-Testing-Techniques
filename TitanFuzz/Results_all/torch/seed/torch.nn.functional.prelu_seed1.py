input_data = torch.randn(1, 3, 4, 4)
output_data = torch.nn.functional.prelu(input_data, torch.ones(1))