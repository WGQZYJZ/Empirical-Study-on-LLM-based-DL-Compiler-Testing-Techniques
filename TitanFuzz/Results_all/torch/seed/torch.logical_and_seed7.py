input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
other_tensor = torch.tensor([[1, 0, 1], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
result = torch.logical_and(input_tensor, other_tensor)