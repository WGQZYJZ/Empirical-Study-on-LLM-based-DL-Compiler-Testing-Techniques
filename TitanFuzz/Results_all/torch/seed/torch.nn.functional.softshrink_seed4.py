input_data = torch.randn(4, 4)
output = torch.nn.functional.softshrink(input_data)