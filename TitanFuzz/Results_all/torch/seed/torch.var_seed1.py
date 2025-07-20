input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
output = torch.var(input_data, dim=1, unbiased=False, keepdim=False)