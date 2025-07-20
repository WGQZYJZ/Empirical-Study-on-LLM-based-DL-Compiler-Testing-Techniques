input_data = torch.tensor(np.array([(- 0.9), (- 0.7), (- 0.5), (- 0.3), (- 0.1), 0.1, 0.3, 0.5, 0.7, 0.9]))
output = torch.nn.functional.hardshrink(input_data)