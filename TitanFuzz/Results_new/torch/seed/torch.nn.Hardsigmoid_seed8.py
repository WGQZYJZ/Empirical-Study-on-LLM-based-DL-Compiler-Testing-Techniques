input_data = torch.randn(1, 3, 3, 3)
hardsigmoid = torch.nn.Hardsigmoid(inplace=False)
output = hardsigmoid(input_data)