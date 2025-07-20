input_data = torch.tensor([(- 1.0), 1.0, (- 0.5), 0.5])
softshrink = torch.nn.Softshrink(lambd=0.5)
output = softshrink(input_data)