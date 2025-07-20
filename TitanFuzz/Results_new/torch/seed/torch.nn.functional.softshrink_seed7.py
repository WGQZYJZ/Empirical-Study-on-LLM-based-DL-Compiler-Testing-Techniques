input_data = torch.randn(5, 10)
output_data = torch.nn.functional.softshrink(input_data)