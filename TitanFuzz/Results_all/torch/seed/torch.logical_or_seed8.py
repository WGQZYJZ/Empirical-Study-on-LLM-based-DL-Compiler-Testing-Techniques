input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
other_data = torch.tensor([[1, 1, 1], [0, 0, 1], [1, 0, 1]], dtype=torch.bool)
output = torch.logical_or(input_data, other_data)
input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)