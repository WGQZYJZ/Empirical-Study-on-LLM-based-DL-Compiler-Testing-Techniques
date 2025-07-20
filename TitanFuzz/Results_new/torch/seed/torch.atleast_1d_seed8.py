input_data = torch.rand(1, 2, 3, 4)
output_data = torch.atleast_1d(input_data)
output_data = torch.atleast_2d(input_data)
output_data = torch.atleast_3d(input_data)