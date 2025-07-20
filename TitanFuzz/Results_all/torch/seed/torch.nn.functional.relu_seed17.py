input_data = torch.tensor([(- 1.0), 1.0, 3.0], dtype=torch.float)
output = torch.nn.functional.relu(input_data)