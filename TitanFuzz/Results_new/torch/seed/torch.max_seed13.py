input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
max_value = torch.max(input_data, dim=0)
max_value = torch.max(input_data, dim=1)