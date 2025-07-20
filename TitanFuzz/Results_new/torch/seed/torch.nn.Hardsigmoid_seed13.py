input_data = np.array([[(- 1), (- 0.5), 0, 0.5, 1]])
input_data = torch.from_numpy(input_data)
hardsigmoid = torch.nn.Hardsigmoid()
output = hardsigmoid(input_data)