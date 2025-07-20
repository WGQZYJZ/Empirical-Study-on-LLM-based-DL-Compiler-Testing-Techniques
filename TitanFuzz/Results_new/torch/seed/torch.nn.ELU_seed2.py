input_data = torch.tensor([(- 1), 0, 1, 2], dtype=torch.float32)
elu = torch.nn.ELU(alpha=1.0, inplace=False)
output_data = elu(input_data)