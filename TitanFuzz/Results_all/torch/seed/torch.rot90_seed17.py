input_data = torch.rand(3, 4)
rotated_data = torch.rot90(input_data, 2, dims=(0, 1))