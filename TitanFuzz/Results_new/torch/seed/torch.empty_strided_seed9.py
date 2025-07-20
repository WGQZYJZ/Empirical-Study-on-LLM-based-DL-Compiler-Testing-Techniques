input_data = torch.randn(3, 3, 3, 3)
output_data = torch.empty_strided(input_data.shape, input_data.stride())