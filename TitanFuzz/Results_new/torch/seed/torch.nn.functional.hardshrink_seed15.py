input_data = torch.randn(10)
output_data = torch.nn.functional.hardshrink(input_data, lambd=0.5)