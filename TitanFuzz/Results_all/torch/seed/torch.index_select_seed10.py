input_data = torch.arange(0, 12)
index_data = torch.tensor([1, 3, 5, 7])
output_data = torch.index_select(input_data, dim=0, index=index_data)