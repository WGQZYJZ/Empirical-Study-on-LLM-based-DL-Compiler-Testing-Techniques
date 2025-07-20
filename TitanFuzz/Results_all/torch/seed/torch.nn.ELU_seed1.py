input_data = torch.tensor([(- 1.0), 1.0, 2.0])
elu = torch.nn.ELU()
output_data = elu(input_data)