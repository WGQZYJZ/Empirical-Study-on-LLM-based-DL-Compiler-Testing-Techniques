input_data = torch.randn(1, 3)
output = torch.nn.functional.softshrink(input_data, lambd=0.5)