input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
output_data = torch.nn.functional.elu(input_data)
output_data = torch.nn.functional.elu(input_data, alpha=0.5)