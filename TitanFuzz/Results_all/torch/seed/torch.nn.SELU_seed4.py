input_data = torch.tensor([[(- 1.0), 1.0], [1.0, (- 1.0)]])
selu = torch.nn.SELU(inplace=False)
output = selu(input_data)