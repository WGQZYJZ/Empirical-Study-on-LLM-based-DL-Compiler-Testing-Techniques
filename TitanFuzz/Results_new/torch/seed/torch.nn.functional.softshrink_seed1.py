input_data = torch.randn(2, 3)
output_data = torch.nn.functional.softshrink(input_data, lambd=0.5)