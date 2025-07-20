input_data = torch.randn(3, 4)
index_data = torch.tensor([0, 2])
output_data = torch.index_select(input_data, dim=0, index=index_data)