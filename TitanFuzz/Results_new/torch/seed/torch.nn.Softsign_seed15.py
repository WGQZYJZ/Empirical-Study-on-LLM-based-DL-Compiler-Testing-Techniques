input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1], dtype=torch.float)
softsign_activation = torch.nn.Softsign()
output = softsign_activation(input_data)