input_data = torch.tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0]])
output_data = torch.any(input_data, dim=1)