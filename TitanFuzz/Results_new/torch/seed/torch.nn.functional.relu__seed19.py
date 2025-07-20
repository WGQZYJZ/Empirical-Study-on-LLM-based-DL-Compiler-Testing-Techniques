input_data = torch.tensor([(- 1), 2, 3, (- 5), (- 8), 0, (- 9), 2], dtype=torch.float)
output = torch.nn.functional.relu_(input_data)