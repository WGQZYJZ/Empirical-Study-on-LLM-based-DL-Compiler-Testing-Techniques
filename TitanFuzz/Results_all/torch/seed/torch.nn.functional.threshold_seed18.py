input_data = torch.tensor([[(- 1), (- 0.5), 0, 0.5, 1]])
output_data = torch.nn.functional.threshold(input_data, 0.0, 0.0)
output_data = torch.nn.functional.threshold(input_data, 0.0, 0.0, inplace=True)