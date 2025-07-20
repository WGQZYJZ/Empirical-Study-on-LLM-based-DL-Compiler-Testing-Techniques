input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = torch.isin(input_data, torch.tensor([2, 3, 4, 5, 6, 7]))
result = torch.isin(input_data, torch.tensor([2, 3, 4, 5, 6, 7]), invert=True)