input_data = torch.tensor([[(- 1.0), (- 0.5), 0.0, 0.5, 1.0]])
sigmod_input = torch.nn.SiLU(inplace=False)
output = sigmod_input(input_data)