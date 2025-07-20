input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_data = torch.cummin(input_data, dim=0)
output_data = torch.cummin(input_data, dim=1)