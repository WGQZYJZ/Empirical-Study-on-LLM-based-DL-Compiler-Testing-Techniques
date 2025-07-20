input_data = torch.arange(1, 10).view(3, 3)
output_data = torch.rot90(input_data, 1, dims=(1, 0))