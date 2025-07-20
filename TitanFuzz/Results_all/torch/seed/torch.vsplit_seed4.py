input_data = torch.arange(9, dtype=torch.float).reshape(3, 3)
output_data = torch.vsplit(input_data, [1, 2])
output_data = torch.vsplit(input_data, [1])