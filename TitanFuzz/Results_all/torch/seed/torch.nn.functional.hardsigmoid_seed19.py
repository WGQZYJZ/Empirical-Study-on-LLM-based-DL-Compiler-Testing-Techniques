x = torch.tensor([(- 1.0), 0.0, 0.5, 1.0])
y = torch.nn.functional.hardsigmoid(x)