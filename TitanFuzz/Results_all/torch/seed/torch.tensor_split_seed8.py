input_data = torch.arange(1, 13)
split_data = torch.tensor_split(input_data, 4, dim=0)