input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
hardsigmoid = torch.nn.Hardsigmoid()
output = hardsigmoid(input_data)