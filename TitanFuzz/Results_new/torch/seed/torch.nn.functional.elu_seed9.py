input_data = torch.tensor([(- 1.0), 1.0, 2.0, 3.0, 4.0, 5.0])
output_data = torch.nn.functional.elu(input_data)