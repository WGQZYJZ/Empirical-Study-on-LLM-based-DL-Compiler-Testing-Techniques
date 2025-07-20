input_data = torch.rand(2, 3, 4, 5)
output_data = torch.empty_strided(input_data.size(), input_data.stride())