input_data = torch.tensor([[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 0]])
output = torch.nonzero(input_data)
output_tuple = torch.nonzero(input_data, as_tuple=True)