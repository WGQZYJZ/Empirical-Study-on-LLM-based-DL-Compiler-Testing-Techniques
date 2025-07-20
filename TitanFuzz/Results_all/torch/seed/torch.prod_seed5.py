input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.prod(input_data, dim=1, keepdim=True)