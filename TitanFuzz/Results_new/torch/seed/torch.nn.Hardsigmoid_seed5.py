input_data = torch.randn(5)
hardsigmoid = torch.nn.Hardsigmoid()
output = hardsigmoid(input_data)