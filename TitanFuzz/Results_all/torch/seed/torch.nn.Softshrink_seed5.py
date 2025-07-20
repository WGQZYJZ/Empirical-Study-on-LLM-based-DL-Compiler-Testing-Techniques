input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
softshrink = torch.nn.Softshrink(lambd=0.5)