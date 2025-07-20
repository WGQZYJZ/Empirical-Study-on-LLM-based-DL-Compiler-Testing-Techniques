input_data = torch.rand(1, 3)
output = torch.min(input_data, 1)
output = torch.min(input_data, 0)