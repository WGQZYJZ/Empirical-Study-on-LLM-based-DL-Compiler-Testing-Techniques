input_data = torch.tensor([[1, 0], [1, 1], [0, 1]], dtype=torch.float)
output = torch.logical_not(input_data)
output = torch.logical_not(input_data, out=input_data)