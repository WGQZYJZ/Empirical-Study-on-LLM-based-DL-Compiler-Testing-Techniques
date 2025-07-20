input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])
hardsigmoid = torch.nn.Hardsigmoid()
output = hardsigmoid(input_data)