input_data = torch.arange(0, 12).view(3, 4)
index_data = torch.tensor([0, 2])
output_data = torch.index_select(input_data, 0, index_data)