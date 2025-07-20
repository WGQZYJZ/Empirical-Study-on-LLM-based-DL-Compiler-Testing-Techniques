input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.cumsum(input_data, dim=0)
output = torch.cumsum(input_data, dim=1)