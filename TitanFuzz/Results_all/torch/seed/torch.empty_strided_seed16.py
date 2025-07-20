input_data = torch.ones(2, 3, 4)
output_data = torch.empty_strided(input_data.shape, input_data.stride())