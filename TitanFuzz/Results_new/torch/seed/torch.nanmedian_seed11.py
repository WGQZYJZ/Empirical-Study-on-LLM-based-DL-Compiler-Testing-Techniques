input_data = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
result = torch.nanmedian(input_data)
result = torch.nanmedian(input_data, dim=0)
result = torch.nanmedian(input_data, dim=1)